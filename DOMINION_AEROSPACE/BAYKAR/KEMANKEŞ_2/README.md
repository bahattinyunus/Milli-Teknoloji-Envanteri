# 🎯 Proje: Bayraktar KEMANKEŞ 2 (Yeni Nesil Mini Seyir Füzesi)

[![TRL](https://img.shields.io/badge/TRL-7_Prototip_Doğrulandı-orange?style=for-the-badge&logo=target&logoColor=white)](../../../docs/TRL_GUIDE.md)
[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00b4d8?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/ÜRETİCİ-BAYKAR-0052CC?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/DURUM-Uçuş_ve_Vuruş_Testlerinde-blue?style=for-the-badge&logo=shield&logoColor=white)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/KEMANKES_2.jpg" alt="KEMANKEŞ 2" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>


## 🛡️ Stratejik Tanım & Doktriner Öncelik
**Bayraktar KEMANKEŞ 2**, Bayraktar TB2, TB3, AKINCI ve KIZILELMA gibi insansız muharip hava platformlarından salınabilen, jet motoru tahrikli, yapay zeka destekli optik güdüm mimarisine sahip yeni nesil bir mini akıllı seyir füzesidir.

KEMANKEŞ 1'e kıyasla artırılmış menzil, daha yüksek transonik seyir sürati, büyütülmüş 20 kg harp başlığı ve düşük radar kesit alanı (RCS) sağlayan açılı kompozit gövdesiyle öne çıkar. Düşman elektronik karıştırma şemsiyesinin en yoğun olduğu ortamlarda dahi yerleşik derin öğrenme algoritmalarıyla kara hedeflerini otonom olarak teşhis edip takip eden KEMANKEŞ 2, hava savunma koridorlarını yararak derinlikteki stratejik radarları, komuta sığınaklarını ve lojistik merkezleri nokta atışıyla imha eder.

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Sınıfı** | Yeni Nesil Yapay Zeka Destekli Mini Seyir Füzesi | Havadan salınan stand-off taarruz füzesi |
| **Operasyonel Menzil** | 200+ km | Düşman SAM menzili dışından güvenli taarruz |
| **Uçuş Süresi / Havada Kalış** | ~1 Saat | Hedef sahasında otonom seyrüsefer ve teşhis |
| **Tahrik Ünitesi** | İleri Seviye Sıvı Yakıtlı Mini Turbojet Motoru | Kompozit hava alıklı entegre jet itkisi |
| **Seyir / Dalış Sürati** | 0.6+ Mach / Terminal Safhada Yüksek Dalış Hızı | Hava savunma önleme süresini minimize eder |
| **Harp Başlığı** | ~20 kg Yüksek İnfilaklı Zırh Delici / Parçacıklı | Güçlendirilmiş beton ve zırhlı hedeflere etkili |
| **Güdüm Mimarisi** | Yapay Zeka Destekli Optik Arayıcı + ANS / KKS | Tam otonom AI-ATR görüntü tabanlı kilitlenme |
| **Radar İzi (RCS)** | Düşük Görünürlüklü Açılı Kompozit Tasarım | Radar tespitini geciktiren gövde geometrisi |
| **Taşıyıcı Platformlar** | Bayraktar TB2, TB3, AKINCI, KIZILELMA | Çoklu SİHA ve İnsansız Savaş Uçağı uyumu |

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Gelişmiş AI-ATR (Otomatik Hedef Tanıma):** Milyonlarca askeri araç ve radar görseliyle eğitilmiş derin öğrenme modelleri; füzenin insan müdahalesi olmadan hedefi teşhis edip kilitlenmesini sağlar.
- **Termal / Gündüz Çift Modlu Optik Sensör:** Gece, sis, duman ve zorlu atmosferik koşullarda termal imza üzerinden hedef ayrımı.
- **Kriptolu Sürü Veri Bağı:** Çoklu fırlatılan KEMANKEŞ 2 mühimmatlarının birbirleriyle ve ana platformla haberleşerek hedef paylaşımı yapabilmesi.
- **Anti-Jamming Donanımlı ANS:** Kasıtlı GPS yanıltma ve karıştırma bölgelerinde ataletsel referanslarla rotadan sapmama garantisi.

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Sürü Halinde Hava Savunma Doyurma:** Tek bir AKINCI veya KIZILELMA'dan bırakılan 4 adet KEMANKEŞ 2'nin hedef bataryaya farklı açılardan eşzamanlı dalışı.
- **Gizli Gövde İçi Salım (KIZILELMA Entegrasyonu):** KIZILELMA'nın dahili silah yuvasından stealth profilde fırlatılarak radar izi bırakmadan hedefi imha etmesi.
- **Yüksek Öncelikli Mobil Hedef İmhası:** Hareket halindeki mobil füze rampaları, radar istasyonları ve komuta kontrol tırlarının tespiti ve imhası.

## 📐 Mimari ve Görev Akış Şeması

```mermaid
flowchart TD
    subgraph Salım_Platformu ["İleri Muharip Platformlar"]
        K1["Bayraktar KIZILELMA / AKINCI / TB3"] --> REL["Pylon veya Dahili Yuvadan Bırakış"]
        REL --> JET["Mini Turbojet Ateşlemesi & Kanat Açılımı"]
    end

    subgraph Otonom_Seyir ["Stealth Seyir ve Sürü Koordinasyonu"]
        JET --> SEY["Düşük RCS Açılı Gövde ile 200+ km Seyir"]
        SEY --> COM["Sürü Algoritması ve Hedef Dağıtımı"]
    end

    subgraph Hedef_Tespit_Ve_Vurus ["Yapay Zeka Hedef Tanıma & Terminal Vuruş"]
        COM --> ATR["Derin Öğrenme AI-ATR Optik Arayıcı"]
        ATR --> TRG["Düşman SAM Radarı / Sığınak Kilitlenmesi"]
        TRG --> TERM["20 kg Harp Başlığı ile Cerrahi İmha"]
    end
```

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye: TRL 7 (Operasyonel Ortamda Prototip Doğrulandı)**
- [x] Aerodinamik Gövde Tasarımı ve Rüzgar Tüneli Doğrulamaları
- [x] Mini Turbojet Motoru Yer ve Statik İtki Testleri
- [x] 2024 Yılı Başarılı İlk Uçuş ve Hedef Vuruş Test İcrası
- [ ] Çoklu Mühimmat ile Sürü Angajman Gösterimleri
- [ ] KIZILELMA Dahili İstasyon Uçuş Ayrılma Testleri
- [ ] Seri Üretim Hattının Devreye Alınması

---
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
