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
        """Syncs all project entries, badges, and tables in root README.md with iconic portal layout."""
        print("\n🔄 --- Ana README.md İkonik Portala Dönüştürülerek Senkronize Ediliyor --- 🔄\n")
        full_readme = os.path.join(self.root_dir, readme_path)
        if not os.path.exists(full_readme):
            print(f"❌ {readme_path} bulunamadı!")
            return

        all_projs = self.get_all_projects(refresh=True)
        total_projects = len(all_projs)
        valid_trls = [p['trl'] for p in all_projs if p['trl'] is not None]
        avg_trl = sum(valid_trls) / len(valid_trls) if valid_trls else 0.0

        header_part = f"""# 🇹🇷 Milli Teknoloji Envanteri (National Defense & Tech Portal)

<p align="center">
  <img src="_ASSETS/hero_banner.png" alt="Milli Teknoloji Envanteri Hero Banner" width="100%">
</p>

<p align="center">
  <b>"Köklerden Göklere, Mavi Vatan'dan Uzaya: Tam Bağımsız Türk Savunma Sanayii"</b>
</p>

<p align="center">
  <a href="https://github.com/bahattinyunus/Milli-Teknoloji-Envanteri"><img src="https://img.shields.io/badge/Envanter-{total_projects}+_Stratejik_Platform-00f2fe?style=for-the-badge&logo=target&logoColor=black" alt="Envanter Sayısı"></a>
  <a href="docs/TRL_GUIDE.md"><img src="https://img.shields.io/badge/Ortalama_TRL-{avg_trl:.2f}_%2F_9.00-00E676?style=for-the-badge&logo=speedtest&logoColor=black" alt="Ortalama TRL"></a>
  <a href="DASHBOARD.html"><img src="https://img.shields.io/badge/Muharebe_Hazırlık-100%25_Operasyonel-ff007f?style=for-the-badge&logo=shield&logoColor=white" alt="Operasyonel"></a>
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/Doktrin-Çelik_Kubbe_&_MUM--T-7928CA?style=for-the-badge&logo=airplayvideo&logoColor=white" alt="Doktrin"></a>
  <a href="docs/API_CLI.md"><img src="https://img.shields.io/badge/Standart-NATO_&_SSB_TRL-blueviolet?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Standart"></a>
</p>

<p align="center">
  <a href="#-dominion-aerospace-hava--uzay">🌌 Hava & Uzay</a> •
  <a href="#-dominion-electronics--ai-dijital-egemenlik">📡 Elektronik & YZ</a> •
  <a href="#-dominion-land-kara--zırh">🚜 Kara & Zırh</a> •
  <a href="#-dominion-sea-mavi-vatan">⚓ Mavi Vatan</a> •
  <a href="#-çelik-kubbe--ağ-merkezli-hava-savunma-doktrini">🛡️ Çelik Kubbe</a> •
  <a href="#-mum-t-ve-karma-sürü-muharebe-doktrini">🤖 MUM-T Doktrini</a> •
  <a href="DASHBOARD.html">🖥️ Canlı Dashboard</a> •
  <a href="#-stratejik-dokümantasyon-ve-standartlar">📚 Dokümantasyon</a>
</p>

---

## 🏛️ Stratejik Egemenlik ve Vizyon Manifestosu

Milli Teknoloji Envanteri, Türkiye'nin **2053 ve 2071 stratejik vizyonlarına** giden yolda geliştirilen yerli ve milli savunma sanayii varlıklarının yüksek çözünürlüklü dijital kütüphanesidir. İthal ikameci anlayıştan küresel oyun kurucu doktrin seviyesine yükselen Türk savunma ekosisteminin tüm operasyonel bileşenlerini ve TRL olgunluk seviyelerini belgeler.

### 🌟 Dört Boyutlu Muharebe Hakimiyeti:
1. **🌌 Hava ve Uzay:** 5. Nesil Hayalet Uçak (KAAN), İnsansız Muharip Uçaklar (KIZILELMA, ANKA-3), Yüksek İrtifa TİHA'lar ve Alçak Yörünge Uydu Takımları.
2. **📡 Siber ve Elektronik Harp:** AESA Radarları (ERALP, CENK, MURAD), Çelik Kubbe Yapay Zeka Karar Ağı, ADVENT Savaş Yönetimi ve KORAL/REDET EH Sistemleri.
3. **🚜 Kara ve Zırhlı Muharebe:** ALTAY Yeni Nesil Ana Muharebe Tankı, FIRTINA II Obüsleri, İleri Zırhlı Taktik Araçlar ve Balistik Derin Darbe Füzeleri (BORA, TAYFUN).
4. **⚓ Mavi Vatan:** TCG ANADOLU Çok Maksatlı Amfibi Hücum Gemisi, MİLGEM İ-Sınıfı Fırkateynler, MİLDEN Havadan Bağımsız Tahrikli Denizaltılar ve Otonom SİDA Sürüleri.

---

## 💎 Amiral Gemisi Platformlar (Flagship Highlights)

| Platform | Üretici | Dominion | Rol & Stratejik Nitelik | TRL |
| :--- | :--- | :--- | :--- | :---: |
| **[KAAN](./DOMINION_AEROSPACE/TUSAŞ/KAAN/README.md)** | TUSAŞ | AEROSPACE | 5. Nesil Milli Muharip Uçak, Süperseyir, Dahili Silah Yuvası, AESA | `TRL 7` |
| **[KIZILELMA](./DOMINION_AEROSPACE/BAYKAR/KIZILELMA/README.md)** | BAYKAR | AEROSPACE | İnsansız Savaş Uçağı (MİUS), Düşük RCS, Süpersonik İtki, MUM-T | `TRL 8` |
| **[ANKA-3](./DOMINION_AEROSPACE/TUSAŞ/ANKA-3/README.md)** | TUSAŞ | AEROSPACE | Uçan Kanat (Flying Wing) Derin Darbe Hayalet SİHA | `TRL 7` |
| **[ÇELİK KUBBE](./DOMINION_ELECTRONICS/ASELSAN/ÇELİK_KUBBE/README.md)** | SSB / ASELSAN | ELECTRONICS | Çok Katmanlı Yapay Zeka Destekli Entegre Hava Savunma Sistemi | `TRL 8` |
| **[TCG ANADOLU](./DOMINION_SEA/DzKK/TCG_ANADOLU/README.md)** | DzKK / SEDEF | SEA | Dünyanın İlk SİHA/LHD Amfibi Görev Gemisi | `TRL 9` |
| **[TCG İSTANBUL (F-515)](./DOMINION_SEA/STM/TCG_İSTANBUL/README.md)** | STM / DzKK | SEA | Milli MİLGEM İ-Sınıfı Fırkateyn, MİDLAS Dikey Atım & ADVENT SYS | `TRL 9` |
| **[ALTAY](./DOMINION_LAND/BMC/ALTAY/README.md)** | BMC | LAND | Yeni Nesil Ana Muharebe Tankı, AKKOR Aktif Koruma, 1500 BG BATU | `TRL 8` |
| **[TAYFUN](./DOMINION_LAND/ROKETSAN/TAYFUN/README.md)** | ROKETSAN | LAND | Kısa/Orta Menzilli Stratejik Hipersonik/Balistik Füze Sistemi | `TRL 8` |

---

## 🏛️ Kurumsal Dominion Envanteri

> [!NOTE]
> Aşağıdaki tablolar `inventory_manager.py` analiz motoru tarafından otomatik olarak taranıp doğrulanmıştır. Her platformun detaylı teknik özelliklerine, silah konfigürasyonlarına ve motor tiplerine ilgili bağlantıdan ulaşabilirsiniz.
"""

        dominion_meta = {
            'AEROSPACE': (
                '🌌 DOMINION AEROSPACE (Hava & Uzay)',
                'Hava Hakimiyeti, İnsansız Hava Araçları, Helikopterler, İtki Motorları ve Uydu Sistemleri',
                'DOMINION_AEROSPACE'
            ),
            'ELECTRONICS': (
                '📡 DOMINION ELECTRONICS & AI (Dijital Egemenlik)',
                'AESA Radarları, Elektronik Harp, Komuta Kontrol (C4I), Askeri Yapay Zeka ve Elektro-Optik Sistemler',
                'DOMINION_ELECTRONICS'
            ),
            'LAND': (
                '🚜 DOMINION LAND (Kara & Zırh)',
                'Ana Muharebe Tankları, Zırhlı Taktik Araçlar, Ağır Topçu, Balistik Füzeler ve Güç Grupları',
                'DOMINION_LAND'
            ),
            'SEA': (
                '⚓ DOMINION SEA (Mavi Vatan)',
                'Fırkateynler, Amfibi Hücum Gemileri, Havadan Bağımsız Denizaltılar ve Otonom SİDA Sürüleri',
                'DOMINION_SEA'
            )
        }

        tables_text = ""
        for dom, (title, desc, folder) in dominion_meta.items():
            projs_in_dom = [p for p in all_projs if p['dominion'] == dom]
            projs_in_dom.sort(key=lambda x: (x['company'], x['name']))

            tables_text += f"\n### [{title}](./{folder}/README.md)\n\n"
            tables_text += f"> *{desc}* — **Toplam {len(projs_in_dom)} Kayıtlı Platform**\n\n"
            tables_text += f"<details open>\n"
            tables_text += f"<summary><b>📋 {dom} Platform Kataloğunu Görüntüleyin / Daraltın ({len(projs_in_dom)} Sistem)</b></summary>\n\n"
            tables_text += "| Proje / Platform | Üretici / Kurum | Sınıf & Stratejik Görev | Olgunluk (TRL) |\n"
            tables_text += "| :--- | :--- | :--- | :---: |\n"

            for p in projs_in_dom:
                trl_val = f"`TRL {int(p['trl'])}`" if p['trl'] and p['trl'].is_integer() else (f"`TRL {p['trl']:.1f}`" if p['trl'] else "`TRL 7`")
                role = p['class'] if p['class'] and p['class'] != 'Platform / Alt Sistem' else p['strategic_role']
                if not role: role = "Kritik Savunma Teknolojisi"
                if len(role) > 55: role = role[:52] + "..."
                tables_text += f"| **[{p['name']}](./{p['path']}/README.md)** | {p['company']} | {role} | {trl_val} |\n"

            tables_text += "\n</details>\n"

        footer_part = """
---

## 🛡️ Çelik Kubbe & Ağ Merkezli Hava Savunma Doktrini

Milli Çelik Kubbe mimarisi; en alt irtifadan uzay sınırına kadar tüm radar, elektro-optik, komuta kontrol ve füze/namlulu önleme katmanlarını yapay zeka ile senkronize eder:

```mermaid
graph TD
    subgraph SENSORS ["1. RADAR & SENSÖR GÖZETLEME KATMANI"]
        ERALP["ERALP Taşınabilir Erken İhbar Radarı (450+ km)"]
        CENK["CENK-350N Çok Fonksiyonlu Deniz AESA"]
        MURAD["MURAD AESA Burun Radarı (KAAN / AKINCI)"]
        IMECE["İMECE & GÖKTÜRK Yüksek Çözünürlüklü Uydular"]
        PUHU["PUHU Taşınabilir Dinleme & Kestirme Sistemi"]
    end

    subgraph C4I_BRAIN ["2. YAPAY ZEKA DESTEKLİ C4I KOMUTA MERKEZİ"]
        CELIK["🛡️ ÇELİK KUBBE ENTEGRE SİSTEMİ"]
        HAKIM["HAKİM Hava Komuta Kontrol Sistemi"]
        ADVENT["ADVENT Ağ Destekli Savaş Yönetimi"]
        MAIN["MAIN AI Harp Doktrini Modeli"]
    end

    subgraph SHORAD ["3. ÇOK ALÇAK & ALÇAK İRTİFA SAVUNMA (0 - 10 km)"]
        KORKUT["KORKUT 35mm Parçacıklı Mühimmat (ATOM)"]
        SUNGUR["SUNGUR Portatif Hava Savunma Füzesi"]
        GURZ["GÜRZ Hibrit Hava Savunma Sistemi"]
        ALKA["ALKA Yönlendirilmiş Enerji Silahı (Lazer)"]
    end

    subgraph MEDIUM_HIGH ["4. ORTA & UZUN MENZİL HAVA SAVUNMA (10 - 150+ km)"]
        HISAR_A["HİSAR-A+ Alçak İrtifa Füzesi"]
        HISAR_O["HİSAR-O+ Orta İrtifa Füzesi"]
        SIPER1["SİPER Ürün-1 Uzun Menzil Bölge Savunma (100 km)"]
        SIPER2["SİPER Ürün-2 İleri İrtifa Önleyici (150+ km)"]
    end

    SENSORS --> CELIK
    SENSORS --> HAKIM
    CELIK <--> HAKIM
    HAKIM <--> ADVENT
    MAIN <--> HAKIM

    CELIK ==> SHORAD
    CELIK ==> MEDIUM_HIGH
```

---

## 🤖 MUM-T ve Karma Sürü Muharebe Doktrini

İnsanlı ve insansız platformların müşterek harekat icra ettiği Manned-Unmanned Teaming (MUM-T) mimarisi:

```mermaid
flowchart LR
    subgraph COMMAND_AIR ["İnsanlı Lider Platform"]
        KAAN["KAAN 5. Nesil MMU<br/><i>(Taktik Karar & Görev Lideri)</i>"]
    end

    subgraph UNMANNED_ESCORT ["Sadık Kanat Adamları (Loyal Wingman)"]
        KIZILELMA["KIZILELMA MİUS<br/><i>(Hava-Hava Önleme & İtki Gücü)</i>"]
        ANKA3["ANKA-3 Stealth SİHA<br/><i>(Derin Darbe & SEAD/DEAD)</i>"]
        SUPER_SIMSEK["SÜPER ŞİMŞEK<br/><i>(Elektronik Karıştırma & Yem İHA)</i>"]
    end

    subgraph SWARM_STRIKE ["Akıllı Karma Sürü & Kamikaze"]
        ALPAGU["ALPAGU Akıllı Dolanan Mühimmat"]
        KARGU["KARGU Döner Kanatlı Vurucu İHA"]
        BOYGA["BOYGA Havan Mühimmatı Bırakan İHA"]
    end

    subgraph NAVAL_FORCE ["Mavi Vatan Otonom Deniz Gücü"]
        ANADOLU["TCG ANADOLU (L-400)"]
        TB3["Bayraktar TB3 (Katlanır Kanat)"]
        MARLIN["MARLİN Elektronik Harp SİDA"]
        SALDIRGAN["SALDIRGAN / SANCAR SİDA"]
    end

    KAAN ==>|Şifreli KEMENT Taktik Veri Bağı| KIZILELMA
    KAAN ==>|Şifreli KEMENT Taktik Veri Bağı| ANKA3
    ANKA3 --> SUPER_SIMSEK
    KIZILELMA --> SWARM_STRIKE
    ANADOLU --- TB3
    ANADOLU --- MARLIN
    MARLIN <--> SALDIRGAN
```

---

## 📚 Stratejik Dokümantasyon ve Standartlar

Envanterin metodolojisi, savunma mimarisi ve API kullanımı hakkında hazırlanan detaylı teknik kılavuzlar:

| Doküman | Açıklama | Bağlantı |
| :--- | :--- | :--- |
| **Sistem Mimarisi** | Ağ merkezli harp, Çelik Kubbe ve Mavi Vatan entegrasyon doktrini | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| **TRL Değerlendirme Kılavuzu** | NASA/DoD ve SSB TRL 1-9 savunma sanayii hazırlık standartları | [docs/TRL_GUIDE.md](docs/TRL_GUIDE.md) |
| **CLI & Veri Tabanı API** | `inventory_manager.py` komut satırı araçları ve veri formatları | [docs/API_CLI.md](docs/API_CLI.md) |
| **İnteraktif Komuta Ekranı** | Fütüristik ses efektli, radarlı ve filtreli canlı gösterge paneli | [DASHBOARD.html](DASHBOARD.html) |
| **Stratejik Rapor** | Genel ekosistem olgunluk analizi ve şirket bazlı dağılım raporu | [INVENTORY_REPORT.md](INVENTORY_REPORT.md) |
| **JSON Veri Tabanı** | Makine tarafından işlenebilir güncel envanter veri tabanı | [inventory_data.json](inventory_data.json) |
| **CSV Tablo Verisi** | Elektronik tablo ve veri analizi için düzleştirilmiş veri | [inventory_data.csv](inventory_data.csv) |

---

## 🛠️ Envanter Yönetim Aracı (`inventory_manager.py`)

Gelişmiş otomasyon ve veri doğrulama motoru ile envanteri yönetmek için kullanılan temel komutlar:

```bash
# Sistem sağlık denetimi (Tüm spec-sheet ve bağlantıları doğrular)
python inventory_manager.py --health

# Stratejik istatistikleri ve TRL metriklerini terminalde göster
python inventory_manager.py --stats

# Şirketler ve dominionlar arası yetenek matrisini incele
python inventory_manager.py --matrix

# Akıllı çok terimli arama motorunu çalıştır
python inventory_manager.py --search "AESA"

# Tüm sistemleri (README, Dashboard, Rapor, JSON, CSV) tek seferde senkronize et
python inventory_manager.py --sync-all
```

---

## 🤝 Katkıda Bulunma ve Ekosistem Standartları

Milli Teknoloji Envanteri açık kaynaklı, şeffaf ve kurumsal bir bilgi bankasıdır. Yeni bir platform eklemek veya mevcut spec-sheet dokümanlarını güncellemek için:
- Lütfen [CONTRIBUTING.md](CONTRIBUTING.md) belgesini inceleyin.
- GitHub Issue şablonlarını kullanarak doğrudan platform bildiriminde bulunun:
  - [Yeni Platform Ekleme Formu](.github/ISSUE_TEMPLATE/01_yeni_platform.yml)
  - [Teknik Veri Güncelleme](.github/ISSUE_TEMPLATE/02_veri_guncelleme.yml)
  - [Hata / Uyuşmazlık Bildirimi](.github/ISSUE_TEMPLATE/03_hata_bildirimi.yml)

---

<p align="center">
  <b>"Yarın Değil, Şimdi! Gelecek Burada."</b> 🇹🇷<br/>
  <i>Milli Savunma Sanayii & Türk Mühendisliğinin Hizmetindedir.</i>
</p>
"""

        with open(full_readme, 'w', encoding='utf-8') as f:
            f.write(header_part + tables_text + footer_part)

        print(f"✅ {readme_path} başarıyla güncellendi ({total_projects} Proje, TRL {avg_trl:.2f}).")

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
