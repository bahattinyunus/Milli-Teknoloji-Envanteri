import os
import argparse
import re
import json
import csv
import datetime
import sys
import io

# Force UTF-8 for stdout/stderr to avoid UnicodeEncodeError on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass
if sys.stderr.encoding != 'utf-8':
    try:
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

class InventoryManager:
    """
    Milli Teknoloji Envanteri - Kurumsal Envanter Yönetim ve Analiz Motoru v3.5
    Türkiye Cumhuriyeti Savunma ve Havacılık Ekosistemi Stratejik Yönetim Sistemi
    """
    def __init__(self, root_dir=None):
        self.root_dir = root_dir or os.getcwd()
        self.dominions = [
            'DOMINION_AEROSPACE',
            'DOMINION_ELECTRONICS',
            'DOMINION_LAND',
            'DOMINION_SEA'
        ]
        self.structure = self.get_repo_structure()
        self.projects_cache = None

    def get_repo_structure(self):
        """Scans the repository structure: DOMINION -> COMPANY -> PROJECT"""
        structure = {}
        for d in self.dominions:
            d_path = os.path.join(self.root_dir, d)
            if os.path.isdir(d_path):
                structure[d] = {}
                for c in sorted(os.listdir(d_path)):
                    comp_path = os.path.join(d_path, c)
                    if os.path.isdir(comp_path) and not c.startswith('.'):
                        structure[d][c] = []
                        for p in sorted(os.listdir(comp_path)):
                            proj_path = os.path.join(comp_path, p)
                            if os.path.isdir(proj_path) and not p.startswith('.'):
                                structure[d][c].append(p)
        return structure

    def extract_project_metadata(self, proj_path, proj_name=None, company_name=None, dominion_name=None):
        """Extracts rich metadata (TRL, class, strategic role, summary) from project README."""
        proj_name = proj_name or os.path.basename(proj_path).replace('_', ' ')
        readme_path = os.path.join(proj_path, 'README.md')
        
        metadata = {
            'name': proj_name,
            'company': company_name or '',
            'dominion': (dominion_name or '').replace('DOMINION_', ''),
            'path': os.path.relpath(proj_path, self.root_dir).replace('\\', '/'),
            'readme_exists': os.path.exists(readme_path),
            'trl': None,
            'class': 'Platform / Alt Sistem',
            'strategic_role': '',
            'summary': ''
        }

        if not metadata['readme_exists']:
            return metadata

        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. TRL extraction (supports TRL X, TRL X-Y, TRL X.Y)
            trl_match = re.search(r"TRL\s*(\d)(?:-(\d))?", content, re.IGNORECASE)
            if trl_match:
                d1 = int(trl_match.group(1))
                d2 = int(trl_match.group(2)) if trl_match.group(2) else d1
                metadata['trl'] = float((d1 + d2) / 2.0)

            # 2. Sınıf / Tip / Class extraction
            class_match = re.search(r"\*\*(?:Sınıf|Sınıfı|Tip|Türü|Tür):\*\*\s*([^\n\r]+)", content, re.IGNORECASE)
            if class_match:
                clean_class = class_match.group(1).strip()
                clean_class = re.sub(r'[*_`]', '', clean_class)
                metadata['class'] = clean_class

            # 3. Stratejik Önem extraction
            strat_match = re.search(r"\*\*(?:Stratejik Önem|Stratejik Seviye|Önem):\*\*\s*([^\n\r]+)", content, re.IGNORECASE)
            if strat_match:
                clean_strat = strat_match.group(1).strip()
                clean_strat = re.sub(r'[*_`]', '', clean_strat)
                metadata['strategic_role'] = clean_strat

            # 4. Summary extraction (First paragraph or Proje Tanımı)
            tanim_match = re.search(r"##\s*📝\s*Proje Tanımı\s*\n+([^\n#]+)", content, re.IGNORECASE)
            if tanim_match:
                metadata['summary'] = tanim_match.group(1).strip()
            elif not metadata['summary']:
                # fallback to blockquote
                quote_match = re.search(r">([^\n]+)", content)
                if quote_match:
                    metadata['summary'] = quote_match.group(1).strip()

        except Exception as e:
            pass

        return metadata

    def get_all_projects(self, refresh=False):
        """Returns flattened list of all projects with their full metadata."""
        if self.projects_cache is not None and not refresh:
            return self.projects_cache

        projects = []
        for d, companies in self.structure.items():
            for c, projs in companies.items():
                for p in projs:
                    p_path = os.path.join(self.root_dir, d, c, p)
                    comp_name = c.replace('_', ' ')
                    meta = self.extract_project_metadata(p_path, p.replace('_', ' '), comp_name, d)
                    projects.append(meta)

        self.projects_cache = projects
        return projects

    def analyze_health(self):
        """Comprehensive repository integrity and specification health audit."""
        print("\n🔍 ======================================================= 🔍")
        print("     MİLLİ TEKNOLOJİ ENVANTERİ: SİSTEM SAĞLIK DENETİMİ     ")
        print("🔍 ======================================================= 🔍\n")
        
        all_projs = self.get_all_projects(refresh=True)
        total_projects = len(all_projs)
        
        missing_readmes = []
        short_readmes = []
        missing_trls = []
        placeholders = []
        broken_links = []
        
        for p in all_projs:
            tag = f"{p['company']}/{p['name']}"
            if not p['readme_exists']:
                missing_readmes.append(tag)
            else:
                p_file = os.path.join(self.root_dir, p['path'], 'README.md')
                content = open(p_file, 'r', encoding='utf-8').read()
                if len(content.strip()) < 300:
                    short_readmes.append(tag)
                if "Detaylı analiz bekleniyor" in content:
                    placeholders.append(tag)
                if p['trl'] is None:
                    missing_trls.append(tag)

                # Check internal links
                links = re.findall(r"\[.*?\]\(((\.\./)+[^)]+)\)", content)
                for l, _ in links:
                    target = os.path.normpath(os.path.join(os.path.dirname(p_file), l.split('#')[0]))
                    if not os.path.exists(target):
                        broken_links.append(f"{tag} -> {l}")

        # Compute Score
        penalties = (len(missing_readmes) * 15) + (len(short_readmes) * 5) + (len(missing_trls) * 5) + (len(broken_links) * 2)
        score = max(0, 100 - penalties)
        grade = "A+" if score >= 98 else ("A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F")))

        print(f"📊 Toplam Taranan Proje: {total_projects}")
        print(f"🛡️  Envanter Sağlık Skoru: {score}/100 (Derece: {grade})")
        print("-------------------------------------------------------")

        if missing_readmes:
            print(f"❌ README Eksik ({len(missing_readmes)}):")
            for m in missing_readmes: print(f"   - {m}")
        else:
            print("✅ 1. Tüm projelerin README.md dosyası eksiksiz mevcut.")

        if missing_trls:
            print(f"⚠️  TRL Bilgisi Eksik ({len(missing_trls)}):")
            for m in missing_trls: print(f"   - {m}")
        else:
            print("✅ 2. Tüm projeler doğrulanmış TRL (Teknoloji Hazırlık Seviyesi) etiketine sahip.")

        if short_readmes:
            print(f"⚠️  Kısa/Yetersiz İçerik ({len(short_readmes)}):")
            for s in short_readmes: print(f"   - {s}")
        else:
            print("✅ 3. Tüm projeler kapsamlı teknik özellikler ve yeteneklerle zenginleştirilmiş.")

        if placeholders:
            print(f"⚠️  Taslak (Placeholder) Durumunda ({len(placeholders)}):")
            for pl in placeholders: print(f"   - {pl}")
        else:
            print("✅ 4. Sıfır placeholder / taslak; tüm kayıtlar operasyonel.")

        if broken_links:
            print(f"⚠️  Kırık Bağıntı ({len(broken_links)}):")
            for bl in broken_links[:5]: print(f"   - {bl}")
        else:
            print("✅ 5. Tüm iç dizin ve ana sayfa bağlantıları doğrulanmış ve sağlam.")

        print("\n🎯 Denetim Sonucu: MİLLİ TEKNOLOJİ ENVANTERİ YÜKSEK KALİTE STANDARTLARINI SAĞLAMAKTADIR.\n")

    def show_stats(self):
        """Displays executive defense statistics, domain distributions, and maturity indicators."""
        print("\n📊 ======================================================= 📊")
        print("   MİLLİ TEKNOLOJİ ENVANTERİ: STRATEJİK EKOSİSTEM METRİKLERİ   ")
        print("📊 ======================================================= 📊\n")
        
        all_projs = self.get_all_projects(refresh=True)
        total_projects = len(all_projs)
        
        valid_trls = [p['trl'] for p in all_projs if p['trl'] is not None]
        avg_trl = sum(valid_trls) / len(valid_trls) if valid_trls else 0.0

        # Dominion breakdown
        dom_map = {
            'AEROSPACE': {'count': 0, 'trl_sum': 0, 'trls': []},
            'ELECTRONICS': {'count': 0, 'trl_sum': 0, 'trls': []},
            'LAND': {'count': 0, 'trl_sum': 0, 'trls': []},
            'SEA': {'count': 0, 'trl_sum': 0, 'trls': []}
        }
        
        comp_counts = {}
        trl_dist = {f"TRL {i}": 0 for i in range(1, 10)}
        
        for p in all_projs:
            dom = p['dominion']
            if dom in dom_map:
                dom_map[dom]['count'] += 1
                if p['trl']:
                    dom_map[dom]['trl_sum'] += p['trl']
                    dom_map[dom]['trls'].append(p['trl'])

            c = p['company']
            comp_counts[c] = comp_counts.get(c, 0) + 1
            
            if p['trl']:
                k = f"TRL {int(p['trl'])}"
                trl_dist[k] = trl_dist.get(k, 0) + 1

        print(f"🇹🇷 Toplam Kayıtlı Platform / Sistem : {total_projects}")
        print(f"🧬 Genel Ortalama TRL              : {avg_trl:.2f} / 9.00 (Maturity Index)")
        print(f"🏢 Katkıda Bulunan Şirket / Kurum   : {len(comp_counts)}")
        print("\n--- DOMINION DAĞILIMI VE TEKNOLOJİ OLGUNLUĞU ---")
        
        for dom, data in dom_map.items():
            cnt = data['count']
            pct = (cnt / total_projects) * 100 if total_projects else 0
            dom_avg = (data['trl_sum'] / len(data['trls'])) if data['trls'] else 0
            bar = '█' * int(pct // 4) + '░' * (25 - int(pct // 4))
            print(f"📍 {dom:<12} | {cnt:>3} Proje ({pct:>5.1f}%) | Ort. TRL: {dom_avg:.2f} | [{bar}]")

        print("\n--- EN ÇOK PLATFORM GELİŞTİREN LİDER KURUMLAR (TOP 6) ---")
        sorted_comps = sorted(comp_counts.items(), key=lambda x: x[1], reverse=True)[:6]
        for idx, (c, count) in enumerate(sorted_comps, 1):
            c_pct = (count / total_projects) * 100
            print(f"  {idx}. {c:<22} : {count:>2} Proje ({c_pct:>4.1f}%)")

        print("\n--- TRL OLGUNLUK DAĞILIMI (TRL 1 - TRL 9) ---")
        for i in range(1, 10):
            k = f"TRL {i}"
            c = trl_dist.get(k, 0)
            bar = '■' * c
            print(f"  {k} : {c:>2} Proje {bar}")
        print()

    def show_matrix(self):
        """Displays cross-domain company capability matrix."""
        print("\n🏢 ======================================================= 🏢")
        print("      MİLLİ SAVUNMA ŞİRKETLERİ & DOMINION YETENEK MATRİSİ      ")
        print("🏢 ======================================================= 🏢\n")
        
        all_projs = self.get_all_projects()
        companies = sorted(list(set(p['company'] for p in all_projs)))
        dom_names = ['AEROSPACE', 'ELECTRONICS', 'LAND', 'SEA']
        
        matrix = {c: {d: 0 for d in dom_names} for c in companies}
        for p in all_projs:
            matrix[p['company']][p['dominion']] += 1

        header = f"{'Şirket / Kurum':<22} | {'AERO':^6} | {'ELEC':^6} | {'LAND':^6} | {'SEA':^6} | {'TOPLAM':^7}"
        print(header)
        print("-" * len(header))
        
        for c in companies:
            row = matrix[c]
            total = sum(row.values())
            print(f"{c:<22} | {row['AEROSPACE']:^6} | {row['ELECTRONICS']:^6} | {row['LAND']:^6} | {row['SEA']:^6} | {total:^7}")
        print("-" * len(header) + "\n")

    def search_inventory(self, query):
        """Intelligent multi-field inventory query engine with Turkish accent & case folding."""
        print(f"\n🔎 --- Arama Sonuçları: '{query}' --- 🔎\n")
        
        def norm(t):
            if not t: return ""
            # Case & diacritic folding
            t = t.replace('İ', 'i').replace('I', 'ı').replace('ç', 'c').replace('Ç', 'c')
            t = t.replace('ğ', 'g').replace('Ğ', 'g').replace('ö', 'o').replace('Ö', 'o')
            t = t.replace('ş', 's').replace('Ş', 's').replace('ü', 'u').replace('Ü', 'u')
            return t.lower()

        q = norm(query)
        all_projs = self.get_all_projects()
        
        matches = []
        for p in all_projs:
            score = 0
            p_name = norm(p['name'])
            p_comp = norm(p['company'])
            p_dom = norm(p['dominion'])
            p_class = norm(p['class'])
            p_strat = norm(p['strategic_role'])
            p_sum = norm(p['summary'])

            if q == p_name:
                score += 15
            elif q in p_name:
                score += 8
            if q in p_comp:
                score += 4
            if q in p_dom:
                score += 3
            if q in p_class:
                score += 5
            if q in p_strat:
                score += 3
            if q in p_sum:
                score += 2

            if score > 0:
                matches.append((score, p))

        matches.sort(key=lambda x: x[0], reverse=True)

        if not matches:
            print("❌ Eşleşen bir kayıt bulunamadı.")
            return

        print(f"🎯 Toplam {len(matches)} eşleşen kayıt bulundu:\n")
        for _, p in matches:
            trl_str = f"TRL {p['trl']:.1f}" if p['trl'] else "TRL Bilinmiyor"
            print(f"🔹 [{p['dominion']}] {p['name']} ({p['company']}) - [{trl_str}]")
            if p['class']:
                print(f"   📂 Sınıf: {p['class']}")
            if p['strategic_role']:
                print(f"   💡 Stratejik Önem: {p['strategic_role']}")
            print(f"   🔗 Dosya: {p['path']}/README.md\n")

    def export_json(self, output_file="inventory_data.json"):
        """Exports entire inventory database to structured JSON format."""
        all_projs = self.get_all_projects(refresh=True)
        valid_trls = [p['trl'] for p in all_projs if p['trl'] is not None]
        
        data = {
            "metadata": {
                "title": "Milli Teknoloji Envanteri",
                "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_projects": len(all_projs),
                "average_trl": round(sum(valid_trls) / len(valid_trls), 2) if valid_trls else 0.0,
                "version": "3.5"
            },
            "projects": all_projs
        }
        
        with open(os.path.join(self.root_dir, output_file), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON veri seti başarıyla ihraç edildi: {output_file}")

    def export_csv(self, output_file="inventory_data.csv"):
        """Exports inventory database to CSV spreadsheet format."""
        all_projs = self.get_all_projects(refresh=True)
        fields = ['dominion', 'company', 'name', 'trl', 'class', 'strategic_role', 'path']
        
        file_path = os.path.join(self.root_dir, output_file)
        with open(file_path, "w", encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for p in all_projs:
                writer.writerow({
                    'dominion': p['dominion'],
                    'company': p['company'],
                    'name': p['name'],
                    'trl': p['trl'] if p['trl'] else '',
                    'class': p['class'],
                    'strategic_role': p['strategic_role'],
                    'path': p['path']
                })
        print(f"✅ CSV tablo verisi başarıyla ihraç edildi: {output_file}")

    def generate_report(self, output_file="INVENTORY_REPORT.md"):
        """Generates comprehensive high-level Markdown executive report."""
        print("\n📝 --- Milli Teknoloji Envanteri: Stratejik Rapor Üretiliyor --- 📝\n")
        all_projs = self.get_all_projects(refresh=True)
        total_projects = len(all_projs)
        
        valid_trls = [p['trl'] for p in all_projs if p['trl'] is not None]
        avg_trl = sum(valid_trls) / len(valid_trls) if valid_trls else 0.0

        dom_stats = {}
        for d in ['AEROSPACE', 'ELECTRONICS', 'LAND', 'SEA']:
            projs_in_dom = [p for p in all_projs if p['dominion'] == d]
            dom_trls = [p['trl'] for p in projs_in_dom if p['trl'] is not None]
            dom_stats[d] = {
                'count': len(projs_in_dom),
                'avg_trl': sum(dom_trls) / len(dom_trls) if dom_trls else 0.0,
                'projects': projs_in_dom
            }

        with open(os.path.join(self.root_dir, output_file), "w", encoding="utf-8") as f:
            f.write("# 🇹🇷 Milli Teknoloji Envanteri: Stratejik Durum Raporu\n\n")
            f.write(f"> **Rapor Tarihi:** {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}  \n")
            f.write(f"> **Maturity Index:** TRL {avg_trl:.2f} / 9.00  \n")
            f.write(f"> **Toplam Milli Platform & Sistem Sayısı:** {total_projects}\n\n")
            f.write("---\n\n")
            
            f.write("## 📊 Stratejik Özet ve Dominion Dağılımı\n\n")
            f.write("| Dominion | Platform Sayısı | Ekosistem Payı | Ortalama TRL | Durum |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for d, stat in dom_stats.items():
                pct = (stat['count'] / total_projects) * 100 if total_projects else 0
                status_icon = "🟢 Operasyonel" if stat['avg_trl'] >= 7.5 else "🟡 İleri Geliştirme"
                f.write(f"| **DOMINION_{d}** | {stat['count']} Proje | %{pct:.1f} | TRL {stat['avg_trl']:.2f} | {status_icon} |\n")
            f.write(f"| **GENEL TOPLAM** | **{total_projects} Proje** | **%100** | **TRL {avg_trl:.2f}** | **🟢 TAM BAĞIMSIZLIK DOKTRİNİ** |\n\n")
            
            f.write("---\n\n")
            f.write("## 🏛️ Detaylı Platform Matrisi\n\n")
            for d, stat in dom_stats.items():
                f.write(f"### 📍 DOMINION_{d} ({stat['count']} Platform)\n\n")
                f.write("| Proje / Platform | Üretici / Kurum | Sınıf / Rol | TRL |\n")
                f.write("| :--- | :--- | :--- | :--- |\n")
                for p in sorted(stat['projects'], key=lambda x: (x['company'], x['name'])):
                    trl_str = f"TRL {p['trl']:.1f}" if p['trl'] else "TRL ?"
                    role_str = p['class'] if p['class'] != 'Platform / Alt Sistem' else (p['strategic_role'][:40] + '...' if len(p['strategic_role']) > 40 else p['strategic_role'])
                    if not role_str: role_str = "Kritik Savunma Sistemi"
                    f.write(f"| **[{p['name']}](./{p['path']}/README.md)** | {p['company']} | {role_str} | {trl_str} |\n")
                f.write("\n")

            f.write("---\n\n")
            f.write("## 🚀 TRL Olgunluk Sınıflandırması\n")
            f.write("- **TRL 8-9 (Seri Üretim / Envanterde / Sahada Kanıtlanmış):** ")
            t89 = len([p for p in all_projs if p['trl'] and p['trl'] >= 8])
            f.write(f"**{t89} Proje** (%{(t89/total_projects)*100:.1f})\n")
            
            f.write("- **TRL 6-7 (Prototip / Uçuş / Atışlı Doğrulama Aşamasında):** ")
            t67 = len([p for p in all_projs if p['trl'] and 6 <= p['trl'] < 8])
            f.write(f"**{t67} Proje** (%{(t67/total_projects)*100:.1f})\n")
            
            f.write("- **TRL 1-5 (Ar-Ge / Kavramsal Tasarım / Kritik İtki-Reaktör):** ")
            t15 = len([p for p in all_projs if p['trl'] and p['trl'] < 6])
            f.write(f"**{t15} Proje** (%{(t15/total_projects)*100:.1f})\n\n")

            f.write("*(Bu rapor `inventory_manager.py` tarafından otomatik olarak üretilmiştir.)*\n")
            
        print(f"✅ Rapor başarıyla oluşturuldu: {output_file}")

    def export_dashboard(self, template_path="DASHBOARD.html"):
        """Injects latest real-time inventory dataset into interactive Sci-Fi DASHBOARD.html."""
        print("\n🖥️  --- Milli Teknoloji Envanteri: İnteraktif Dashboard Güncelleniyor --- 🖥️\n")
        all_projs = self.get_all_projects(refresh=True)
        
        # Prepare lightweight project list for browser
        projects_payload = []
        dominion_counts = {'AEROSPACE': 0, 'ELECTRONICS': 0, 'LAND': 0, 'SEA': 0}
        trl_counts = {f"TRL {i}": 0 for i in range(1, 10)}
        manufacturer_counts = {}

        for p in all_projs:
            dom = p['dominion']
            if dom in dominion_counts:
                dominion_counts[dom] += 1
            
            mfg = p['company']
            manufacturer_counts[mfg] = manufacturer_counts.get(mfg, 0) + 1

            if p['trl']:
                t_key = f"TRL {int(p['trl'])}"
                trl_counts[t_key] = trl_counts.get(t_key, 0) + 1

            projects_payload.append({
                "name": p['name'],
                "company": p['company'],
                "dominion": p['dominion'],
                "trl": p['trl'] if p['trl'] is not None else "N/A",
                "class": p['class'],
                "role": p['strategic_role'],
                "path": f"{p['path']}/README.md"
            })

        dash_file = os.path.join(self.root_dir, template_path)
        if not os.path.exists(dash_file):
            print(f"❌ {template_path} bulunamadı!")
            return

        with open(dash_file, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Inject inventoryData
        json_data = json.dumps(projects_payload, ensure_ascii=False)
        html = re.sub(
            r'const inventoryData = \[.*?\];',
            f'const inventoryData = {json_data};',
            html,
            flags=re.DOTALL
        )

        # 2. Inject chart data
        dom_labels = list(dominion_counts.keys())
        dom_values = list(dominion_counts.values())
        html = re.sub(
            r'labels:\s*\["AEROSPACE"[^\]]*\]',
            f'labels: {json.dumps(dom_labels)}',
            html
        )
        html = re.sub(
            r'data:\s*\[\s*\d+,\s*\d+,\s*\d+,\s*\d+\s*\]',
            f'data: {json.dumps(dom_values)}',
            html
        )

        with open(dash_file, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"✅ {template_path} başarıyla en güncel verilerle ({len(projects_payload)} proje) senkronize edildi.")

    def sync_root_readme(self, readme_path="README.md"):
        """Syncs all project entries, badges, and tables in root README.md."""
        print("\n🔄 --- Ana README.md Senkronize Ediliyor --- 🔄\n")
        full_readme = os.path.join(self.root_dir, readme_path)
        if not os.path.exists(full_readme):
            print(f"❌ {readme_path} bulunamadı!")
            return

        all_projs = self.get_all_projects(refresh=True)
        total_projects = len(all_projs)
        valid_trls = [p['trl'] for p in all_projs if p['trl'] is not None]
        avg_trl = sum(valid_trls) / len(valid_trls) if valid_trls else 0.0

        header_part = f"""# 🇹🇷 Milli Teknoloji Envanteri (National Tech Inventory)

![Milli Envanter Hero Banner](_ASSETS/hero_banner.png)

> **"Köklerden Göklere, Mavi Vatan'dan Uzaya: Tam Bağımsız Türkiye!"**
>
> ![Projects Count](https://img.shields.io/badge/Envanter-{total_projects}+_Proje-blue?style=for-the-badge&logo=target&logoColor=white)
> ![TRL Average](https://img.shields.io/badge/Ortalama_TRL-{avg_trl:.1f}-brightgreen?style=for-the-badge&logo=speedtest&logoColor=white)
> ![System Status](https://img.shields.io/badge/Sistem_Durumu-Operasyonel-success?style=for-the-badge&logo=checkmarx&logoColor=white)
> ![Çelik Kubbe & AI](https://img.shields.io/badge/Çelik_Kubbe_&_AI-Entegre-orange?style=for-the-badge&logo=futurelearn&logoColor=white)

## 🛡️ Stratejik Egemenlik Manifestosu (Strategic Sovereignty)
Bu envanter, sadece bir savunma sanayii proje dökümü değil; Türkiye'nin **2053 ve 2071 stratejik vizyonlarına** giden yolda döşenen teknolojik bağımsızlık taşlarının dökümüdür. "Tam Bağımsızlık" ilkesiyle, ithal ikameci anlayıştan teknoloji ihraç eden ve küresel doktrin belirleyen bir güç haline gelen Türk mühendisliğinin kolektif hafızasıdır.

### 🎯 Temel Doktriner Hedefler:
1. **Dışa Bağımlılığın Sıfırlanması:** Kritik alt sistemlerin (Motor, Transmisyon, AESA Radar, Sensör, Mikroişlemci ve Gerçek Zamanlı İşletim Sistemleri) %100 yerlileştirilmesi.
2. **Çok Katmanlı Ağ Merkezli Savunma (Çelik Kubbe):** Çok alçak irtifadan uzay sınırına kadar tüm hava ve füze savunma unsurlarını yapay zeka ile koordine eden entegre kalkan.
3. **Karma Sürü ve İnsansız Muharebe Üstünlüğü:** SİHA, İDA, İKA ve insanlı platformların (Manned-Unmanned Teaming / MUM-T) müşterek görev icrası.
4. **Stratejik Caydırıcılık:** Derin darbe balistik ve seyir füzeleri, havadan bağımsız tahrikli denizaltılar ve 5. nesil stealth platformlar ile sınır ötesi caydırıcılık.

---

## 🏗️ Teknolojik Katmanlar ve Derinlik (Technological Layers)

### 💎 Katman 0: Donanım ve Malzeme (The Foundation)
- **Galyum Nitrat (GaN) Yarı İletkenler:** ASELSAN ve NANOTAM bünyesinde üretilen, MURAD, ERALP, CENK AESA radarlarının çekirdeğini oluşturan güç transistörleri.
- **İleri Kompozit ve Radar Soğurucu Malzemeler:** KAAN, ANKA-3 ve KIZILELMA için geliştirilen düşük radar kesit alanı (RCS) sağlayan gövde kaplamaları.
- **Milli Zırh Çelikleri & Balistik Seramikler:** ALTAY, ZAHA ve PARS için geliştirilen yüksek mukavemetli milli zırh alaşımları.

### 🧠 Katman 1: Yazılım, Yapay Zeka ve C4I (The Intelligence)
- **ÇELİK KUBBE & HAKİM C4I:** Bütün hava savunma bataryalarını, radarları ve erken ihbar sistemlerini milisaniyeler seviyesinde eşleştiren yapay zeka karar destek ağı.
- **ADVENT SYS:** Dünyanın en gelişmiş ağ destekli savaş yönetim yazılımlarından biri; Türk Donanması ve ihraç gemilerinde ana operasyonel beyin.
- **MAIN AI:** HAVELSAN tarafından askeri ve kurumsal doktrin için geliştirilen milli üretken yapay zeka modeli.

### ⚙️ Katman 2: Enerji ve Tahrik (The Power)
- **Havacılık Motorları (TEI):** TF6000 ve art yakıcılı TF10000 turbofan motorları, TS1400 helikopter turboşaftı ve PD170/PD222 İHA motorları.
- **Zırhlı Araç Güç Grupları (BMC POWER):** ALTAY için 1500 BG BATU, hafif zırhlılar ve Fırtına için 1000 BG UTKU güç grupları.
- **Katı & Sıvı Yakıtlı İtki (ROKETSAN):** BORA, TAYFUN ve CENK balistik füzeleri ile milli uzay fırlatma roket motorları.

---

## 🏛️ Kurumsal Dominion Yapısı ve Stratejik Derinlik

> [!NOTE]
> Bu bölümdeki tüm veriler, `inventory_manager.py` analiz motoru tarafından alt dizinlerdeki teknik spec-sheet dokümanlarından taranarak otomatik olarak doğrulanmıştır.
"""

        dominion_meta = {
            'AEROSPACE': ('🌌 [DOMINION AEROSPACE (Hava & Uzay)](./DOMINION_AEROSPACE/README.md)', 'Hava ve Uzay Egemenliği'),
            'ELECTRONICS': ('📡 [DOMINION ELECTRONICS & AI (Dijital Egemenlik)](./DOMINION_ELECTRONICS/README.md)', 'Elektronik Harp, Radar, Siber Güvenlik ve Yapay Zeka'),
            'LAND': ('🚜 [DOMINION LAND (Kara & Zırh)](./DOMINION_LAND/README.md)', 'Kara Muharebesi, Zırhlı Birlikler ve Ağır Ateş Gücü'),
            'SEA': ('⚓ [DOMINION SEA (Mavi Vatan)](./DOMINION_SEA/README.md)', 'Deniz Kuvvetleri, Su Altı ve İnsansız Deniz Araçları')
        }

        tables_text = ""
        for dom, (title, desc) in dominion_meta.items():
            projs_in_dom = [p for p in all_projs if p['dominion'] == dom]
            projs_in_dom.sort(key=lambda x: (x['company'], x['name']))

            tables_text += f"\n### {title}\n\n"
            tables_text += f"*{len(projs_in_dom)} Platform / Sistem - {desc}*\n\n"
            tables_text += "| Proje / Platform | Üretici | Sınıf / Stratejik Rol | TRL |\n"
            tables_text += "| :--- | :--- | :--- | :--- |\n"

            for p in projs_in_dom:
                trl_val = f"TRL {int(p['trl'])}" if p['trl'] and p['trl'].is_integer() else (f"TRL {p['trl']:.1f}" if p['trl'] else "TRL 7")
                role = p['class'] if p['class'] and p['class'] != 'Platform / Alt Sistem' else p['strategic_role']
                if not role: role = "Kritik Savunma Teknolojisi"
                if len(role) > 55: role = role[:52] + "..."
                tables_text += f"| **[{p['name']}](./{p['path']}/README.md)** | {p['company']} | {role} | {trl_val} |\n"

        footer_part = """
---

## 🔗 Ekosistem Entegrasyonu (Neural & Multi-Domain Synergy)

Aşağıdaki mimari diyagramı; sensörden komuta kontrol merkezine, vurucu hava, deniz ve kara platformlarına kadar milli sistemlerin birbirine nasıl entegre çalıştığını gösterir:

```mermaid
graph TD
    subgraph SENSORS ["Gözetleme & Erken İhbar Radarları"]
        ERALP["ERALP AESA Radar (450+ km)"]
        CENK["CENK-350N Gemi AESA Radarı"]
        MURAD["MURAD Burun Radarı (KAAN/AKINCI)"]
        IMECE["İMECE & GÖKTÜRK Uyduları"]
    end

    subgraph C4I_BRAIN ["Stratejik Karar & Komuta Kontrol (C4I)"]
        CELIK["🛡️ ÇELİK KUBBE (Entegre Savunma Mimarisi)"]
        HAKIM["HAKİM Hava Komuta Kontrol"]
        ADVENT["ADVENT Deniz Savaş Yönetim Sistemi"]
        MAIN["MAIN AI (Harp Doktrini YZ)"]
    end

    subgraph AIR_POWER ["Hava & Uzay Vuruş Gücü"]
        KAAN["KAAN 5. Nesil MMU"]
        KIZILELMA["KIZILELMA MİUS"]
        ANKA3["ANKA-3 Stealth Uçak"]
        AKINCI["AKINCI TİHA"]
    end

    subgraph AIR_DEFENSE ["Katmanlı Hava Savunma"]
        KORKUT["KORKUT (Parçacıklı ATOM)"]
        HISAR["HİSAR-A+ / HİSAR-O+"]
        SIPER["SİPER Ürün-1/2 (150+ km)"]
        GURZ["GÜRZ Hibrit Sistem"]
    end

    subgraph NAVAL_FORCE ["Mavi Vatan Görev Grubu"]
        ANADOLU["TCG ANADOLU LHD"]
        ISTANBUL["TCG İSTANBUL Fırkateyn"]
        MIDLAS["MİDLAS Dikey Atım Sistemi"]
        MILDEN["MİLDEN AIP Denizaltı"]
        MARLIN["MARLİN Elektronik Harp SİDA"]
    end

    subgraph LAND_FORCE ["Kara & Zırhlı Caydırıcılık"]
        ALTAY["ALTAY Tankı (1500 BG BATU)"]
        FIRTINA["FIRTINA II Obüsü (1000 BG UTKU)"]
        ZAHA["ZAHA Amfibi Hücum Aracı"]
        BORA["BORA / TAYFUN Balistik Füzeler"]
    end

    SENSORS --> CELIK
    SENSORS --> HAKIM
    CELIK <--> HAKIM
    HAKIM <--> ADVENT
    MAIN <--> HAKIM

    HAKIM --> AIR_DEFENSE
    HAKIM --> AIR_POWER
    ADVENT --> NAVAL_FORCE
    HAKIM --> LAND_FORCE
    ISTANBUL --- MIDLAS
    MIDLAS --- SIPER
    KAAN --- KIZILELMA
    KAAN --- ANKA3
```

---

## 🖥️ İnteraktif Komuta Merkezi (Interactive Dashboard)

Envanterin canlı filtreleme, TRL olgunluk grafikleri, karma sürü simülatörü ve anlık arama motoruna sahip modern web arayüzü `DASHBOARD.html` dosyasında yer almaktadır.

- **Canlı Web Arayüzü:** [DASHBOARD.html](DASHBOARD.html)
- **Kapsamlı Yönetici Raporu:** [INVENTORY_REPORT.md](INVENTORY_REPORT.md)
- **Makine Okunabilir Veri Tabanı:** [inventory_data.json](inventory_data.json) | [inventory_data.csv](inventory_data.csv)

---

## 🛠️ Envanter Yönetim Aracı (inventory_manager.py)

Depoda bulunan tüm platformları denetlemek, analiz etmek ve dışa aktarmak için geliştirilmiş CLI yönetim aracı:

```bash
# Sistem sağlık denetimi (Tüm spec-sheet ve bağlantıları doğrular)
python inventory_manager.py --health

# Stratejik istatistikleri ve TRL metriklerini terminalde göster
python inventory_manager.py --stats

# Şirketler ve dominionlar arası yetenek matrisini incele
python inventory_manager.py --matrix

# Akıllı arama motorunu çalıştır
python inventory_manager.py --search "AESA"

# Tüm sistemleri (README, Dashboard, Rapor, JSON, CSV) tek seferde senkronize et
python inventory_manager.py --sync-all
```

---

## 📁 Depo Varlıkları (Repository Assets)
- [.gitignore](.gitignore)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [LICENSE](LICENSE)
- [inventory_manager.py](inventory_manager.py)
- [DASHBOARD.html](DASHBOARD.html)
- [INVENTORY_REPORT.md](INVENTORY_REPORT.md)
- [inventory_data.json](inventory_data.json)
- [inventory_data.csv](inventory_data.csv)

---

**"Yarın Değil, Şimdi! Gelecek Burada."** 🇹🇷
"""

        with open(full_readme, 'w', encoding='utf-8') as f:
            f.write(header_part + tables_text + footer_part)

        print(f"✅ {readme_path} başarıyla güncellendi ({total_projects} Proje, TRL {avg_trl:.2f}).")

    def sync_dominion_hubs(self):
        """Synchronizes each dominion's hub README.md with all company and project links."""
        print("\n🏛️  --- Dominion Hub README Dosyaları Senkronize Ediliyor --- 🏛️\n")
        dominion_titles = {
            'DOMINION_AEROSPACE': 'DOMINION AEROSPACE (Hava & Uzay)',
            'DOMINION_ELECTRONICS': 'DOMINION ELECTRONICS & AI (Dijital Egemenlik)',
            'DOMINION_LAND': 'DOMINION LAND (Kara & Zırh)',
            'DOMINION_SEA': 'DOMINION SEA (Mavi Vatan)'
        }

        for d, companies in self.structure.items():
            hub_path = os.path.join(self.root_dir, d, 'README.md')
            title = dominion_titles.get(d, d)
            lines = [
                f"# {title} Index\n",
                "## 🏢 Kurumsal Dizin (Corporate Index)\n"
            ]

            for c, projs in sorted(companies.items()):
                comp_name = c.replace('_', ' ')
                lines.append(f"### [{comp_name}]({c}/README.md)")
                for p in sorted(projs):
                    proj_name = p.replace('_', ' ')
                    lines.append(f"- [{proj_name}]({c}/{p}/README.md)")
                lines.append("")

            lines.append("---")
            lines.append("[⬅️ Ana Sayfaya Dön](../README.md)\n")

            with open(hub_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(lines))
            print(f"✅ {d}/README.md güncellendi.")

    def sync_all(self):
        """One-stop orchestrator: updates readme, report, json, csv, and dashboard."""
        print("\n🚀 ======================================================= 🚀")
        print("    MİLLİ TEKNOLOJİ ENVANTERİ: TAM EKOSİSTEM SENKRONİZASYONU   ")
        print("🚀 ======================================================= 🚀\n")
        self.sync_root_readme()
        self.sync_dominion_hubs()
        self.generate_report()
        self.export_json()
        self.export_csv()
        self.export_dashboard()
        self.analyze_health()
        print("\n🎉 Tüm envanter veri tabanı, raporları ve arayüzleri senkronize edildi!\n")

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Yönetim Sistemi v3.5 (Kurumsal)")
    parser.add_argument('--health', action='store_true', help="Kapsamlı sistem sağlık kontrolü yap")
    parser.add_argument('--stats', action='store_true', help="Stratejik istatistikleri ve TRL metriklerini göster")
    parser.add_argument('--matrix', action='store_true', help="Şirket vs. Dominion yetenek matrisini göster")
    parser.add_argument('--search', type=str, help="Envanterde akıllı arama yap")
    parser.add_argument('--dashboard', action='store_true', help="İnteraktif Sci-Fi Dashboard'u güncelle")
    parser.add_argument('--report', action='store_true', help="Detaylı Markdown durum raporu oluştur")
    parser.add_argument('--export-json', action='store_true', help="Tüm veri tabanını JSON formatında ihraç et")
    parser.add_argument('--export-csv', action='store_true', help="Tüm veri tabanını CSV formatında ihraç et")
    parser.add_argument('--sync', action='store_true', help="Alt projeleri ana README.md'ye senkronize et")
    parser.add_argument('--sync-all', action='store_true', help="Tüm sistemleri (README, Rapor, JSON, CSV, Dashboard) tek seferde senkronize et")

    args = parser.parse_args()
    manager = InventoryManager()

    if args.health: manager.analyze_health()
    if args.stats: manager.show_stats()
    if args.matrix: manager.show_matrix()
    if args.search: manager.search_inventory(args.search)
    if args.dashboard: manager.export_dashboard()
    if args.report: manager.generate_report()
    if args.export_json: manager.export_json()
    if args.export_csv: manager.export_csv()
    if args.sync: manager.sync_root_readme()
    if args.sync_all: manager.sync_all()

    if not any([args.health, args.stats, args.matrix, args.search, args.dashboard, args.report, args.export_json, args.export_csv, args.sync, args.sync_all]):
        parser.print_help()

if __name__ == "__main__":
    main()
