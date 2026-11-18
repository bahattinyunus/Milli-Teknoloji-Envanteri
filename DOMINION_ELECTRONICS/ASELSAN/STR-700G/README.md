# 📡 Proje: ASELSAN STR-700G (Hava Savunma ve Topçu Tespit Radar Sistemleri)

<div align="center">

[![TRL](https://img.shields.io/badge/TRL-9_Envanterde_&_Saha_Kanıtlı-00E676?style=for-the-badge&logo=shield&logoColor=white)](../../../docs/TRL_GUIDE.md)
[![Dominion](https://img.shields.io/badge/DOMINION-ELECTRONICS-00ff88?style=for-the-badge&logo=cpu&logoColor=black)](../../README.md)
[![Üretici](https://img.shields.io/badge/ÜRETİCİ-ASELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/DURUM-Seri_Üretim_&_TSK_Envanterinde-brightgreen?style=for-the-badge)]()

</div>

<p align="center">
  <img src="../../../_ASSETS/platforms/ERALP.jpg" alt="ASELSAN Silah Tespit ve Hava Savunma Radar Ailesi" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

> **Geliştirici:** ASELSAN (Radar ve Elektronik Harp Sistemleri - REHİS Sektör Başkanlığı)  
> **Sınıf:** Yeni Nesil GaN AESA Silah Tespit Radarı (STR) ve Alçak İrtifa Hava Gözetleme Radarı  
> **Stratejik Önem:** Düşman topçu, havan ve çok namlulu roketatar (ÇNRA) mermilerini havadayken yakalayıp atış yapılan mevziyi saniyeler içinde hesaplayarak FIRTINA II obüslerine karşı-batarya atış koordinatı aktaran taktik radar kalkanı.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik

**ASELSAN STR (Silah Tespit Radarı)** ailesi, muharebe sahasında dost birliklerin üzerine ateşlenen havan, top ve roket mühimmatlarını henüz havada uçuş halindeyken tespit eden, balistik yörüngesini geriye doğru hesaplayarak **düşman silahının ateşlendiği noktayı (Origin Point)** ve **merminin düşeceği noktayı (Impact Point)** saniyeler içinde belirleyen aktif faz dizinli (AESA) radar sistemidir.

Elde edilen düşman mevzi koordinatları, **ADOP-2000** (Ateş Destek Otomasyon Sistemi) üzerinden anında dost **FIRTINA II** obüslerine ve **ÇNRA** bataryalarına aktarılır; böylece düşman topçusu henüz mevzi değiştiremeden karşı-batarya ateşiyle imha edilir. Aynı zamanda merminin düşeceği üs bölgesindeki personele erken ikaz (C-RAM uyarısı) vererek can kaybını önler.

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Radar Tipi** | S-Bant GaN Aktif Faz Dizinli (AESA) Silah Tespit Radarı | Elektronik taramalı yüksek hızlı hüzme yönlendirme |
| **Tespit Menzili** | 100+ Kilometre (Topçu ve Roket Mühimmatı) | Havan, Obüs ve ÇNRA balistik yörünge takibi |
| **Kapsama Açısı** | 90° Sektör / 360° Döner Mod Operasyonu | Elektronik ve mekanik hibrit tarama |
| **Çalışma Modları** | Düşman Silah Tespiti + Dost Topçu Tanzimi | Dost mermilerin hedefe düşüş sapmasını düzeltme |
| **Ağ Entegrasyonu** | ADOP-2000, HAKİM ve Çelik Kubbe C-RAM Ağı | Otomatik karşı-batarya ateş tahsisi |
| **Taşıyıcı Platform** | 6x6 / 8x8 Taktik Tekerlekli Araç (10 Dakikada Kurulum) | Yüksek hareket kabiliyeti ve "At-ve-Kaç" bekası |

---

## 🧩 Alt Sistemler ve Aviyonik / Elektronik Entegrasyonu

```mermaid
flowchart LR
    subgraph THREAT["Düşman Ateş Desteği"]
        ENEMY_ART["Düşman Obüs / Havan / ÇNRA Atışı"]
    end

    subgraph STR_RADAR["ASELSAN STR AESA Radarı"]
        TRACK["Havada Mermi Yörünge Takibi"]
        CALC["Atış Noktası & Düşüş Noktası Hesabı"]
    end

    subgraph RESPONSE["Karşı-Batarya & Erken İkaz"]
        WARN["Üs Bölgesi C-RAM Siren & Sığınak İkazı"]
        ADOP["ADOP-2000 Otomatik Hedef Aktarımı"]
        FIRTINA["FIRTINA II / TRG-230 Karşı-Batarya İmhası"]
    end

    ENEMY_ART --> TRACK --> CALC
    CALC --> WARN
    CALC --> ADOP --> FIRTINA
```

- **Dost Topçu Atış Tanzimi:** Dost obüslerin attığı mermilerin hedefin ne kadar sağına/soluna düştüğünü havada ölçerek ikinci atışın tam hedefe oturmasını sağlar.
- **Yüksek Elektronik Harp Direnci (ECCM):** Yan kulak bastırma ve frekans çevikliği sayesinde düşman radar karıştırıcılarından etkilenmeden görev yapar.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi

1. **Karşı-Batarya Harbi (Counter-Battery):** Sınır ötesi harekatlarda dost üs bölgelerine roket veya havan atan terör/düşman mevzilerinin saniyeler içinde tespit edilip ateş altına alınması.
2. **Üs Bölgesi Erken İkaz (C-RAM):** Mermi düşmeden 15-30 saniye önce alarm vererek personelin koruganlara geçmesini ve KORKUT/GÜRZ sistemlerinin o sektöre yönelmesini sağlama.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

- **Mevcut Durum:** `TRL 9` (Türk Silahlı Kuvvetleri envanterinde sınır hattı ve sınır ötesi harekat bölgelerinde aktif olarak görev yapmaktadır).
- [x] AESA anten mimarisi ve balistik kestirim algoritmalarının doğrulanması
- [x] TSK Kara Kuvvetleri Komutanlığı'na seri teslimatlar ve muharebe sahası kanıtı
- [ ] Hava hedefleri ve mini İHA tespit modlarının birleştirildiği Çok Maksatlı Radar (ÇMR) evrimi

---

## 🔗 İç Dizin Navigasyonu

[⬅️ Üst Dizine (ASELSAN)](../README.md) | [🏛️ Dominion Hub (DOMINION_ELECTRONICS)](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
