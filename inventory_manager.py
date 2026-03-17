import os
import argparse
import re
import json
import datetime
import sys
import io

# Force UTF-8 for stdout/stderr to avoid UnicodeEncodeError on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

class InventoryManager:
    def __init__(self):
        self.root_dir = os.getcwd()
        self.dominions = ['DOMINION_AEROSPACE', 'DOMINION_ELECTRONICS', 'DOMINION_LAND', 'DOMINION_SEA']
        self.structure = self.get_repo_structure()

    def get_repo_structure(self):
        structure = {}
        for d in self.dominions:
            if os.path.isdir(d):
                structure[d] = {}
                for c in os.listdir(d):
                    comp_path = os.path.join(d, c)
                    if os.path.isdir(comp_path):
                        structure[d][c] = []
                        for p in os.listdir(comp_path):
                            proj_path = os.path.join(comp_path, p)
                            if os.path.isdir(proj_path):
                                structure[d][c].append(p)
        return structure

    def extract_trl(self, proj_name, proj_path=None):
        """Attempt to find TRL from root README or project specific README."""
        # 1. Try project-specific README first for more accurate/recent data
        if proj_path:
            p_readme = os.path.join(proj_path, 'README.md')
            if os.path.exists(p_readme):
                with open(p_readme, 'r', encoding='utf-8') as f:
                    p_content = f.read()
                    # Look for "TRL X" or a list item with TRL
                    trl_match = re.search(r"TRL\s*(\d)", p_content, re.IGNORECASE)
                    if trl_match:
                        return float(trl_match.group(1))

        # 2. Fallback to root README table
        readme_path = 'README.md'
        if not os.path.exists(readme_path): return None
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        escaped_name = re.escape(proj_name)
        pattern = rf"\| \*\*\[{escaped_name}\].*?\|.*?\|.*?\| (TRL \d(-?\d)?)"
        match = re.search(pattern, content, re.IGNORECASE)

        if match:
            trl_str = match.group(1)
            digits = re.findall(r"\d", trl_str)
            if digits:
                return sum(int(d) for d in digits) / len(digits)
        return None

    def analyze_health(self):
        print("\n🔍 --- Milli Teknoloji Envanteri: Sağlık Denetimi --- 🔍\n")
        missing_readmes = []
        placeholders = []
        
        for d, companies in self.structure.items():
            for c, projects in companies.items():
                for p in projects:
                    proj_path = os.path.join(d, c, p)
                    readme = os.path.join(proj_path, 'README.md')
                    if not os.path.exists(readme):
                        missing_readmes.append(f"{c}/{p}")
                    else:
                        with open(readme, 'r', encoding='utf-8') as f:
                            if "Detaylı analiz bekleniyor" in f.read():
                                placeholders.append(f"{c}/{p}")
        
        if missing_readmes:
            print("⚠️  README Eksik Olan Projeler:")
            for m in missing_readmes: print(f"  - {m}")
        else:
            print("✅ Tüm projelerin README dosyası mevcut.")
            
        if placeholders:
            print(f"\n📝 Taslak (Placeholder) Durumundaki Projeler: {len(placeholders)} adet")
            # for pl in placeholders: print(f"  - {pl}") # Listeyi çok uzatmamak için gizledim
        else:
            print("\n✅ Tüm projeler teknik verilerle zenginleştirilmiş.")

    def show_stats(self):
        print("\n📊 --- Milli Teknoloji Envanteri: Stratejik İstatistikler --- 📊\n")
        total_projects = 0
        trl_sum = 0
        trl_count = 0
        
        dominion_stats = {}
        
        for d, companies in self.structure.items():
            dom_projects = 0
            dom_trl_sum = 0
            dom_trl_count = 0
            for c, projects in companies.items():
                for p in projects:
                    total_projects += 1
                    dom_projects += 1
                    trl = self.extract_trl(p.replace('_', ' '), os.path.join(d, c, p))
                    if trl is not None:
                        trl_sum += trl
                        trl_count += 1
                        dom_trl_sum += trl
                        dom_trl_count += 1
            
            dominion_stats[d] = {
                "count": dom_projects,
                "avg_trl": dom_trl_sum / dom_trl_count if dom_trl_count > 0 else 0
            }
        
        print(f"📈 Toplam Kayıtlı Proje: {total_projects}")
        print(f"🧬 Genel Ortalama TRL: {trl_sum/trl_count:.2f}" if trl_count > 0 else "🧬 Genel TRL: Bilgi Yok")
        print("\n--- Dominion Bazlı Dağılım ---")
        for d, s in dominion_stats.items():
            print(f"📍 {d.replace('DOMINION_', ''):<12}: {s['count']} Proje | Ort. TRL: {s['avg_trl']:.2f}")

    def search_inventory(self, query):
        print(f"\n🔎 --- Arama Sonuçları: '{query}' --- 🔎\n")
        found = False
        for d, companies in self.structure.items():
            for c, projects in companies.items():
                for p in projects:
                    if query.lower() in p.lower() or query.lower() in c.lower():
                        print(f"✅ [{d}] {c.replace('_', ' ')} -> {p.replace('_', ' ')}")
                        found = True
        if not found:
            print("❌ Eşleşen bir kayıt bulunamadı.")

    def generate_report(self):
        print("\n📝 --- Milli Teknoloji Envanteri: Rapor Oluşturuluyor --- 📝\n")
        report_file = "INVENTORY_REPORT.md"
        
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("# 🇹🇷 Milli Teknoloji Envanteri Raporu\n\n")
            f.write(f"**Tarih:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("## Özet\n")
            
            total_projects = sum(len(projects) for companies in self.structure.values() for projects in companies.values())
            f.write(f"- **Toplam Proje Sayısı:** {total_projects}\n")
            
            for d, companies in self.structure.items():
                dom_name = d.replace('DOMINION_', '')
                dom_count = sum(len(projects) for projects in companies.values())
                f.write(f"- **{dom_name}:** {dom_count} Proje\n")
            
            f.write("\n## Detaylı Envanter\n")
            for d, companies in self.structure.items():
                f.write(f"### {d}\n")
                for c, projects in companies.items():
                    f.write(f"#### {c}\n")
                    for p in projects:
                         # TRL bilgisini çekmeye çalış
                        trl = self.extract_trl(p.replace('_', ' '), os.path.join(d, c, p))
                        trl_str = f" (TRL {trl:.1f})" if trl else ""
                        f.write(f"- {p.replace('_', ' ')}{trl_str}\n")
                f.write("\n")
                
        print(f"✅ Rapor başarıyla oluşturuldu: {report_file}")

    def add_project_wizard(self):
        print("\n🚀 --- Yeni Proje Ekleme Sihirbazı --- 🚀\n")
        
        # 1. Dominion Seçimi
        print("Mevcut Dominionlar:")
        for idx, d in enumerate(self.dominions):
            print(f"{idx + 1}. {d}")
        
        while True:
            try:
                d_idx = int(input("Dominion Seçiniz (No): ")) - 1
                if 0 <= d_idx < len(self.dominions):
                    target_dominion = self.dominions[d_idx]
                    break
                print("Geçersiz seçim.")
            except ValueError:
                print("Lütfen bir sayı giriniz.")
        
        # 2. Şirket/Kurum Girişi
        company = input("Şirket/Kurum Adı (Boşluk yerine '_' kullanın veya otomatik düzeltilecektir): ").strip()
        company = company.replace(" ", "_")
        
        # 3. Proje Adı
        project = input("Proje Adı: ").strip()
        project_safe = project.replace(" ", "_")
        
        # Klasörleri Oluştur
        target_path = os.path.join(target_dominion, company, project_safe)
        
        if os.path.exists(target_path):
            print(f"❌ Hata: Bu proje zaten mevcut! ({target_path})")
            return

        os.makedirs(target_path, exist_ok=True)
        print(f"✅ Klasör oluşturuldu: {target_path}")
        
        # README Oluştur
        readme_content = f"""# {project}
    
> **Üretici:** {company.replace('_', ' ')}  
> **Alan:** {target_dominion.replace('DOMINION_', '')}

## 📝 Proje Tanımı
Detaylı analiz bekleniyor...

## ⚙️ Teknik Özellikler
- **Tip:** ...
- **Menzil:** ...
- **Hız:** ...

## 🚀 Geliştirme Durumu (TRL)
- [ ] Kavramsal Tasarım
- [ ] Prototip
- [ ] Seri Üretim
"""
        with open(os.path.join(target_path, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)
            
        print("✅ Taslak README.md oluşturuldu.")
        print("\n🎉 Proje başarıyla eklendi! Lütfen ana README.md dosyasını güncellemeyi unutmayın.")

    def export_dashboard(self):
        print("\n🖥️  --- Milli Teknoloji Envanteri: İnteraktif Dashboard Üretiliyor --- 🖥️\n")
        
        total_projects = 0
        trl_data = {}
        dominion_counts = {}
        projects_list = [] # For the data table
        
        for d, companies in self.structure.items():
            dom_name = d.replace('DOMINION_', '')
            dominion_counts[dom_name] = 0
            for c, projects in companies.items():
                for p in projects:
                    total_projects += 1
                    dominion_counts[dom_name] += 1
                    trl = self.extract_trl(p.replace('_', ' '), os.path.join(d, c, p))
                    
                    trl_val = 0
                    if trl is not None:
                        trl_key = f"TRL {int(trl)}"
                        trl_data[trl_key] = trl_data.get(trl_key, 0) + 1
                        trl_val = trl
                    else:
                        trl_data["Bilinmiyor"] = trl_data.get("Bilinmiyor", 0) + 1
                    
                    projects_list.append({
                        "name": p.replace('_', ' '),
                        "company": c.replace('_', ' '),
                        "dominion": dom_name,
                        "trl": trl_val if trl_val else "N/A"
                    })

        # Load the newly created DASHBOARD.html template if it exists, otherwise use a fallback
        template_path = 'DASHBOARD.html'
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                html_template = f.read()
        else:
            # Fallback (mini version of the new UI)
            html_template = "<!-- TEMPLATE MISSING -->"

        # Inject Data
        # Replace 'const inventoryData = [];' with actual data
        data_injection = f"const inventoryData = {json.dumps(projects_list, ensure_ascii=False)};"
        html_template = html_template.replace("const inventoryData = [];", data_injection)
        
        # Inject chart data (Dominion)
        dom_labels = list(dominion_counts.keys())
        dom_values = list(dominion_counts.values())
        chart_js = f"""
        new Chart(document.getElementById('dominionChart'), {{
            type: 'doughnut',
            data: {{
                labels: {json.dumps(dom_labels)},
                datasets: [{{
                    data: {json.dumps(dom_values)},
                    backgroundColor: ['#00d2ff', '#3fb950', '#cb81fe', '#f85149'],
                    borderWidth: 0
                }}]
            }},
            options: {{ 
                plugins: {{ 
                    legend: {{ position: 'bottom', labels: {{ color: '#8b949e', font: {{ family: 'Outfit' }} }} }} 
                }},
                cutout: '70%'
            }}
        }});
        // Render initial table
        renderTable(inventoryData);
        """
        html_template = html_template.replace("// Chart population would happen here using chart.js", chart_js)

        with open('DASHBOARD.html', 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        with open('DASHBOARD.html', 'w', encoding='utf-8') as f:
            f.write(html_template)
        
    def sync_root_readme(self):
        """Sync TRL values from subdirectories back to the root README.md"""
        print("\n🔄 --- Ana README.md Senkronize Ediliyor --- 🔄\n")
        readme_path = 'README.md'
        if not os.path.exists(readme_path): return
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        updated_content = content
        for d, companies in self.structure.items():
            for c, projects in companies.items():
                for p in projects:
                    proj_name = p.replace('_', ' ')
                    trl = self.extract_trl(proj_name, os.path.join(d, c, p))
                    if trl:
                        # Find the row and update TRL
                        # Pattern looks for | **[Name]... | ... | ... | TRL X
                        # We want to replace TRL X with TRL {trl}
                        pattern = rf"(\| \*\*\[{re.escape(proj_name)}\].*?\|.*?\|.*?\| )TRL \d(-?\d)?"
                        replacement = rf"\1TRL {int(trl)}"
                        updated_content = re.sub(pattern, replacement, updated_content, flags=re.IGNORECASE)

        if updated_content != content:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print("✅ Ana README.md başarıyla güncellendi.")
        else:
            print("ℹ️ Herhangi bir değişiklik gerekmiyor.")

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Yönetim Sistemi v2.0")
    parser.add_argument('--health', action='store_true', help="Sağlık kontrolü yap")
    parser.add_argument('--stats', action='store_true', help="İstatistikleri göster")
    parser.add_argument('--search', type=str, help="Arama yap")
    parser.add_argument('--dashboard', action='store_true', help="HTML Dashboard oluştur")
    parser.add_argument('--report', action='store_true', help="Markdown rapor oluştur")
    parser.add_argument('--add', action='store_true', help="Yeni proje ekleme sihirbazını başlat")
    parser.add_argument('--sync', action='store_true', help="Alt README'lerdeki TRL verilerini ana README'ye işle")
    
    args = parser.parse_args()
    manager = InventoryManager()
    
    if args.health: manager.analyze_health()
    if args.stats: manager.show_stats()
    if args.search: manager.search_inventory(args.search)
    if args.dashboard: manager.export_dashboard()
    if args.report: manager.generate_report()
    if args.add: manager.add_project_wizard()
    if args.sync: manager.sync_root_readme()
    
    if not any([args.health, args.stats, args.search, args.dashboard, args.report, args.add]):
        parser.print_help()

if __name__ == "__main__":
    main()
