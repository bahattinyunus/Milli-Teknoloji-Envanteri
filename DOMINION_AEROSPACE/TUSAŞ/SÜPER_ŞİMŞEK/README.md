# ⚡ Proje: SÜPER ŞİMŞEK (Yüksek Hızlı Sahte Hedef ve Kamikaze İHA)

[![TRL](https://img.shields.io/badge/TRL-7_Prototip_Uçuş_Testi-blue?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TUSAŞ-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Uçuş_Testleri_ve_Mühimmat_Entegrasyonu-yellow?style=for-the-badge)](README.md)

<div align="center">
  <img src="../../../_ASSETS/aerospace_icon.png" alt="DOMINION AEROSPACE" width="100"/>
</div>

![TUSAŞ SÜPER ŞİMŞEK Yüksek Hızlı Hedef / Kamikaze İHA Sistemi](https://www.tusas.com/uploads/super-simsek.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
SÜPER ŞİMŞEK, TUSAŞ'ın operasyonel tecrübeye sahip ŞİMŞEK hedef uçak ailesinin yüksek hızlı, artırılmış menzilli ve modüler faydalı yük taşıyabilen yeni nesil türevidir. ANKA-3, AKSUNGUR ve KAAN gibi insansız ve insanlı taarruz uçaklarından havadan salınabilen (Air-Launched) bu platform; düşman hava savunma radarlarını yanıltıcı 'Sahte Hedef' (Air-Launched Decoy - ADM), aktif elektronik karıştırıcı veya harp başlığı entegre edilmiş 'Kamikaze / Dolanan Mühimmat' konfigürasyonlarında görev yapabilmektedir. Düşman radar ağlarını doyuma ulaştırma ve hava savunma bataryalarını gafil avlama doktrininin kritik bir asimetrik unsurudur.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Maksimum Kalkış Ağırlığı** | ~200 kg |
| **Faydalı Yük Kapasitesi** | 35 - 50 kg (Harp başlığı veya Elektronik Harp kiti) |
| **Motor Tipi** | 1 x Mini Turbojet Motoru (TEI TJ90 / TJ300 türevi) |
| **Maksimum Hız** | Mach 0.8 - 0.9 (Yüksek Subsonik / Transonik) |
| **Menzil / Harekât Yarıçapı** | 700+ km (Havadan salım ile) |
| **Servis Tavanı** | 35.000 ft (10.668 m) |
| **Fırlatma Yöntemleri** | ANKA, AKSUNGUR, ANKA-3, KAAN harici/dahili istasyonlarından veya karadan roket destekli (RATO) katapult |
| **Güdüm ve Kontrol** | INS/GPS, Anti-Jamming GNSS, Optik/Kızılötesi Terminal Güdüm opsiyonu |
| **Gövde Malzemesi** | Düşük radar izli kompozit kanat ve gövde |
| **Sahte Hedef Yeteneği** | Lünberg lensi ve aktif RF transponder ile farklı uçak tiplerinin radar izini taklit etme |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Aktif/Pasif Radar Yansıtıcı:** Farklı avcı uçaklarının (F-16, F-4, vb.) radar kesit alanını taklit eden dijital radar izi simülatörü.
- **Elektronik Harp Podu:** Minyatür RF karıştırıcı (Jammer) ve chaff dağıtım donanımı.
- **Otonom Uçuş Bilgisayarı:** TUSAŞ otonom seyrüsefer ve hedef takip algoritmaları, önceden planlanmış yanıltıcı rota profilleri.
- **Taktik Veri Bağı:** Ana fırlatıcı platform (ANKA-3 / AKSUNGUR) ile çift yönlü şifreli telemetri ve hedef güncelleme kanalı.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Hava Savunma Aldatması (Decoy):** Düşman S-300/S-400 benzeri uzun menzilli hava savunma bataryalarını üzerine çekerek radarlarını açmaya zorlama ve mühimmatlarını boşa harcatma.
- **Kamikaze Taarruz:** Tespit edilen düşman erken ihbar radarlarına veya komuta merkezlerine yüksek hızla dalış yaparak harp başlığıyla imha etme.
- **Elektronik Taarruz (Stand-in Jamming):** Düşman hava sahasının derinliklerinde radar karıştırması yaparak dost taarruz uçaklarına güvenli koridor açma.
- **Hedef Uçak Eğitimi:** HİSAR ve SİPER gibi milli hava savunma sistemlerinin yüksek süratli manevra yapan tehditlere karşı test edilmesi.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Fırlatma ve Dağıtım Platformları"
        P1["ANKA-3 Hayalet İnsansız Savaş Uçağı"]
        P2["AKSUNGUR / ANKA Ağır MALE SİHA"]
        P3["Kara Konuşlu Katapult & Roket Destek (RATO)"]
    end
    subgraph "SÜPER ŞİMŞEK Görev Mimarisi"
        S1["Turbojet İtki Sistemi (Mach 0.8+)"]
        S2["Otonom Rota & Sayısal Görev Bilgisayarı"]
        S3["KEMENT Taktik Veri Bağı"]
    end
    subgraph "Modüler Faydalı Yük Konfigürasyonu"
        C1["Sahte Hedef: Radar İzi Simülatörü (Lünberg Lensi)"]
        C2["Elektronik Harp: Minyatür RF Karıştırıcı Pod"]
        C3["Kamikaze: Parçacık Tesirli Harp Başlığı"]
    end
    P1 --> S1
    P2 --> S1
    P3 --> S1
    S1 --> S2 --> S3
    S2 --> C1
    S2 --> C2
    S2 --> C3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] Temel Aerodinamik ve Gövde Tasarımı
- [x] Turbojet İtki Entegrasyonu
- [x] Havadan Salım Testleri (AKSUNGUR üzerinden)
- [x] Süper Şimşek Otonom Uçuş ve Hedef Takip Testleri
- [ ] Elektronik Harp ve Kamikaze Başlığı Canlı Atış Kalifikasyonu
- [ ] Seri Üretim ve Filo Entegrasyonu

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
