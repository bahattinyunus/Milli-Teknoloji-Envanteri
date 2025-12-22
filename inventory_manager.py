import os
import argparse
import re

def get_repo_structure():
    structure = {}
    dominions = ['DOMINION_AEROSPACE', 'DOMINION_ELECTRONICS', 'DOMINION_LAND', 'DOMINION_SEA']
    for d in dominions:
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

def extract_trl(proj_name):
    """Attempt to find TRL from root README."""
    readme_path = 'README.md'
    if not os.path.exists(readme_path): return None
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find row with project name
    pattern = rf"\| \*\*\[{proj_name}\].*?\|.*?\|.*?\| (TRL \d(-?\d)?)"
    match = re.search(pattern, content, re.IGNORECASE)

    if match:
        trl_str = match.group(1)
        # Extract digits
        digits = re.findall(r"\d", trl_str)
        if digits:
            return sum(int(d) for d in digits) / len(digits)
    return None

def analyze_health():
    print("\n🔍 --- Milli Teknoloji Envanteri: Sağlık Denetimi --- 🔍\n")
    structure = get_repo_structure()
    missing_readmes = []
    placeholders = []
    
    for d, companies in structure.items():
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
        print("\n📝 Placeholder (Taslak) Durumundaki Projeler:")
        for pl in placeholders: print(f"  - {pl}")
    else:
        print("\n✅ Tüm projeler teknik verilerle zenginleştirilmiş.")

def show_stats():
    print("\n📊 --- Milli Teknoloji Envanteri: Stratejik İstatistikler --- 📊\n")
    structure = get_repo_structure()
    total_projects = 0
    trl_sum = 0
    trl_count = 0
    
    dominion_stats = {}
    
    for d, companies in structure.items():
        dom_projects = 0
        dom_trl_sum = 0
        dom_trl_count = 0
        for c, projects in companies.items():
            for p in projects:
                total_projects += 1
                dom_projects += 1
                trl = extract_trl(p.replace('_', ' '))
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

def search_inventory(query):
    print(f"\n🔎 --- Arama Sonuçları: '{query}' --- 🔎\n")
    structure = get_repo_structure()
    found = False
    for d, companies in structure.items():
        for c, projects in companies.items():
            for p in projects:
                if query.lower() in p.lower() or query.lower() in c.lower():
                    print(f"✅ [{d}] {c.replace('_', ' ')} -> {p.replace('_', ' ')}")
                    found = True
    if not found:
        print("❌ Eşleşen bir kayıt bulunamadı.")

def export_dashboard():
    print("\n🖥️  --- Milli Teknoloji Envanteri: İnteraktif Dashboard Üretiliyor --- 🖥️\n")
    structure = get_repo_structure()
    
    total_projects = 0
    trl_data = {}
    dominion_counts = {}
    
    for d, companies in structure.items():
        dom_name = d.replace('DOMINION_', '')
        dominion_counts[dom_name] = 0
        for c, projects in companies.items():
            for p in projects:
                total_projects += 1
                dominion_counts[dom_name] += 1
                trl = extract_trl(p.replace('_', ' '))
                if trl is not None:
                    trl_key = f"TRL {int(trl)}"
                    trl_data[trl_key] = trl_data.get(trl_key, 0) + 1

    html_template = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Milli Teknoloji Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            body {{ background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; margin: 0; padding: 20px; }}
            h1 {{ font-family: 'Orbitron', sans-serif; color: #58a6ff; text-align: center; text-transform: uppercase; letter-spacing: 3px; }}
            .container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin-top: 40px; }}
            .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; width: 450px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
            .stats-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }}
            .stat-box {{ background: #21262d; padding: 15px; border-radius: 8px; text-align: center; border-left: 4px solid #238636; }}
            .stat-box h3 {{ margin: 0; font-size: 14px; color: #8b949e; }}
            .stat-box p {{ margin: 5px 0 0; font-size: 24px; font-weight: bold; color: #fff; }}
        </style>
    </head>
    <body>
        <h1>Milli Teknoloji Envanteri Dashboard</h1>
        <div class="container">
            <div class="card">
                <div class="stats-grid">
                    <div class="stat-box"><h3>Toplam Proje</h3><p>{total_projects}</p></div>
                    <div class="stat-box" style="border-left-color: #58a6ff;"><h3>Sistem Durumu</h3><p>Aktif</p></div>
                </div>
                <canvas id="dominionChart"></canvas>
            </div>
            <div class="card">
                <canvas id="trlChart"></canvas>
            </div>
        </div>

        <script>
            const domCtx = document.getElementById('dominionChart').getContext('2d');
            new Chart(domCtx, {{
                type: 'polarArea',
                data: {{
                    labels: {list(dominion_counts.keys())},
                    datasets: [{{
                        label: 'Proje Sayısı',
                        data: {list(dominion_counts.values())},
                        backgroundColor: ['#58a6ffCC', '#238636CC', '#cb81feCC', '#f85149CC']
                    }}]
                }},
                options: {{ responsive: true, plugins: {{ legend: {{ position: 'bottom', labels: {{ color: '#fff' }} }} }} }}
            }});

            const trlCtx = document.getElementById('trlChart').getContext('2d');
            new Chart(trlCtx, {{
                type: 'bar',
                data: {{
                    labels: {sorted(list(trl_data.keys()))},
                    datasets: [{{
                        label: 'TRL Dağılımı',
                        data: {[trl_data[k] for k in sorted(trl_data.keys())]},
                        backgroundColor: '#238636'
                    }}]
                }},
                options: {{ 
                    scales: {{ y: {{ beginAtZero: true, grid: {{ color: '#30363d' }}, ticks: {{ color: '#8b949e' }} }}, x: {{ ticks: {{ color: '#8b949e' }} }} }},
                    plugins: {{ legend: {{ labels: {{ color: '#fff' }} }} }}
                }}
            }});
        </script>
    </body>
    </html>
    """
    
    with open('DASHBOARD.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print("✅ DASHBOARD.html başarıyla oluşturuldu. Tarayıcıda açarak inceleyebilirsiniz.")

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Analiz & Yönetim Aracı")
    parser.add_argument('--health', action='store_true', help="Envanterin dokümantasyon sağlığını denetler")
    parser.add_argument('--stats', action='store_true', help="Genel ve Dominion bazlı istatistikler sunar")
    parser.add_argument('--search', type=str, help="Proje veya şirket adına göre arama yapar")
    parser.add_argument('--dashboard', action='store_true', help="İnteraktif HTML Dashboard üretir")
    
    args = parser.parse_args()
    
    if args.health: analyze_health()
    elif args.stats: show_stats()
    elif args.search: search_inventory(args.search)
    elif args.dashboard: export_dashboard()
    else: parser.print_help()

if __name__ == "__main__":
    main()

