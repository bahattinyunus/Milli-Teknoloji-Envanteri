import os
import argparse
import re
import json
import datetime

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

    def extract_trl(self, proj_name):
        """Attempt to find TRL from root README."""
        readme_path = 'README.md'
        if not os.path.exists(readme_path): return None
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Normalize project name for regex (escape special chars just in case)
        escaped_name = re.escape(proj_name)
        
        # Regex to find the row in the markdown table
        # Looking for | **[ProjectName]... | ... | TRL X
        pattern = rf"\| \*\*\[{escaped_name}\].*?\|.*?\|.*?\| (TRL \d(-?\d)?)"
        match = re.search(pattern, content, re.IGNORECASE)

        if match:
            trl_str = match.group(1)
            # Extract digits
            digits = re.findall(r"\d", trl_str)
            if digits:
                # If range like 1-3, return average (2)
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
                    trl = self.extract_trl(p.replace('_', ' '))
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
                        trl = self.extract_trl(p.replace('_', ' '))
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
                    trl = self.extract_trl(p.replace('_', ' '))
                    
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

        html_template = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Milli Teknoloji Envanteri</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg-dark: #0d1117; --card-bg: #161b22; --border: #30363d; --accent: #58a6ff; --text: #c9d1d9; --success: #238636; }}
        body {{ background-color: var(--bg-dark); color: var(--text); font-family: 'Inter', sans-serif; margin: 0; padding: 20px; }}
        h1, h2 {{ font-family: 'Orbitron', sans-serif; color: var(--accent); text-transform: uppercase; letter-spacing: 2px; }}
        .header {{ text-align: center; margin-bottom: 40px; border-bottom: 1px solid var(--border); padding-bottom: 20px; }}
        .grid-container {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px; margin-bottom: 40px; }}
        .card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        .stat-box {{ background: #21262d; padding: 15px; border-radius: 8px; text-align: center; border-left: 4px solid var(--success); margin-bottom: 10px; }}
        .stat-box h3 {{ margin: 0; font-size: 12px; color: #8b949e; }}
        .stat-box p {{ margin: 5px 0 0; font-size: 24px; font-weight: bold; color: #fff; }}
        
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid var(--border); }}
        th {{ color: var(--accent); font-family: 'Orbitron', sans-serif; font-size: 12px; }}
        tr:hover {{ background-color: #21262d; }}
        input[type="text"] {{ width: 100%; padding: 10px; margin-bottom: 10px; background: #0d1117; border: 1px solid var(--border); color: #fff; border-radius: 6px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Milli Teknoloji Envanteri Dashboard</h1>
        <p>Stratejik Teknoloji Takip Sistemi</p>
    </div>

    <div class="grid-container">
        <!-- İstatistikler -->
        <div class="card">
            <h2>Genel Durum</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div class="stat-box"><h3>TOPLAM PROJE</h3><p>{total_projects}</p></div>
                <div class="stat-box" style="border-left-color: var(--accent);"><h3>SİSTEM DURUMU</h3><p>OPERASYONEL</p></div>
                <div class="stat-box" style="border-left-color: #cb81fe;"><h3>DOMINION SAYISI</h3><p>4</p></div>
                <div class="stat-box" style="border-left-color: #f85149;"><h3>ORTALAMA TRL</h3><p>N/A</p></div>
            </div>
        </div>

        <!-- Grafikler -->
        <div class="card">
            <canvas id="dominionChart"></canvas>
        </div>
        <div class="card">
            <canvas id="trlChart"></canvas>
        </div>
    </div>

    <!-- Veri Tablosu -->
    <div class="card" style="width: 100%; box-sizing: border-box;">
        <h2>Envanter Listesi</h2>
        <input type="text" id="searchInput" onkeyup="filterTable()" placeholder="Proje, Şirket veya Dominion ara...">
        <table id="projectTable">
            <thead>
                <tr>
                    <th>Proje Adı</th>
                    <th>Şirket</th>
                    <th>Dominion</th>
                    <th>TRL Seviyesi</th>
                </tr>
            </thead>
            <tbody>
                <!-- JS ile doldurulacak -->
            </tbody>
        </table>
    </div>

    <script>
        const projectData = {json.dumps(projects_list)};

        // Tabloyu Doldur
        const tableBody = document.querySelector("#projectTable tbody");
        
        function renderTable(data) {{
            tableBody.innerHTML = "";
            data.forEach(p => {{
                const row = `<tr>
                    <td><strong>${{p.name}}</strong></td>
                    <td>${{p.company}}</td>
                    <td><span style="font-size: 10px; padding: 2px 6px; border-radius: 4px; background: #30363d;">${{p.dominion}}</span></td>
                    <td>${{p.trl}}</td>
                </tr>`;
                tableBody.innerHTML += row;
            }});
        }}
        renderTable(projectData);

        // Arama Fonksiyonu
        function filterTable() {{
            const query = document.getElementById("searchInput").value.toLowerCase();
            const filtered = projectData.filter(p => 
                p.name.toLowerCase().includes(query) || 
                p.company.toLowerCase().includes(query) || 
                p.dominion.toLowerCase().includes(query)
            );
            renderTable(filtered);
        }}

        // Grafikler
        new Chart(document.getElementById('dominionChart'), {{
            type: 'doughnut',
            data: {{
                labels: {list(dominion_counts.keys())},
                datasets: [{{
                    data: {list(dominion_counts.values())},
                    backgroundColor: ['#58a6ff', '#238636', '#cb81fe', '#f85149'],
                    borderWidth: 0
                }}]
            }},
            options: {{ plugins: {{ legend: {{ position: 'right', labels: {{ color: '#fff' }} }} }} }}
        }});

        new Chart(document.getElementById('trlChart'), {{
            type: 'bar',
            data: {{
                labels: {sorted(list(trl_data.keys()))},
                datasets: [{{
                    label: 'Proje Sayısı',
                    data: {[trl_data[k] for k in sorted(trl_data.keys())]},
                    backgroundColor: '#238636'
                }}]
            }},
            options: {{ 
                plugins: {{ legend: {{ display: false }} }},
                scales: {{ y: {{ grid: {{ color: '#30363d' }}, ticks: {{ color: '#8b949e' }} }} }}
            }}
        }});
    </script>
</body>
</html>"""
        
        with open('DASHBOARD.html', 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        print("✅ DASHBOARD.html başarıyla oluşturuldu (v2.0).")

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Yönetim Sistemi v2.0")
    parser.add_argument('--health', action='store_true', help="Sağlık kontrolü yap")
    parser.add_argument('--stats', action='store_true', help="İstatistikleri göster")
    parser.add_argument('--search', type=str, help="Arama yap")
    parser.add_argument('--dashboard', action='store_true', help="HTML Dashboard oluştur")
    parser.add_argument('--report', action='store_true', help="Markdown rapor oluştur")
    parser.add_argument('--add', action='store_true', help="Yeni proje ekleme sihirbazını başlat")
    
    args = parser.parse_args()
    manager = InventoryManager()
    
    if args.health: manager.analyze_health()
    if args.stats: manager.show_stats()
    if args.search: manager.search_inventory(args.search)
    if args.dashboard: manager.export_dashboard()
    if args.report: manager.generate_report()
    if args.add: manager.add_project_wizard()
    
    if not any([args.health, args.stats, args.search, args.dashboard, args.report, args.add]):
        parser.print_help()

if __name__ == "__main__":
    main()
