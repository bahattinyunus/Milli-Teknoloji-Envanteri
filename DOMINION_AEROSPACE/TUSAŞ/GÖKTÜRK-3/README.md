# 📡 Proje: GÖKTÜRK-3 (Sentetik Açıklıklı Radar - SAR Keşif Uydusu)

[![TRL](https://img.shields.io/badge/TRL-6_Sistem_Doğrulama_Aşamasında-blue?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TUSAŞ_%26_ASELSAN-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Geliştirme_ve_Test-orange?style=for-the-badge)](README.md)

<p align="center">
  <img src="../../../_ASSETS/platforms/GOKTURK-3.jpg" alt="GÖKTÜRK-3" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![GÖKTÜRK-3 Sentetik Açıklıklı Radar (SAR) Uydusu Tasarımı](https://www.tusas.com/uploads/2021/04/gokturk-3-web.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
GÖKTÜRK-3, optik kameraların yetersiz kaldığı gece şartlarında, yoğun bulutlu, sisli ve her türlü zorlu hava koşullarında dahi Dünya yüzeyinden santimetre mertebesinde yüksek çözünürlüklü radar görüntüsü elde etmek üzere geliştirilen milli Sentetik Açıklıklı Radar (SAR) uydusudur. TUSAŞ ana yükleniciliğinde ve ASELSAN SAR faydalı yük sorumluluğunda yürütülen proje; Türkiye'nin kesintisiz '24 saat / her hava koşulunda' küresel istihbarat toplama doktrininin en kritik uzay ayağıdır. SAR teknolojisi sayesinde kamuflaj altındaki askeri unsurları, radar yansıtıcılarını ve yer değişikliklerini tespit edebilme kabiliyeti sunar.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Radar Faydalı Yükü** | Aktif Faz Dizinli X-Bant SAR (Sentetik Açıklıklı Radar) |
| **Görüntüleme Çözünürlüğü** | Spotlight Modunda: <0.5 metre | Stripmap: ~1 metre | ScanSAR: ~3 metre |
| **Çalışma Frekansı** | X-Bant (ASELSAN tasarımı T/R modülleri) |
| **Yörünge Tipi** | Güneş Eşzamanlı Alçak Dünya Yörüngesi (Sun-Synchronous LEO) |
| **Yörünge İrtifası** | 500 - 600 km |
| **Kütle / Sınıf** | ~1.500 - 2.000 kg sınıfı ağır SAR platformu |
| **Görüntüleme Modları** | Spotlight, Stripmap, ScanSAR, Deniz Gözlem Modu (Maritime) |
| **İtki Sistemi** | Elektrikli İtki / Kimyasal İtki Hibrit Yörünge Düzeltme |
| **Veri Linki Hızı** | Kriptolu X/Ka-Bant Çok Yüksek Hızlı SAR Downlink |
| **Görev Ömrü** | En az 7 yıl |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **ASELSAN X-Bant SAR Anteni:** Binlerce T/R (Gönderme/Alma) GaN modülünden oluşan elektronik hüzme yönlendirmeli aktif faz dizinli radar.
- **SAR Veri İşleme Ünitesi:** Yüksek hızlı çiplerle ham radar yankılarının uzayda ön işlenmesi ve veri sıkıştırma algoritmaları.
- **Gelişmiş Yörünge & Yönelim Kontrol (AOCS):** Ağır radar anteninin oluşturduğu atalet momentlerini dengeleyen yüksek torklu tepki tekerleri.
- **Yüksek Güç Enerji Ünitesi:** SAR radarının anlık yüksek güç tüketimini karşılayan büyük alanlı güneş panelleri ve yüksek deşarj kapasiteli bataryalar.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Her Hava Şartında İstihbarat:** Yoğun bulut tabakası, yağmur veya gece karanlığından etkilenmeden hedef sahasının 3 boyutlu radar haritalanması.
- **Hareketli Hedef Tespiti (GMTI):** Kara ve deniz yüzeyindeki hareketli askeri unsurların (tank konvoyları, savaş gemileri) tespiti ve takibi.
- **Kamuflaj Delici İstihbarat:** Radar dalgalarının yaprak örtüsü ve hafif engelleri geçerek gizlenmiş hedefleri açığa çıkarması.
- **İnterferometrik SAR (InSAR):** Zemin çöküntüleri, fay hatları hareketleri ve askeri tahkimat kazılarının milimetrik tespiti.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "SAR Sensör & Donanım"
        S1["ASELSAN X-Bant Aktif Faz Dizinli Anten"]
        S2["GaN T/R Modülleri (Elektronik Hüzme Yönlendirme)"]
        S3["Yüksek Güçlü Enerji & Batarya Depolama"]
    end
    subgraph "Uydu Aviyonik & Veri Hattı"
        A1["Yerleşik SAR Ham Veri Sıkıştırma Birimi"]
        A2["Katı Hal Hafıza (Terabit Kapasiteli)"]
        A3["Kriptolu X/Ka-Bant Downlink Transponder"]
    end
    subgraph "Yer İstasyonu & Analiz"
        Y1["Hava Kuvvetleri SAR Yer İstasyonu"]
        Y2["SAR Görüntü Oluşturma İşlemcisi (SAR Processor)"]
        Y3["Hedef Kıymetlendirme & Değişim Tespiti (CDA)"]
    end
    S1 --> S2 --> S3
    S2 --> A1 --> A2 --> A3
    A3 ==> Y1
    Y1 --> Y2 --> Y3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] SAR Radar Teknolojisi Fizibilite ve Mimari Tasarım
- [x] T/R Modül ve Anten Laboratuvar Doğrulaması
- [x] USET Altyapısında SAR Entegrasyon Modeli Testleri
- [ ] Uçuş Modeli İmalatı ve Uydu Düzeyi Entegrasyon
- [ ] Fırlatma ve Yörüngede Radar Kalibrasyonu (TRL 6 -> TRL 9)

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
