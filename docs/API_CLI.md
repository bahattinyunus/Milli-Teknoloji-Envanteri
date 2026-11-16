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
    "generated_at": "2026-11-16 17:00:00",
    "total_projects": 167,
    "average_trl": 8.27,
    "version": "3.5"
  },
  "projects": [
    {
      "name": "KAAN",
      "company": "TUSAŞ",
      "dominion": "AEROSPACE",
      "trl": 7.0,
      "class": "5. Nesil Milli Muharip Uçak",
      "strategic_role": "Hava hakimiyeti ve stratejik caydırıcılık...",
      "path": "DOMINION_AEROSPACE/TUSAŞ/KAAN/README.md"
    }
  ]
}
```
