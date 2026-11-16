# 🪖 Proje: ASELSAN TULGAR (Kaska Monteli Gösterge Sistemi - HMDS)

[![TRL](https://img.shields.io/badge/TRL-8_Uçuş_Doğrulaması-yellowgreen?style=for-the-badge&logo=shield)

<p align="center">
  <img src="https://www.aselsan.com.tr/uploads/tulgar.jpg" alt="TULGAR" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](https://www.aselsan.com)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-ASELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Entegrasyon_ve_Uçuş_Testi-brightgreen?style=for-the-badge)](#)

<div align="center">
  
</div>

> **Geliştirici:** ASELSAN  
> **Sınıf:** 5. Nesil Kaska Monteli Entegre Gösterge ve Nişangah Sistemi (HMDS)  
> **Stratejik Önem:** KAAN ve modern jet pilotlarına kokpit içi panellere bakma zorunluluğunu ortadan kaldıran, uçağın gövdesini saydamlaştırarak 360° durumsal farkındalık ve kafa hareketiyle füze kitleme kabiliyeti kazandıran yerli aviyonik vizyon sistemi.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
ASELSAN TULGAR, beşinci nesil savaş uçaklarının (başta KAAN Milli Muharip Uçak olmak üzere) yüksek dinamizmli hava muharebesi senaryolarında pilotun reaksiyon süresini saniyelerden milisaniyelere indiren yüksek teknolojili bir Kaska Monteli Gösterge Sistemidir (HMDS). Klasik uçaklardaki Head-Up Display (HUD) cihazını tamamen ortadan kaldıran TULGAR; uçağın hız, irtifa, hücum açısı gibi temel seyrüsefer bilgilerini ve sensör füzyonu ile elde edilen radar, FLIR ve füze ikaz verilerini pilotun vizörüne yüksek kontrastlı renkli mikro-ekranlar vasıtasıyla yansıtır. Uçağın gövde dışı kameralarıyla (EOTS/TOYGUN ve DAS) senkronize çalışan hibrit kafa takip sistemi, pilot kafasını nereye çevirirse kokpit zeminini "saydamlaştırarak" uçağın altındaki veya arkasındaki hedefleri doğrudan görmesini sağlar.

```mermaid
flowchart TD
    subgraph Pilot_Kask_Birimleri["ASELSAN TULGAR Donanımı"]
        KASK["Karbon-Kompozit Ergonomik Kask Kabuğu"]
        DISP["Çift Kanallı Yüksek Parlaklıklı Renkli Sayısal Vizör"]
        HTS["Hibrit Kafa Takip Sensörleri (Optik + İnertial MEMS)"]
        NVG["Entegre Sayısal Gece Görüş Sensör Modülü"]
        KASK --- DISP
        KASK --- HTS
        KASK --- NVG
    end

    subgraph Uçak_Aviyonik_Merkezi["KAAN Aviyonik & Görev Bilgisayarı"]
        MC["Milli Görev Bilgisayarı"]
        TOYGUN["TOYGUN EOTS & Gövde İçi Kameralar"]
        DAS["Dağıtık Açıklıklı Kızılötesi Sensör Ağı (DAS)"]
        RADAR["MURAD AESA Radarı"]
    end

    subgraph Yüksek_Açılı_Füze_Güdümü["Off-Boresight Angajmanı"]
        BOZDOGAN["BOZDOĞAN Görüş İçi Hava-Hava Füzesi (HOBS)"]
        GOKDOGAN["GÖKDOĞAN Görüş Ötesi Hava-Hava Füzesi"]
    end

    HTS ==>|Kafa Açısı & Bakış Doğrultusu (LOS)| MC
    TOYGUN & DAS & RADAR ==>|Sensör Füzyon Görüntüsü| MC
    MC ==>|Sentetik Görüş & Taktik Hedefleme| DISP
    MC ==>|Nişan Hattı Koordinatı| BOZDOGAN
    MC ==>|Nişan Hattı Koordinatı| GOKDOGAN
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Görüntü Teknolojisi** | Çift Renkli Sayısal Mikro-Ekran / Geniş Açı Vizöre Yansıtma |
| **Görüş Alanı (FoV)** | 40° Yatay x 30° Dikey Geniş Görüş Açısı |
| **Kafa Takip Hassasiyeti** | < 1 miliradyan açısal doğruluk (Optik Kamera + Dahili IMU Hibrit Takip) |
| **G-Kuvveti Dayanımı** | -3G ila +9G Ani Manevra Yükleri Altında Tam Kararlılık |
| **Kask Malzemesi** | Aramid & Karbon Fiber Güçlendirilmiş Ultra Hafif Kompozit |
| **Ağırlık Merkezi** | Pilot boyun kaslarını yormayan, pilot kafa taramasına özel optimize ağırlık dağılımı |
| **Gece Görüş Entegrasyonu** | Vizöre entegre dijital gece görüş sensörü (harici ağır gece gözlüğü gerektirmez) |
| **Oksijen & Kask İçi İletişim**| KBRN filtre uyumlu entegre maske ve gürültü önleyici aktif kulaklık mimarisi |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Off-Boresight (Eksen Dışı) Füze Kitleme:** Pilotun uçağın burnunu hedefe çevirmesine gerek kalmadan, yalnızca düşman jetine bakarak BOZDOĞAN hava-hava füzesini kitleyip ateşleyebilmesi.
- **Saydam Gövde ve DAS Görüntü Bindirme:** Gövde çevresindeki termal kameraların görüntüsünü kask vizöründe birleştirerek gece uçuşunda dahi yer yüzeyini ve dost/düşman unsurları 360 derece kesintisiz görme.
- **Düşman Radar & Tehdit Uyarı Sembolojisi:** RWR ve Füze İkaz Sistemleri tarafından algılanan bir tehdit yaklaşırken vizörde kırmızı yön oku ve sesli yönlendirme ile anında pilotu uyarma.
- **Yapay Zeka Destekli Taktik Katman:** Hava hedeflerinin dost, düşman veya tarafsız olduğu bilgisini vizörde otomatik renk kodlarıyla (yeşil/kırmızı/sarı) doğrudan hedefin üzerinde etiketleme.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **İt Dalaşı (Dogfight) ve Yüksek G Manevraları:** Dar açı dönüş manevralarında pilot kafasını serbestçe çevirerek düşmanı gözden kaçırmaz ve anında füze angajmanı kurar.
- **Gece Alçak İrtifa Sızma ve Yer Taarruzu:** Entegre gece görüş ve sentetik FLIR bindirmesi sayesinde dağlık coğrafyada sıfır görüşte bile yer engebelerini görerek güvenle uçuş.
- **Ağ Merkezli Takım Uçuşu:** Lider pilotun baktığı koordinatı veri bağı üzerinden koldaki diğer uçakların kasklarına ve KIZILELMA/ANKA-3 SİHA'larına anında aktarma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 8 (Uçuş Testleri ve Platform Entegrasyonu Doğrulandı)**
- [x] Özel Pilot Ergonomi ve Kask Kabuğu Tasarım Kalifikasyonu
- [x] Laboratuvar ve Santrifüj Yüksek-G Dayanıklılık Testleri
- [x] F-16 ÖZGÜR Platformunda Ön Uçuş ve Entegrasyon Doğrulamaları
- [x] KAAN Uçuş Test Programı Kokpit Sistemlerine Tam Entegrasyon
- [ ] Seri Üretim ve Tüm Beşinci Nesil Jet Filolarına Standart Donanım Dağıtımı

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
