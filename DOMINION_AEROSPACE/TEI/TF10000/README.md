# ✈️ Proje: TEI-TF10000 Art Yakıcılı Turbofan Motor

<div align="center">

[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00f2fe?style=for-the-badge&logo=spacex&logoColor=white)

<p align="center">
  <img src="https://www.tei.com.tr/uploads/tf10000.jpg" alt="TF10000" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](../../README.md)
[![Üretici](https://img.shields.io/badge/%C3%9CRET%C4%B0C%C4%B0-TEI-orange?style=for-the-badge&logo=target&logoColor=white)](../README.md)
[![TRL](https://img.shields.io/badge/TRL-6%20(Prototip%20Do%C4%9Frulama%20ve%20Test)-yellow?style=for-the-badge&logo=speedtest&logoColor=black)](../../../docs/TRL_GUIDE.md)
[![Durum](https://img.shields.io/badge/DURUM-Art%20Yak%C4%B1c%C4%B1%20Entegrasyonu%20%2F%20Geli%C5%9Ftirme-blue?style=for-the-badge&logo=shield&logoColor=white)](#)



</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
**TEI-TF10000**, Türkiye'nin geliştirdiği ilk askeri turbofan motor olan TF6000'in çekirdek mimarisi üzerine art yakıcı (Afterburner / Reheat) modülü eklenerek üretilen, 10.000 lbf sınıfı süpersonik jet motorudur. Bayraktar KIZILELMA-B insansız savaş uçağı ve TUSAŞ ANKA-3'ün süpersonik versiyonlarına ses hızının üzerinde (Mach 1.2+) sürat kazandırmak amacıyla geliştirilmektedir. Türkiye'nin 5. nesil milli muharip uçağı KAAN'ın yerli motoruna giden yoldaki en kritik teknolojik basamak olan TF10000; tek kristal türbin kanatçıkları, süperalaşım döküm ve yüksek sıcaklık art yakıcı geometrisiyle jet motoru liginde dev bir sıçramadır.

---

## 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Motor Mimarisi** | Düşük Bypasslı, Çift Şaftlı Art Yakıcılı Turbofan | Askeri Süpersonik İtki Ünitesi |
| **Kuru İtki (Dry Thrust)** | 6.000 lbf (~26.7 kN) | Art yakıcı kapalı ekonomik seyir gücü |
| **Art Yakıcılı İtki (Reheat)** | 10.000 lbf (~44.5 kN) | Süpersonik ivmelenme ve tırmanma gücü |
| **Bypass Oranı (BPR)** | ~1.08 | Yüksek hız ve kompakt kesit için optimize |
| **Türbin Giriş Sıcaklığı (TIT)** | 1.450+ °C | İleri termal bariyer kaplamaları (TBC) |
| **Kompresör Kademesi** | 2 Kademe Fan + 6 Kademe Eksenel Kompresör | Yüksek basınç oranı ve kompresyon verimi |
| **Nozul Geometrisi** | Değişken Geometrili Yakınsak-Iraksak Nozul | Süpersonik egzoz gazı yönlendirmesi |
| **Uygulama Alanları** | KIZILELMA-B, ANKA-3 Süpersonik, HÜRJET-C, Hızlı Hücumbotlar | İnsansız savaş uçakları ve hafif muharip jetler |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph Cekirdek_Turbofan["TF6000 Çekirdek Bölümü"]
        FAN["2 Kademeli Titanyum Fan"]
        HPC["6 Kademeli Yüksek Basınç Kompresörü (BLISK)"]
        COMBUSTION["Halka Tipi (Annular) Yanma Odası"]
        HPT["Tek Kristal Yüksek Basınç Türbini (1450°C)"]
        LPT["Alçak Basınç Türbini"]
        
        FAN --> HPC
        HPC --> COMBUSTION
        COMBUSTION --> HPT
        HPT --> LPT
    end

    subgraph Art_Yakici_ve_Nozul["Art Yakıcı (Afterburner) Fazı"]
        FUEL_SPRAY["Art Yakıcı Yakıt Enjeksiyon Halkaları"]
        FLAME_HOLDER["Alev Tutucu (Flame Holder) Izgarası"]
        CON_DIV_NOZZLE["Değişken Geometrili Nozul (10.000 lbf İtki)"]
        
        LPT --> FUEL_SPRAY
        FUEL_SPRAY --> FLAME_HOLDER
        FLAME_HOLDER --> CON_DIV_NOZZLE
    end

    subgraph Motor_Yonetimi["Dijital C4I Motor Yönetimi"]
        FADEC_TF["Yedekli Milli Askeri FADEC"]
        FADEC_TF --> FUEL_SPRAY
        FADEC_TF --> CON_DIV_NOZZLE
        FADEC_TF --> COMBUSTION
    end
```

- **Milli Tek Kristal Döküm Türbin Kanatçıkları:** TEI dökümhanelerinde geliştirilen, merkezkaç kuvvetine ve 1.450°C'yi aşan yanma gazlarına dayanıklı nikel süperalaşım kanatçıklar.
- **Değişken Geometrili Nozul Mekanizması:** Art yakıcı devreye girdiğinde nozul boğazını hidrolik/elektromekanik aktüatörlerle genişleterek motor içi geri basıncı önler ve süpersonik şok dalgalarını itkiye dönüştürür.
- **BLISK (Bladed Disk) Kompresör Diskleri:** Kanatçık ve diskin yekpare titanyum bloktan işlendiği, parça sayısını ve kaçakları azaltan ileri imalat teknolojisi.

---

## 🎯 Entegrasyon Platformları ve Muharebe Rolleri

### 1. Bayraktar KIZILELMA-B Süpersonik Muharebe
KIZILELMA'nın B varyantına ses üstü sürat kazandırarak hava-hava muharebelerinde düşman F-16 veya Su-35 savaş uçaklarına karşı önleme kabiliyeti sağlar.

### 2. TUSAŞ ANKA-3 Derin Darbe Taarruzu
Düşman hava savunmasının derinliklerine yüksek hızla sızarak dahili yuvasındaki SOM-J veya Tolun mühimmatlarını bırakıp hızla uzaklaşma olanağı tanır.

### 3. Deniz Platformları ve Hücumbotlar
Türk Deniz Kuvvetleri'nin yeni nesil hızlı hücumbot projelerinde gaz türbini tahrik ünitesi olarak yüksek sürat gücü sunar.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

```
[██████░░░░] TRL 6 - Çekirdek Doğrulandı, Art Yakıcı İmalat ve Yer Testleri
```

- [x] **TRL 1-3:** Art yakıcı aerotermal modelleme ve CFD simülasyonları.
- [x] **TRL 4:** TF6000 çekirdek motoru üzerinden tasarım optimizasyonu ve malzeme kalifikasyonu.
- [x] **TRL 5:** Çekirdek motor TF6000'in başarıyla ilk ateşlemesini yapması (Şubat 2024).
- [x] **TRL 6:** Art yakıcı modülü prototip imalatı ve yer bremzesinde alev tutucu test tertibatı kurulumu.
- [ ] **TRL 7:** TF10000 tam motor olarak art yakıcı ile bremzede tam güç (10.000 lbf) testi (2025).
- [ ] **TRL 8-9:** Uçuş testleri ve platform entegrasyonu (KIZILELMA-B & ANKA-3).

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
