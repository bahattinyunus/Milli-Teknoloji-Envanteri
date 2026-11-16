# 🦅 Proje: ASELSAN TOYGUN (5. Nesil Elektro-Optik Hedefleme Sistemi - EOTS)

[![TRL](https://img.shields.io/badge/TRL-7%2F8_Prototip_Doğrulandı-yellowgreen?style=for-the-badge&logo=shield)](https://www.aselsan.com)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-ASELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Entegrasyon_Aşamasında-orange?style=for-the-badge)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/TOYGUN.jpg" alt="TOYGUN" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

<div align="center">
  
</div>

> **Geliştirici:** ASELSAN  
> **Sınıf:** 5. Nesil Düşük Görünürlüklü Entegre Elektro-Optik Hedefleme Sistemi (EOTS)  
> **Stratejik Önem:** KAAN Milli Muharip Uçak, KIZILELMA ve insansız jet muhariplerinin gövde içine gömülü, radar izini bozmayan ve pasif olarak yüzlerce kilometre ötedeki hava ve kara hedeflerini lazerle işaretleyen optik kalbi.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
ASELSAN TOYGUN, 5. nesil stealth (düşük radar kesit alanına sahip) savaş uçaklarının harici pod taşımaksızın hava-hava ve hava-yer hedeflerini tespit, teşhis, otomatik takip ve lazerle işaretleme yapabilmesi için tasarlanmış gövde içi entegre Elektro-Optik Hedefleme Sistemidir (EOTS). F-35'in Lockheed Martin EOTS sistemine doğrudan yerli ve bağımsız bir alternatif olan TOYGUN; safir yüzeyli çok açılı optik penceresi sayesinde uçağın radar kesit alanını (RCS) artırmadan yüksek çözünürlüklü termal ve gündüz görüntüleme sağlar. Radar suskunluğu (EMCON) durumunda bile uçağın pasif kalarak düşman unsurlarını fark edilmeden vurmasına olanak tanır.

```mermaid
flowchart TD
    subgraph Aviyonik_Mimari["5. Nesil Aviyonik Entegrasyon (KAAN / KIZILELMA)"]
        MC["Milli Görev Bilgisayarı"]
        MURAD["MURAD AESA Radarı"]
        KARAT["KARAT Kızılötesi Arama-Takip (IRST)"]
        TULGAR["TULGAR Kaska Monteli Gösterge (HMDS)"]
    end

    subgraph TOYGUN_EOTS["ASELSAN TOYGUN EOTS"]
        direction TB
        W["Faceted Sapphire Düşük RCS Optik Pencere"]
        MWIR["Yüksek Çözünürlüklü MWIR / SWIR Termal Kamera"]
        TV["HD Renkli Gündüz Kamerası"]
        LTD["Diyod Pompalı Lazer Hedef İşaretleyici (LTD/LRF)"]
        STAB["Ultra Hassas Jiroskopik Stabilizasyon Birimi"]
        TRK["Yapay Zeka Destekli Çoklu Hedef İzleme Algoritması"]
        W --> MWIR & TV & LTD
        STAB --> W
        MWIR & TV --> TRK
    end

    subgraph Mühimmat_Güdümü["Hassas Güdüm & Angajman"]
        TOLUN["TOLUN Minyatür Bomba"]
        SOM["SOM-J Seyir Füzesi"]
        BOZDOGAN["BOZDOĞAN Görüş İçi Hava-Hava Füzesi"]
    end

    TOYGUN_EOTS <-->|Yüksek Hızlı Sayısal Optik Veri Hattı| MC
    MURAD -.->|Sensör Füzyonu İpucu| TOYGUN_EOTS
    KARAT -.->|Hava-Hava Pasif Veri Eşleme| TOYGUN_EOTS
    TOYGUN_EOTS ==>|Vizör Hedef Görüntüsü| TULGAR
    TRK ==>|Lazer Kodlama & Güdüm Koordinatı| TOLUN & SOM
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Konfigürasyon** | Gövde Altı Gömülü (Conformal / Internal EOTS Mimarisi) |
| **Optik Pencere** | Çok Yüzeyli Safir Cam (Düşük RCS ve Aerodinamik Sürtünme Koruması) |
| **Kızılötesi Sensör** | 3. Nesil Megapiksel MWIR (Orta Dalga Kızılötesi) ve SWIR Sensör |
| **Gündüz Görüntüleme** | Geniş Dinamik Aralıklı (HDR) Yüksek Çözünürlüklü Renkli TV |
| **Lazer Birimleri** | Göz Güvenli Lazer Mesafe Ölçer (ELRF), 1064 nm NATO Uyumlu Lazer İşaretleyici ve Aydınlatıcı |
| **Stabilizasyon Hassasiyeti** | < 5 mikro-radyan seviyesinde ultra hassas çok eksenli yalpa sönümleme |
| **Görüş Açıları** | Sürekli 360° azimut tarama ve derin irtifa elevasyon kapsaması |
| **Ağırlık & Hacim** | Hafifletilmiş titanyum/berilyum alaşım gövde, gövde içi kompakt hacim |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Sensör Füzyon İşlemcisi:** MURAD AESA radarı, KARAT IRST ve elektronik harp süiti ile entegre çalışarak uçağın taktik ekranına tek ve net bir hedef resmi aktarır.
- **TULGAR Kask Uyumu:** TOYGUN kamerasından alınan kızılötesi görüntü, pilotun kask vizörüne gerçek zamanlı bindirilerek gece şartlarında dahi pilotun uçağın altını saydam biçimde görmesini sağlar.
- **Dahili Lazer Aydınlatma & Nokta Takibi (Spot Tracker):** Dost unsurların (JTAC / Taktik İHA) yer işaretlediği lazer spotunu anında algılayıp silah sistemine hedef gösterir.
- **Milli Mühimmat Entegrasyonu:** SOM-J, TOLUN, TEBER, MAM serisi ve lazer güdümlü mühimmatların terminal safha hedefe kilitlenmesi için milimetrik koordinat üretir.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Derin Darbe ve Stealth Hava-Yer Görevi:** Düşman radar sahasına görünmeden sızıp hedef yerleşkesini, sığınakları ve kritik komuta merkezlerini pasif optik ile işaretleyip imha etme.
- **Radar Suskunluğunda (Passive Air-to-Air) Av:** AESA radarını açmadan düşman uçaklarının motor ısısını ve aerodinamik sürtünme sıcaklığını tespit edip hava-hava füzesi fırlatma.
- **Deniz Yüzey Hedeflerine Taarruz:** Deniz araçlarının silüetini optik olarak tanıma ve kıyı savunma füzelerini doğrudan köprüüstü veya mühimmat deposu gibi zayıf noktalara yönlendirme.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 7/8 (Prototip Laboratuvar ve Platform Kalifikasyon Testleri Aşamasında)**
- [x] Kritik Tasarım Fazı (CDR) ve Optomekanik Doğrulama
- [x] Zemin ve Aviyonik Sistem Entegrasyon Laboratuvar (SIL) Testleri
- [x] Lazer ve FLIR Sensör Kalifikasyonu
- [ ] KAAN Prototip Uçakları Üzerinde Uçuş Testleri
- [ ] Seri Üretim ve KIZILELMA Blok-3 Konfigürasyonuna Entegrasyon

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
