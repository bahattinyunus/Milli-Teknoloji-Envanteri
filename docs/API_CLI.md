# 🛠️ inventory_manager.py CLI & Veri API Dokümantasyonu

`inventory_manager.py`, Milli Teknoloji Envanteri deposunun bütünlüğünü korumak, veri analizi yapmak ve dışa aktarmak için geliştirilmiş kurumsal bir Python motorudur.

---

## 💻 Komut Satırı Seçenekleri (CLI Options)

```bash
# Sistem Sağlık Denetimi (Health Check)
# Tüm projelerin README, TRL, link ve içerik uzunluklarını denetler.
python inventory_manager.py --health

# Stratejik İstatistikler & TRL Göstergeleri
# Dominion yüzdeleri, ortalama TRL ve TRL histogramını ekrana basar.
python inventory_manager.py --stats

# Şirket & Dominion Yetenek Matrisi
# 30 savunma sanayii kurumunun 4 boyuttaki varlık dağılımını gösterir.
python inventory_manager.py --matrix

# Akıllı Türkçe Arama (Diacritic & Case Insensitive)
python inventory_manager.py --search "AESA Radar"

# İnteraktif Sci-Fi Dashboard'u Güncelle
# DASHBOARD.html içerisine güncel veri setini ve grafik parametrelerini enjekte eder.
python inventory_manager.py --dashboard

# Detaylı Markdown Yönetici Raporu Üret
# INVENTORY_REPORT.md dosyasını baştan oluşturur.
python inventory_manager.py --report

# JSON Veri Tabanı İhracı
python inventory_manager.py --export-json

# CSV Tablo İhracı
python inventory_manager.py --export-csv

# Ana README.md Dosyasını Senkronize Et
python inventory_manager.py --sync

# Tam Otomatik Ekosistem Senkronizasyonu (Tüm Görevler Tek Seferde)
python inventory_manager.py --sync-all
```

---

## 📦 Veri Şeması (JSON / CSV)

`inventory_data.json` dosyası aşağıdaki standart veri şemasına uyar:

```json
{
  "metadata": {
    "title": "Milli Teknoloji Envanteri",
    "generated_at": "2026-11-18 22:40:00",
    "total_projects": 172,
    "average_trl": 8.20,
    "version": "4.0"
  },
  "projects": [
    {
      "name": "KAAN",
      "company": "TUSAŞ",
      "dominion": "AEROSPACE",
      "trl": 7.0,
      "status": "Uçuş Testleri ve Zarf Açma",
      "class": "Milli Muharip Uçak - MMU / 5. Nesil Savaş Uçağı",
      "strategic_role": "Hava hakimiyeti ve stratejik caydırıcılık...",
      "image": "_ASSETS/platforms/KAAN.jpg",
      "specs": {
        "Azami Hız": "Mach 1.8+ (Süperseyir / Supercruise yetenekli)",
        "Servis Tavanı": "55.000 ft (16.764 m)"
      },
      "path": "DOMINION_AEROSPACE/TUSAŞ/KAAN"
    }
  ]
}
```
