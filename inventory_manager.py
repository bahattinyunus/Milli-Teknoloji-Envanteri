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

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Analiz & Yönetim Aracı")
    parser.add_argument('--health', action='store_true', help="Envanterin dokümantasyon sağlığını denetler")
    parser.add_argument('--stats', action='store_true', help="Genel ve Dominion bazlı istatistikler sunar")
    parser.add_argument('--search', type=str, help="Proje veya şirket adına göre arama yapar")
    
    args = parser.parse_args()
    
    if args.health: analyze_health()
    elif args.stats: show_stats()
    elif args.search: search_inventory(args.search)
    else: parser.print_help()

if __name__ == "__main__":
    main()
