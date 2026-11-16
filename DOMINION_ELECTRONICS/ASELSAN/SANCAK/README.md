# 📻 Proje: ASELSAN SANCAK (Yeni Nesil Muhabere Elektronik Taarruz Sistemi)

[![TRL](https://img.shields.io/badge/TRL-9_Saha_Kanıtlanmış-success?style=for-the-badge&logo=shield)](https://www.aselsan.com)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-ASELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Aktif_Envanterde-brightgreen?style=for-the-badge)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/SANCAK.jpg" alt="ASELSAN SANCAK" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

<div align="center">
  
</div>

> **Geliştirici:** ASELSAN  
> **Sınıf:** Yeni Nesil V/UHF Taktik Muhabere Elektronik Taarruz Sistemi (REDET II Fazı)  
> **Stratejik Önem:** Yüksek hareket kabiliyetine sahip taktik birliklerin düşman telsiz şebekelerini karıştırma, sahte emir yayma ve muhabere istihbaratı toplama kabiliyeti.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
ASELSAN SANCAK, modern müşterek harekat sahasında düşman kuvvetlerinin komuta kontrol omurgasını oluşturan V/UHF taktik muhabere altyapısını felç etmek üzere geliştirilmiş milli yeni nesil Elektronik Taarruz (ET / Jamming) ve Elektronik Destek (ED / COMINT) platformudur. REDET-II programı kapsamında üretilen SANCAK; taktik tekerlekli zırhlı araç üzerine entegre edilmiş yüksek hareket kabiliyetiyle ön hat birliklerine refakat eder. Düşmanın frekans atlamalı (frequency hopping), kriptolu ve direkt dizi yayılı spektrum (DSSS) mimarisine sahip taktik telsiz şebekelerini mikrosaniyeler mertebesinde tespit edip yönünü kestirir (DF - Direction Finding); ardından dar ve geniş bant reaktif karıştırma teknikleriyle düşman haberleşmesini tamamen kesintiye uğratır veya sahte emir enjeksiyonuyla komuta zaafiyeti oluşturur.

```mermaid
flowchart TD
    subgraph Tehdit_Spektrumu["Tehdit Spektrumu (V/UHF)"]
        T1["Taktik Telsizler (30-512 MHz)"]
        T2["Frekans Atlamalı Linkler"]
        T3["Düşman Komuta Veri Ağları"]
    end

    subgraph SANCAK_Sistemi["ASELSAN SANCAK Platformu"]
        direction TB
        A1["Çok Elemanlı Dizin Anten ve RF Ön Uç"] --> S1["Sayusal Alıcı & İnterferometrik DF"]
        S1 --> P1["Gerçek Zamanlı Spektrum Analizörü & Sinyal Ayrıştırıcı"]
        P1 --> D1{"Tehdit Değerlendirme & Angajman Algoritması"}
        D1 -->|COMINT Dinleme/Kayıt| LOG["İstihbarat ve Kayıt Birimi"]
        D1 -->|Karıştırma Emri| JAM["Yüksek Güçlü Sayısal Modüle Karıştırıcı (DRFM/PA)"]
    end

    subgraph Karşı_Tedbir["Elektronik Taarruz Çıkışı"]
        JAM --> O1["Follower Jamming (Frekans Takipçi Karıştırma)"]
        JAM --> O2["Barrage / Smart Jamming (Seçici Alan Bastırma)"]
        JAM --> O3["Deception (Sahte Mesaj / Aldatma)"]
    end

    T1 -.-> A1
    T2 -.-> A1
    T3 -.-> A1
    O1 -.->|RF Baskılama| T1
    O2 -.->|RF Baskılama| T2
    O3 -.->|Aldatma| T3
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Çalışma Frekans Aralığı** | 30 MHz - 3000 MHz (VHF / UHF / Düşük SHF) |
| **Yön Kestirim Hassasiyeti** | < 1° - 2° RMS (Sayısal Korelasyonlu İnterferometre) |
| **Karıştırma Teknikleri** | Takipçi Karıştırma (Follower Jamming), Sayısal Modüle Gürültü, Nokta (Spot) & Süpürmeli (Sweep) Karıştırma, Sahte Mesaj Yayma |
| **Anlık Bant Genişliği** | Çok kanallı yüksek hızlı anlık spektrum tarama (Real-Time Wideband Processing) |
| **RF Çıkış Gücü** | Çoklu Kilowatt (kW) seviyesinde katı hal (SSPA) güç yükselteç dizini |
| **Taşıyıcı Platform** | 8x8 / 6x6 Taktik Tekerlekli Yüksek Zırh Korumalı Şasi (KBRN filtreli kabin) |
| **Reaksiyon Zamanı** | Milisaniye mertebesinde atlama hızındaki frekanslara dinamik kilitlenme |
| **Konuşlanma / Terk Süresi** | Hidrolik mast ve stabilizasyon ayakları ile < 5 dakika |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Sayısal RF Hafıza (DRFM) ve Sayısal Modülatör:** Düşman telsiz modülasyonunu anında kopyalayarak aynı dalga formunda hedef odaklı enerji yönlendirme.
- **Yüksek Hızlı İnterferometrik Anten Grubu:** Araç tavanında yükseltilebilir hidrolik mast üzerine konuşlu, 360° azimut kapsayan yön kestirim ve taarruz anten dizilimi.
- **Taktik Komuta ve C4I Entegrasyonu:** TSK Taktik Veri Ağı (TAYNET / KEMENT) ve HAKİM Hava/Kara Komuta Kontrol Sistemleri ile tam entegrasyon; müşterek elektronik harp koordinasyonu.
- **Elektronik Harp Destek (ED / COMINT) Kayıt Paketi:** Dinlenen telsiz konuşmalarını otomatik yazıya dönüştürme ve kriptolu sinyal kayıt kabiliyeti.
- **KORAL ve MİLKAR Birlikteliği:** Radar karıştırma yapan KORAL ve haberleşme karıştırma yapan MİLKAR/SANCAK sistemlerinin tek bir EH harekat merkezinden koordine edilmesi.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Sınır Ötesi Harekât Bastırması:** Düşman ileri hat karakolları ve komuta merkezlerinin taktik telsiz irtibatını felç ederek karşı saldırı koordinasyonunu engelleme.
- **Konvoy Refakati ve Alan Koruması:** Taktik zırhlı birlik intikallerinde geniş alan telsiz körleme şemsiyesi oluşturarak pusu koordinasyonunu kırma.
- **Sahte Emir ve Taktik Aldatma:** Düşman birliklerinin komuta şebekelerine sızıp sahte çekilme veya yanlış koordinat anonsları basarak muharebe düzenini bozma.
- **Hava Savunma Bataryası Muhabere İzolasyonu:** Düşman hava savunma radarları ile batarya kontrol merkezleri arasındaki telsiz/veri linki hatlarını kesintiye uğratma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 9 (Saha Kanıtlanmış Seri Üretim)**
- [x] REDET-II Fazı Kapsamında Tasarım, Prototipleme ve Kalifikasyon
- [x] TSK Envanterine Giriş ve Operasyonel Muharebe Testleri (2022+)
- [x] Sınır Güvenliği ve Muharebe Sahası Görevlerinde Fiili İcraat
- [ ] Yapay Zeka Destekli Bilişsel Elektronik Harp (Cognitive EW) Algoritma Güncellemesi
- [ ] Otonom İHA/SİHA Destekli İleri İletişim Karıştırma Röleleri ile Ağ Bütünlüğü

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
