# 🦅 Proje: SOM (Satha Atılan Orta Menzilli Seyir Füzesi Ailesi)

[![TRL](https://img.shields.io/badge/TRL-9_Muharebede_Kanıtlanmış_ve_Hizmette-success?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TÜBİTAK_SAGE_%26_ROKETSAN-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Aktif_Filolarda_ve_Seri_Üretimde-green?style=for-the-badge)](README.md)

<p align="center">
  <img src="../../../_ASSETS/platforms/SOM.jpg" alt="SOM" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![TÜBİTAK SAGE SOM Havadan Atılan Seyir Füzesi](https://www.sage.tubitak.gov.tr/sites/images/som_main.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
SOM (Satha Atılan Mühimmat), Türk Silahlı Kuvvetleri'nin düşman hava savunma şemsiyelerinin menziline girmeden (Stand-Off), yoğun korunan stratejik kara ve deniz hedeflerini yüksek hassasiyetle vurabilmesi için TÜBİTAK SAGE tarafından tasarlanan ve ROKETSAN tarafından seri üretimi gerçekleştirilen Türkiye'nin ilk milli seyir füzesi ailesidir. Kale Havacılık üretimi KTJ-3200 milli turbojet motoruyla donatılan platform; düşük radar kesit alanı (Stealth), arazi referanslı seyrüsefer (TRN/TERCOM), görüntü referanslı seyrüsefer (IBN), kızılötesi görüntüleyici (IIR) terminal arayıcı başlık ve çift yönlü KEMENT taktik veri bağı sayesinde hedefini santimetre hassasiyetiyle imha edebilmektedir.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Füze Tipi** | Hava-Yer / Hava-Deniz Hassas Seyir Füzesi (ALCM) |
| **Menzil** | 250+ km (Stand-off taarruz mesafesi) |
| **Maksimum Hız** | Mach 0.94 (Yüksek Subsonik) |
| **Motor** | Kale Havacılık KTJ-3200 Milli Turbojet Motoru (veya Safran TR40) |
| **Toplam Ağırlık** | ~600 kg (SOM-A/B) / ~500 kg (SOM-J) |
| **Harp Başlığı** | 230 kg Yüksek İnfilaklı Parçacık Tesirli veya Çift Kademeli Ardışık Delici (Tandem Penetrator) |
| **Güdüm Sistemi** | Ataletsel Seyrüsefer (INS) + GPS + Yeryüzü Referanslı Seyrüsefer (TRN) + Otomatik Hedef Algılama (ATA) |
| **Terminal Arayıcı** | Yüksek Çözünürlüklü Soğutmalı IIR (Kızılötesi Görüntüleyici Arayıcı Başlık) |
| **Veri Bağı** | KEMENT Taktik Veri Bağı (Uçuş ortası hedef güncelleme, yeniden hedeflendirme ve hasar tespiti) |
| **Taşıyıcı Platformlar** | F-16 PO-III/ÖZGÜR, F-4E 2020, KAAN, AKINCI, AKSUNGUR, KIZILELMA, ANKA-3 |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **IIR Terminal Arayıcı ve ATA:** Otomatik Hedef Algılama (ATA) yazılımı ile hafızasındaki 3 boyutlu hedef modeliyle görseli eşleştirerek yanıltıcı hedefleri ve sahte hedefleri eler.
- **TRN / IBN Yeryüzü Referanslı Seyrüsefer:** Radar altimetre ve sayısal harita verilerini eşleştirerek GPS sinyalinin tamamen kesildiği coğrafyalarda dahi vadi içlerinden radar kapsamasının altından gizlice ilerleme.
- **KEMENT Çift Yönlü Veri Bağı:** Füzenin kamerasındaki canlı görüntüyü pilotun veya komuta merkezinin ekranına aktarma; pilota hedef üzerinde vuruş noktasını değiştirme (örneğin binanın belirli bir penceresini seçme) yeteneği.
- **Gizlilik / Stealth Gövde:** Radar soğurucu geometrik hatlar ve kompozit kaplama ile hava savunma radarları tarafından çok geç tespit edilme.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Stratejik Komuta Merkezleri ve Radar Mevzileri:** SOM-B2 ardışık delici harp başlığı ile betonla güçlendirilmiş derin yeraltı sığınaklarını delip imha etme.
- **Kritik Altyapı ve Havalimanları:** SOM-A ve B1 varyantları ile düşman hangarlarını, mühimmat depolarını ve pist kavşaklarını felç etme.
- **Hareketli Su Üstü Harp (ASuW):** SOM-J ve SOM-B1 ile firkateyn, destroyer ve amfibi çıkarma gemilerine karşı IIR güdümle cerrahi su hattı vuruşu.
- **SİHA ile Derin Darbe:** AKINCI ve KIZILELMA SİHA'ları tarafından taşınarak pilot riski olmaksızın 250+ km derinlikteki düşman unsurlarına taarruz.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Seyrüsefer ve Uçuş Fazı"
        N1["Kale KTJ-3200 Turbojet Motoru (Mach 0.94)"]
        N2["INS / GPS + Yeryüzü Referansı (TRN/TERCOM)"]
        N3["Radar Altından Vadi İçi Gizli Süzülüş (Stealth Gövde)"]
    end
    subgraph "KEMENT Taktik Veri Bağı"
        L1["Canlı Hedef Görüntüsü Aktarımı (Downlink)"]
        L2["Uçuş Ortası Hedef Güncelleme / Görev İptali"]
    end
    subgraph "Terminal Hedefleme & Varyantlar"
        V1["SOM-A: GPS/INS Güdümlü Standart Harp Başlığı"]
        V2["SOM-B1: IIR Arayıcılı Hareketli Kara/Deniz Hedefleri"]
        V3["SOM-B2: İki Kademeli Ardışık Beton Delici Başlık"]
        V4["SOM-J: KAAN/F-35 Dahili İstasyon Uyumlu Kompakt Form"]
    end
    N1 --> N2 --> N3
    N3 --> L1 <--> L2
    L1 --> V1
    L1 --> V2
    L1 --> V3
    L1 --> V4
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] SOM-A ve SOM-B1 Tasarım, Atış Testleri ve Envanter Kabulü (2012)
- [x] SOM-B2 Ardışık Delici Başlık Geliştirme ve Kabul Testleri (2020)
- [x] Kale KTJ-3200 Yerli Turbojet Motoru Entegrasyonu ve Başarılı Canlı Atışı
- [x] AKINCI TİHA Üzerinden SOM Füzesi Test Atışları ve Tam İsabet
- [x] SOM-J Dahili İstasyon Seyir Füzesi Entegrasyon ve Atış Fazı
- [x] TSK Filolarında Muharebe Hazır ve Seri İmalat (TRL 9)

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
