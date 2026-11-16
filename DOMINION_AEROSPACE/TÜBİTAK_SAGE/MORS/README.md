# 💥 Proje: TÜBİTAK SAGE MORS (Modüler Oturmalı Akıllı Havan ve Mini Roket)

[![TRL](https://img.shields.io/badge/TRL-9_Envanterde_ve_Operasyonel-success?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TÜBİTAK_SAGE-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Aktif_Hizmette_ve_Seri_Üretimde-green?style=for-the-badge)](README.md)

<p align="center">
  <img src="../../../_ASSETS/platforms/MORS.jpg" alt="MORS" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![TÜBİTAK SAGE MORS Akıllı Mühimmat Sistemi](https://www.sage.tubitak.gov.tr/sites/default/files/mors.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
MORS (Modüler Oturmalı Roket ve Akıllı Havan Mühimmatı Ailesi), ön hat piyade birliklerinin, kara araçlarının ve insansız platformların (İHA, İKA) organik ateş gücünü cerrahi hassasiyet seviyesine çıkarmak üzere TÜBİTAK SAGE tarafından geliştirilen minyatür hassas güdümlü mühimmat sistemidir. Klasik havan mühimmatlarının düşük isabet oranını ve yüksek mühimmat sarfiyatını ortadan kaldıran MORS; gövdeye entegre açılır aerodinamik kontrol kanatçıkları, GPS/INS destekli akıllı burun tapası ve yarı aktif lazer arayıcı başlığı ile menzili iki katına çıkarırken dairesel sapmayı (CEP) 2 metrenin altına indirmektedir.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Mühimmat Kalibreleri** | 60 mm, 81 mm ve 120 mm havan uyumlu varyantlar |
| **Güdüm Tipi** | GPS / Sayısal INS + Terminal Yarı Aktif Lazer Güdümü (SAL) |
| **Vuruş Hassasiyeti (CEP)** | <2 metre (Cerrahi nokta atışı) |
| **Menzil Artışı** | Klasik havan mühimmatlarına kıyasla %80 - %120 menzil artışı (Açılır kanatlar ile süzülüş) |
| **Azami Menzil** | 81 mm için ~9 km | 120 mm için ~15+ km |
| **Harp Başlığı** | Yüksek İnfilaklı Parçacık Tesirli veya Zırh Delici Çukur İmla |
| **Tapa Seçenekleri** | Çarpmalı, Gecikmeli (Sığınak içi) ve Havada Parçalanmalı (Airburst) Yaklaşma Tapası |
| **Atıcı Platformlar** | Standart Havan Namluları, İnsansız Kara Araçları (İKA), Döner/Sabit Kanatlı SİHA'lar |
| **Kurulum ve Hazırlık** | Saniyeler içinde namluya sürülebilen tak-kullan modüler gövde |
| **Elektronik Koruma** | Kriptolu sinyal alımı ve karıştırmaya dirençli seyrüsefer |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Akıllı Burun Tapası:** Hassas zaman ayarlı ve lazer lekesi arayan minyatür optik algılayıcı ünitesi.
- **Açılır Aerodinamik Kanatçıklar:** Namludan çıkış anında merkezkaç ve yay kuvvetiyle açılan, süzülüş açısını kontrol eden mikro kontrol kanatları.
- **Minyatür IMU ve Mikroişlemci:** Aşırı yüksek fırlatma g-kuvvetlerine (15.000g+) dayanıklı sertleştirilmiş elektronik kart mimarisi.
- **Lazer Algılama Modülü:** İHA veya yer unsurlarının lazerle işaretlediği kodlanmış lekeye yüksek hızla yönelme yeteneği.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Cerrahi Piyade Desteği:** Meskun mahalde veya sarp dağlık arazide dost birliklerin hemen yakınındaki düşman mevzilerine tali hasarsız atış.
- **Sütre Gerisi Hedef İmhası:** Tepe arkasında veya mağara ağzında gizlenen roket/havan mevzilerini dik açılı terminal dalışla vurma.
- **İnsansız Sistem Entegrasyonu:** BARKAN, KAPGAN gibi İKA'lar ile BOYGA ve KARGU benzeri mini İHA'lardan bırakılarak hafif zırhlı hedefleri imha.
- **Hızlı Reaksiyonlu Karşı Batarya:** Düşman atış yaptıktan hemen sonra yer tespit radarı koordinatlarına ilk atımda tam isabetle karşılık verme.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Fırlatma ve Ayrılma Fazı"
        F1["Standart 60/81/120 mm Namlu veya İHA/İKA"]
        F2["15.000g Dayanımlı Sertleştirilmiş Gövde"]
        F3["Namludan Çıkışta Açılan Aerodinamik Kanatlar"]
    end
    subgraph "Uçuş Ortası Süzülüş"
        G1["Minyatür IMU / GPS ile Menzil Artırıcı Süzülüş"]
        G2["Havan Menzilinin 2 Katına Çıkartılması"]
    end
    subgraph "Terminal Güdüm ve İnfilak"
        T1["Yarı Aktif Lazer Arayıcı (SAL) ile Lekeye Kilitlenme"]
        T2["CEP < 2m Nokta Vuruşu"]
        T3["Programlanabilir Tapa (Airburst / Çarpma)"]
    end
    F1 --> F2 --> F3
    F3 --> G1 --> G2
    G2 --> T1 --> T2 --> T3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] Yüksek G Dayanımlı Elektronik Mimari Geliştirme
- [x] Açılır Kanat Mekanizması Namlu Çıkış Testleri
- [x] Lazer Güdüm Kiti ve Terminal Arayıcı Doğrulaması
- [x] Canlı Atışlı Hedef İmha Kalifikasyonları (CEP < 2m)
- [x] TSK ve Özel Kuvvetler Envanterine Giriş (TRL 9)
- [ ] Mini İHA / İKA Entegrasyonlarının Çeşitlendirilmesi

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
