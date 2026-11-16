# 🤖 Proje: SARBOT (Silahlı Otonom Robotik Kara Aracı)

<div align="center">



[![TRL](https://img.shields.io/badge/TRL-7-3f51b5?style=for-the-badge&logo=shield&logoColor=white)

<p align="center">
  <img src="../../../_ASSETS/platforms/SARBOT.jpg" alt="SARBOT" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](../../../docs/TRL_GUIDE.md)
[![Dominion](https://img.shields.io/badge/DOMINION-LAND-green?style=for-the-badge&logo=target&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/MANUFACTURER-SARSILMAZ-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/STATUS-S%C4%B0STEM%20PROTOT%C4%B0P%20%2F%20SAHA%20TESTLER%C4%B0-orange?style=for-the-badge)]()

</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik

**SARBOT**, Türkiye'nin köklü silah üreticisi Sarsılmaz'ın otonom savunma teknolojileri ve robotik harp sahası vizyonu doğrultusunda geliştirdiği **Silahlı İnsansız Kara Aracı (SİKA) ve Robotik Platform Ailesidir**. İnsan hayatını riske atmadan sıcak temas bölgelerinde, meskun mahal operasyonlarında, mağara/tünel keşiflerinde ve kritik üs güvenliğinde Mehmetçiğe doğrudan ileri hat ateş desteği sağlamak üzere geliştirilmiştir.

Modüler paletli ve çok tekerlekli şasi seçeneklerine sahip olan SARBOT; yapay zeka destekli otonom rota takibi, dinamik engel sakınma, dost/düşman tanıma ve Sarsılmaz'ın yerli makineli tüfek aileleri (SAR 762 MT, SAR 127 MT, SAR 109T) ile donatılmış hafif uzaktan komutalı silah kuleleri ile donatılmıştır.

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Araç Tipi** | Hafif / Orta Sınıf Silahlı İnsansız Kara Aracı (SİKA) | Paletli veya çok tekerlekli modüler yürüyüş takımı |
| **Tahrik & Güç** | Tam Elektrikli / BLDC Motor + Li-Ion Batarya Paketi | Sessiz intikal ve düşük termal ayak izi |
| **Operasyonel Süre** | 4 - 8 Saat (Batarya kapasitesine göre) | Hızlı değiştirilebilir modüler batarya blokları |
| **Azami Hız** | 15 - 25 km/s | Engebeli arazide ve bina içinde dinamik hareket |
| **Otonomi Düzeyi** | Seviye 3+ Otonom Seyrüsefer & Konvoy Takip | 3D SLAM, LiDAR ve Stereo Vizyon algoritmaları |
| **Faydalı Yük / Silah** | SAR 762 MT (7.62x51mm) / SAR 109T (9mm) / SAR 127 | Sarsılmaz UKSS stabilize hafif kule istasyonu |
| **Mühimmat Kapasitesi** | 500 - 1.000 Mermi (7.62mm) | Kesintisiz baskı ateşi sağlayan geniş kutu hazne |
| **Kontrol & Veri Bağı** | Güvenli Kriptolu RF Link + Wi-Fi Mesh + Fiber Optik Hat | Karıştırmaya dayanıklı 2+ km kontrol menzili |
| **Gözetleme & Sensörler** | 360° Gece/Gündüz Kamera, Termal FLIR, Akustik Algılayıcı | Tehdit yönünü anında tespit eden mikrofon dizilimi |

---

## 🧩 Alt Sistemler ve Aviyonik / Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph SARBOT_CORE["SARBOT Otonomi & Kontrol Gövdesi"]
        AI_NAV["Gömülü Yapay Zeka Seyrüsefer İşlemcisi<br/>(SLAM + Engel Sakınma)"]
        BATTERY_SYS["Yüksek Enerji Yoğunluklu Li-Ion Güç Paketi"]
        MOTOR_DRIVE["Çift Elektrikli Palet/Teker Sürüş Motorları"]
    end

    subgraph SENSOR_SUITE["Sensör ve Farkındalık Paketi"]
        LIDAR_3D["3D Katı Hal LiDAR"]
        EO_IR["Gündüz HD Zoom Kamera + Soğutmasız Termal FLIR"]
        ACOUSTIC["Atış Yeri Tespit Eden Akustik Mikrofon Ağı"]
    end

    subgraph WEAPON_PAYLOAD["Sarsılmaz Silah Kulesi"]
        SARP_MINI["Mini Stabilize UKSS (2 Eksenli Gyro)"]
        SAR_MG["SAR 762 MT (7.62x51mm) / SAR 127 MT"]
        AMMO_FEED["Otomatik Mayon Besleme ve Mühimmat Sayacı"]
    end

    subgraph OPERATOR_STATION["Taktik Operatör Konsolu"]
        RUGGED_TABLET["Askeri Standart Dayanıklı Tablet / Giyilebilir Kumanda"]
        BMS_LINK["MUM-T Kara Kuvvetleri Taktik Muharebe Ağı"]
    end

    SENSOR_SUITE --> AI_NAV
    AI_NAV --> MOTOR_DRIVE
    BATTERY_SYS --> MOTOR_DRIVE
    AI_NAV --> WEAPON_PAYLOAD
    OPERATOR_STATION <===>|Kriptolu RF Veri Bağı| AI_NAV
```

- **Sessiz Yaklaşma ve Termal Görünmezlik:** Elektrik motorları sayesinde motor sesi çıkarmadan hedefe yaklaşabilir; egzoz ısısı olmadığı için düşman termal kameralarınca fark edilmesi son derece güçtür.
- **Akustik Atış Yeri Tespiti:** Üzerindeki mikrofon dizilimi düşman keskin nişancı veya tüfek ateşinin ses dalgalarını analiz ederek namluyu milisaniyeler içinde doğrudan atışın yapıldığı koordinata otomatik çevirir.
- **Tünel ve Mağara Modu:** GNSS (GPS) sinyalinin olmadığı yer altı sığınaklarında ve mağaralarda LiDAR tabanlı 3D haritalama yaparak yolunu otonom bulur ve geri döner.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi

1. **Bina ve Tünel Girişi Öncü Keşif:** Askeri timlerin içeri girmesinden önce odaya girip tuzak, EYP ve düşman varlığını görüntüleme ve gerekirse ateşle temizleme.
2. **Karakol ve Üs Çevre Emniyeti:** Belirlenen sınır hattında otonom nöbet devriyesi icra ederek tel örgüye yaklaşan izinsiz sızmaları tespit etme.
3. **Piyade İleri Ateş Desteği:** Yoğun çatışma anında siperden çıkamayan personelin yerine öne sürülerek SAR 762 MT ile düşman mevzisini ateş altına alma.
4. **Yaralı ve Teçhizat İkmali:** Küçük boyutuna rağmen 100+ kg mühimmat veya sıhhiye malzemesini tehlikeli hat boyunca personele ulaştırma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

- **Mevcut Durum:** `TRL 7` (Saha prototipleri üretilmiş, askeri poligonlarda atışlı ve otonom hareket doğrulama testleri icra edilmektedir).
- [x] Konsept tasarımı ve robotik şasi imalatı
- [x] Otonomi algoritmaları, LiDAR entegrasyonu ve iç mekan haritalama testleri
- [x] SAR 762 MT makineli tüfek entegrasyonu ve atış denemeleri
- [ ] Karma sürü halinde hareket ve MUM-T müşterek harekat yazılımı
- [ ] Güvenlik kuvvetleri envanter kabul testleri

---

## 🔗 İç Dizin Navigasyonu

[⬅️ Üst Dizine (Sarsılmaz)](../README.md) | [🏛️ Dominion Hub (DOMINION_LAND)](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
