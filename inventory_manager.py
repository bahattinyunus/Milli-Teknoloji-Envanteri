import os
import argparse

def list_inventory():
    """Lists all project README files under the complete corporate Nexus."""
    # The Full elite corporate list
    companies = [
        'TUSAŞ', 'BAYKAR', 'ASELSAN', 'ROKETSAN', 'MKE', 
        'HAVELSAN', 'Nurol_Makina', 'FNSS', 'BMC', 'OTOKAR', 
        'Katmerciler', 'Titra', 'Lentatek', 'ASFAT', 'STM', 
        'SEDEF', 'ARES', 'Yonca-Onuk', 'METEKSAN', 'Sarsılmaz', 
        'CANİK', 'TÜBİTAK_SAGE', 'Altınay_Savunma', 'MilSOFT', 'SDT', 'TEI'
    ]
    
    print("\n🇹🇷 --- Milli Teknoloji Envanteri: Nihai Kurumsal Arama --- 🇹🇷\n")
    
    found_any = False
    for company in companies:
        company_dir = company
        if os.path.isdir(company_dir):
            print(f"🏢 {company.replace('_', ' ')}:")
            found_company_project = False
            try:
                items = os.listdir(company_dir)
            except OSError:
                continue
                
            for project in items:
                project_path = os.path.join(company_dir, project)
                if os.path.isdir(project_path):
                    readme_path = os.path.join(project_path, 'README.md')
                    if os.path.exists(readme_path):
                        print(f"  - {project.replace('_', ' ')}")
                        found_company_project = True
                        found_any = True
            
            if not found_company_project:
                print("  - (Tüm projeler hazırlık aşamasında)")
    
    if not found_any:
        print("Envanter veri tabanı henüz oluşturulmamış veya boş.")
        
    print("\n--- Nihai Rapor Hazır ---\n")

def main():
    parser = argparse.ArgumentParser(description="Milli Teknoloji Envanteri Yönetim Aracı")
    parser.add_argument('--list', action='store_true', help="Tüm envanteri nihai kurumsal bazda listeler")
    
    args = parser.parse_args()
    
    if args.list:
        list_inventory()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
