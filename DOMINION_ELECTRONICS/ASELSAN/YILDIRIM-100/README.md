# ⚡ Proje: ASELSAN YILDIRIM-100 (Yönlendirilmiş Kızılötesi Karşı Tedbir Sistemi - DIRCM)

[![TRL](https://img.shields.io/badge/TRL-8_Kalifiye_Edilmiş-yellowgreen?style=for-the-badge&logo=shield)](https://www.aselsan.com)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-ASELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Platform_Entegrasyonunda-brightgreen?style=for-the-badge)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/YILDIRIM-100.jpg" alt="ASELSAN YILDIRIM-100" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

<div align="center">
  
</div>

> **Geliştirici:** ASELSAN  
> **Sınıf:** Havadan Yönlendirilmiş Kızılötesi Karşı Tedbir Sistemi (DIRCM - Directed Infrared Countermeasure)  
> **Stratejik Önem:** Helikopterleri, nakliye ve VIP uçaklarını alçak irtifada ölümcül tehdit oluşturan omuzdan atılan kızılötesi arayıcı başlıklı füzelere (MANPADS) karşı yüksek güçlü yönlendirilmiş lazer ışınıyla körleyerek bertaraf eden milli savunma kalkanı.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
ASELSAN YILDIRIM-100, hava araçlarının beka kabiliyetini en üst seviyeye çıkarmak amacıyla tasarlanmış yeni nesil bir DIRCM (Yönlendirilmiş Kızılötesi Karşı Tedbir) sistemidir. Geleneksel koruma sağlayan piroteknik işaret fişekleri (flare) modern çok spektrumlu akıllı füze arayıcı başlıklarına karşı yetersiz kalabilmekte ve sınırlı sayıda taşınabilmektedir. YILDIRIM-100; elektro-optik füze ikaz sensörlerinden aldığı uyarı ile füzeyi mikrosaniyeler içinde tespit edip kilitlenir ve taretindeki çok bantlı lazer ışınını doğrudan füzenin optik arayıcı başlığına odaklar. Arayıcı başlık detektörünü "körleştirip" sahte hedef açıları üreterek füzenin hava aracından tamamen sapmasını sağlar. Uçakta elektrik gücü bulunduğu sürece sınırsız sayıda füzeye karşı kesintisiz savunma sunar.

```mermaid
flowchart TD
    subgraph Tehdit_Füzesi["Düşman Tehdidi"]
        MANPADS["MANPADS Isı Güdümlü Füze (IR / UV / Dual Band)"]
    end

    subgraph YILDIRIM100_Sistemi["ASELSAN YILDIRIM-100 DIRCM Mimarisi"]
        direction TB
        MWS["Füze İkaz Sistemi Sensörleri (FİS / UV & IR Sensörler)"]
        CCU["Merkezi Karşı Tedbir Kontrol ve Tehdit Algılama Bilgisayarı"]
        GIMBAL["Ultra Hızlı Çift Eksenli Lazer Yönlendirme Tareti"]
        LASER["Yüksek Güçlü Çok Bantlı Katı Hal Fiber Lazer Kaynağı"]
        TRK["Hassas Kızılötesi Hedef Takip Kamerası (Fine Tracker)"]
        
        MWS ==>|Tehdit İkazı & Kaba Koordinat| CCU
        CCU ==>|Taret Yönlendirme Emri| GIMBAL
        GIMBAL --- TRK
        TRK ==>|Hassas Açı Kilidi| CCU
        CCU ==>|Lazer Ateşleme Modülasyonu| LASER
        LASER ==>|Körletici Lazer Işını| GIMBAL
    end

    subgraph Korunan_Hava_Platformu["Hava Platformu"]
        HELI["T929 ATAK-2 / T625 GÖKBEY / S-70 Blackhawk / A400M"]
    end

    MANPADS -.->|Ateşleme & Motor Termal İzi| MWS
    GIMBAL ==x|Yüksek Güçlü Modüle Lazer Körlemesi| MANPADS
    YILDIRIM100_Sistemi === HELI
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Lazer Tipi** | Çok Bantlı Katı Hal Lazer / Modüle Fiber Lazer Kaynağı |
| **Hedef Seti** | 1., 2., 3. ve 4. Nesil Kızılötesi (IR / UV / Görüntüleyici IIR) Arayıcı Başlıklı MANPADS ve SAM Füzeleri |
| **Reaksiyon Süresi** | Füze fırlatılışından itibaren < 1 saniye içinde lazer kilitlenmesi ve angajman |
| **Kapsama Alanı** | 360° Azimut, -90° ila +45° Elevasyon (Gövde altı ve üstü çift taret opsiyonu) |
| **Taret Hızı ve Hassasiyeti** | Çok yüksek açısal ivmelenme, mikro-radyan seviyesinde optik nişan hassasiyeti |
| **Mühimmat Kapasitesi**| Sınırsız (Hava aracının elektrik jeneratöründen beslenir, flare gerektirmez) |
| **Soğutma Mimarisi** | Kapalı devre sıvı veya hava soğutmalı kompakt termal yönetim |
| **Platform Uyumluluğu** | ATAK-2 (T929), GÖKBEY (T625), C-130, A400M, Helikopter ve VIP Nakliye Filosu |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Füze İkaz Sistemi (FİS) Entegrasyonu:** ASELSAN elektro-optik/ultraviyole füze ikaz sensörleriyle milisaniye düzeyinde tam veri paylaşımı.
- **Akıllı Karıştırma Kodları (Jamming Codes):** Füzenin tarama retikülünü ve dedektör frekansını bozan özel dalga formu modülasyonları ile sahte manevra yaptırma.
- **Çift Taretli Mimari Desteği:** Büyük gövdeli uçaklar (A400M, C-130 vb.) için gövde altı ve üstüne konuşlandırılan taretlerin ortak kontrolü ile tam küresel koruma küresi.
- **RWR ve Chaff/Flare Dispenseri ile Entegre Karşı Tedbir:** DIRCM sistemi çalışırken gereksinim duyulduğunda eşzamanlı RF karşı tedbirlerle karma savunma koordinasyonu.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Alçak İrtifa İndirme ve Yakın Hava Desteği:** Taarruz ve genel maksat helikopterlerinin sıcak temas bölgelerine personel indirmesi sırasında pusu kuran MANPADS timlerini etkisizleştirme.
- **Taktik Nakliye ve İntikal Koruma:** Stratejik nakliye uçaklarının iniş ve kalkış tırmanış safhalarında havaalanı çevresinden gelebilecek omuzdan atılan füze tehditlerine karşı tam koruma.
- **VIP ve Hükümet Uçakları Kalkanı:** Uluslararası riskli hava sahalarında devlet başkanlığı ve diplomatik uçakların füze sabotajlarına karşı caydırıcı güvenliği.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 8 (Platform Seviyesi Kalifikasyon ve Uçuş Testleri Başarılı)**
- [x] Yüksek Güçlü Lazer Kaynağı ve Hassas Taret Mekaniği Kalifikasyonu
- [x] Laboratuvar Donanım-Çevrim İçi (HWIL) Simülatör Testlerinde Başarılı Körleme
- [x] Helikopter Üzerinde Yer ve Uçuş Dinamiği Entegrasyon Doğrulaması
- [ ] T929 ATAK-2 Ağır Taarruz Helikopteri Seri Üretim Paketine Entegrasyon
- [ ] A400M ve TUSAŞ C-130 Erciyes Filolarına Yaygın Donatım

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
