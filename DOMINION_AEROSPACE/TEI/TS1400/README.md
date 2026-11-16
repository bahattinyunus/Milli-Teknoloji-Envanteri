# 🚁 Proje: TEI-TS1400 Milli Turboşaft Helikopter Motoru

<div align="center">

[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00f2fe?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/%C3%9CRET%C4%B0C%C4%B0-TEI-orange?style=for-the-badge&logo=target&logoColor=white)](../README.md)
[![TRL](https://img.shields.io/badge/TRL-8%20(Helikopter%20U%C3%A7u%C5%9F%20Testlerinde)-00E676?style=for-the-badge&logo=speedtest&logoColor=black)](../../../docs/TRL_GUIDE.md)
[![Durum](https://img.shields.io/badge/DURUM-U%C3%A7u%C5%9F%20Testleri%20%2F%20Sertifikasyon%20Tamamlama-ff007f?style=for-the-badge&logo=shield&logoColor=white)](#)

<img src="../../../_ASSETS/aerospace_icon.png" width="120" alt="Aerospace Dominion">

</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
**TEI-TS1400**, Türkiye'nin özgün helikopteri TUSAŞ T625 GÖKBEY başta olmak üzere, T129 ATAK taarruz helikopteri ve yeni nesil döner kanatlı platformları yabancı motor lisans kısıtlamalarından tamamen kurtaran, Türkiye'nin ilk milli ve sertifikalı turboşaft motorudur. 1.470 şaft beygir gücü (SHP) kalkış ve tek motor arızası (OEI) durumunda 1.660 SHP acil durum gücü üreten bu devrimsel motor; tek kristal türbin kanatçıkları, ters akışlı yanma odası ve çift kanallı yedekli FADEC sistemi ile dünya helikopter motoru pazarındaki en modern ve rekabetçi tasarımlardan biridir.

---

## 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Motor Sınıfı** | Çift Şaftlı Serbest Güç Türbinli Turboşaft | Askeri & Sivil Havacılık Sertifikalı |
| **Kalkış Gücü (Take-Off)** | 1.470 SHP | Deniz seviyesi ve sıcak hava performansı |
| **Acil Durum Gücü (OEI - 30 sn)** | 1.660 SHP | Tek motor durduğunda güvenli uçuş gücü |
| **Sürekli Seyir Gücü** | 1.250 SHP | Ekonomik ve uzun menzilli uçuş modu |
| **Kuru Motor Ağırlığı** | ~160 kg | 9.2 shp/kg olağanüstü güç/ağırlık oranı |
| **Servis Tavanı** | 20.000 Feet | Yüksek dağlık arazi ve sıcak hava operasyonları |
| **Çıkış Şaft Devri** | 23.000 RPM (Redüksiyon Dişlisine Giriş) | Helikopter ana transmisyonuna yüksek tork aktarımı |
| **Kompresör Tipi** | 2 Kademeli Santrifüj Kompresör | Yüksek basınç oranı ve yabancı madde direnci |
| **Uygulama Platformları** | TUSAŞ T625 GÖKBEY, T129 ATAK, HÜRJET Varyantları | Genel maksat ve taarruz helikopterleri |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph Hava_Girisi["Hava Girişi ve Kompresyon"]
        IPS["Entegre Partikül Ayırıcı (IPS - Toz/Kum Filtresi)"]
        COMP1["1. Kademe Santrifüj Kompresör"]
        COMP2["2. Kademe Santrifüj Kompresör"]
        IPS --> COMP1
        COMP1 --> COMP2
    end

    subgraph Yanma_ve_Guc_Uretimi["Yanma ve Türbin Fazı"]
        REVERSE_BURN["Ters Akışlı Yanma Odası (Reverse-Flow)"]
        GAS_GEN_TURB["Gaz Jeneratör Türbini (Tek Kristal)"]
        FREE_POWER_TURB["Serbest Güç Türbini (Power Turbine)"]
        
        COMP2 --> REVERSE_BURN
        REVERSE_BURN --> GAS_GEN_TURB
        GAS_GEN_TURB --> FREE_POWER_TURB
    end

    subgraph Mekanik_Cikis["Şaft ve Transmisyon Aktarımı"]
        POWER_SHAFT["Ana Güç Şaftı (1.470 - 1.660 SHP)"]
        GEARBOX["Helikopter Ana Dişli Kutusu & Rotor"]
        FREE_POWER_TURB --> POWER_SHAFT
        POWER_SHAFT --> GEARBOX
    end

    subgraph Dijital_Beyin["Milli Aviyonik Motor Yönetimi"]
        FADEC_TS["TEI Çift Kanallı Bağımsız FADEC"]
        SENS_TS["TIT Sıcaklık & Tork Sensörleri"]
        SENS_TS --> FADEC_TS
        FADEC_TS --> REVERSE_BURN
    end
```

- **Ters Akışlı (Reverse-Flow) Yanma Odası:** Motorun boyunu kısaltarak ağırlık merkezini optimize eden ve türbin girişine son derece homojen sıcaklık dağılımı sağlayan aerotermal mimari.
- **Entegre Partikül Ayırıcı (IPS):** Çöl, dağlık ve tozlu arazilerde helikopterin kalkışı esnasında havaya kalkan kum taneciklerini motora girmeden dışarı atan santrifüj filtre sistemi.
- **Çift Kanallı Yedekli FADEC:** Herhangi bir elektriksel veya sensör arızasında milisaniyeler içinde yedek kanala geçerek motorun durmasını kesin olarak engelleyen tam sayısal motor kontrolü.

---

## 🎯 Operasyonel Görev Profili ve Entegrasyon

### 1. TUSAŞ T625 GÖKBEY Genel Maksat Helikopteri
GÖKBEY'in ambulans, arama kurtarma, VIP ve taktik nakliye görevlerinde yerli kalbi olarak yüksek sıcaklık ve irtifada tam performans uçuş sağlar.

### 2. T129 ATAK Taarruz Helikopteri Entegrasyonu
Mevcut yabancı motorların yerine geçerek ATAK'ın dost ve müttefik ülkelere yönelik ihracatında karşılaşılan tüm diplomatik engelleri ortadan kaldırır.

### 3. Deniz Konuşlu Helikopter Operasyonları
Korozyona dayanıklı nikel süperalaşımları ve tuzlu deniz havasına uygun kaplamalarıyla fırkateyn ve TCG ANADOLU pistlerinde sorunsuz çalışma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

```
[████████░░] TRL 8 - Helikoptere Entegre Edildi, Uçuş Testleri Başarıyla Sürüyor
```

- [x] **TRL 1-4:** SSB Turboşaft Motor Geliştirme Projesi (TMGP) sözleşmesi ve tasarım doğrulama.
- [x] **TRL 5-6:** İlk prototip montajı, çekirdek motor çalıştırması ve 1.500+ SHP güç rekoru.
- [x] **TRL 7:** 22 Nisan 2023 - GÖKBEY helikopteri ile TS1400 motorunun ilk tarihi test uçuşu.
- [x] **TRL 8:** İrtifa, tek motor arızası (OEI) simülasyonları ve zorlu hava koşulları uçuş testleri.
- [ ] **TRL 9:** Sivil Havacılık (SHGM / EASA) ve Askeri sertifikasyonların tamamlanarak seri üretime geçilmesi.

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
