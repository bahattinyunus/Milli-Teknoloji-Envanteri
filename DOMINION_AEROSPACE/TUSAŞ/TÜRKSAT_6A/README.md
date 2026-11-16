# 🛰️ Proje: TÜRKSAT 6A (Türkiye'nin İlk Yerli Haberleşme Uydusu)

[![TRL](https://img.shields.io/badge/TRL-8_Yörüngede_Test_ve_Devreye_Alma-blue?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TUSAŞ_TÜBİTAK_ASELSAN_CTECH-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Yörüngeye_Fırlatıldı_Testler_Sürüyor-green?style=for-the-badge)](README.md)

<div align="center">
  <img src="../../../_ASSETS/aerospace_icon.png" alt="DOMINION AEROSPACE" width="100"/>
</div>

![TÜRKSAT 6A Yerli Haberleşme Uydusu](https://www.tusas.com/uploads/2021/03/turksat6a-1.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
TÜRKSAT 6A, Türkiye'nin uzay ve haberleşme teknolojilerinde tam bağımsızlık vizyonunun simgesi olan ilk yerli ve milli jeosenkron (GEO) haberleşme uydusudur. Ulaştırma ve Altyapı Bakanlığı ile TÜRKSAT A.Ş. desteğinde; TUSAŞ, TÜBİTAK UZAY, ASELSAN ve CTECH konsorsiyumu tarafından geliştirilen uydu, Türkiye'yi dünyada haberleşme uydusu üretebilen 11 ülkeden biri yapmıştır. 42° Doğu yörüngesinde konuşlanarak Türkiye'nin yanı sıra Avrupa, Kuzey Afrika, Orta Doğu ve Güney Asya'yı kapsayan geniş bir coğrafyada kesintisiz televizyon yayını, veri transferi ve milli güvenli askeri haberleşme imkanı sunmaktadır.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Yörünge Tipi ve Konumu** | Jeosenkron Yer-Sabit Yörünge (GEO - 42° Doğu) |
| **Yörünge İrtifası** | 35.786 km |
| **Fırlatma Kütlesi** | 4.250 kg |
| **Faydalı Yük Kapasitesi** | 16 Ku-Bant Aktarıcı (Transponder) + 4 Yedek; 2 X-Bant Aktarıcı (Askeri) |
| **Faydalı Yük Gücü** | 7.5 kW elektrik gücü (Güneş panelleri) |
| **Tasarım Ömrü** | 15+ yıl |
| **Kapsama Alanı** | Türkiye, Avrupa, Orta Doğu, Kuzey Afrika, Hindistan ve Güneydoğu Asya |
| **İtki Sistemi** | Hibrit İtki (Kimyasal Apogee Motoru + Milli Elektrikli İtki HALE-3000) |
| **Entegrasyon Tesisi** | TUSAŞ USET (Uzay Sistemleri Entegrasyon ve Test Merkezi - Ankara) |
| **Fırlatma Aracı** | SpaceX Falcon 9 (8 Temmuz 2024 Fırlatması) |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Haberleşme Faydalı Yükü:** ASELSAN tarafından geliştirilen Ku-Bant ve güvenli X-Bant askeri transponder süiti.
- **Telemetri & Telekomut:** CTECH tarafından geliştirilen S-Bant ve X-Bant güvenli yer kontrol haberleşme terminalleri.
- **Yönelim ve Yörünge Kontrol Sistemi (AOCS):** TÜBİTAK UZAY tarafından geliştirilen yıldız izlerler, güneş algılayıcıları ve yüksek torklu tepki tekerleri.
- **Gövde & Yapısal Sistem:** TUSAŞ tarafından üretilen kompozit ve metalik yapısal paneller, termal kontrol battaniyeleri ve güneş paneli açılma mekanizmaları.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Milli Uydu Haberleşmesi & TV Yayını:** Milyonlarca haneye ultra yüksek çözünürlüklü televizyon yayını ve internet omurgası desteği.
- **Güvenli Askeri Haberleşme:** TSK unsurlarının okyanus aşırı ve sınır ötesi operasyonlarda kriptolu ve karıştırmaya dayanıklı uydu haberleşme ağı.
- **Afet Haberleşmesi:** Deprem, tsunami ve felaket anlarında karasal baz istasyonları çökse dahi kesintisiz acil durum veri linki sağlama.
- **Kapsama Genişletme:** Türkiye'nin uydu kapsama alanına Hindistan ve Güneydoğu Asya'yı ekleyerek 5 milyar nüfusa erişim sağlama.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Konsorsiyum & İş Paylaşımı"
        T1["TUSAŞ: Yapısal Gövde, Termal & Güneş Panelleri"]
        T2["TÜBİTAK UZAY: AOCS, Yazılım & Güç Sistemleri"]
        T3["ASELSAN: Ku/X-Bant Haberleşme Faydalı Yükü"]
        T4["CTECH: Telemetri & Telekomut Sistemleri (TTC)"]
    end
    subgraph "Uzay Aracı Alt Sistemleri"
        S1["35.786 km Jeosenkron Yörünge (42° Doğu)"]
        S2["Hibrit Kimyasal / Elektrikli İtki Motoru"]
        S3["16+4 Ku-Bant & 2 X-Bant Transponderlar"]
    end
    subgraph "Kapsama Alanı & Kullanıcılar"
        U1["TSK Güvenli Askeri Haberleşme Şebekesi"]
        U2["Sivil TV Yayını & Genişbant İnternet"]
        U3["Avrupa, Orta Doğu, Kuzey Afrika & Hindistan"]
    end
    T1 --> S1
    T2 --> S2
    T3 --> S3
    T4 --> S1
    S3 ==> U1
    S3 ==> U2
    S1 ==> U3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] Sistem Seviyesi Tasarım ve Test Modeli (TM) Üretimi
- [x] Isıl Yapısal Model (STM) ve Mühendislik Modeli (EM) Testleri
- [x] USET Tesisinde Uçuş Modeli (FM) Montajı ve Titreşim/Akustik Testleri
- [x] SpaceX Falcon 9 Roketi ile Başarılı Fırlatma (8 Temmuz 2024)
- [x] 42° Doğu Yörüngesine İlerleme ve Yörünge Testleri (In-Orbit Testing)
- [ ] Tam Ticari ve Operasyonel Hizmete Giriş (TRL 8 -> TRL 9)

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
