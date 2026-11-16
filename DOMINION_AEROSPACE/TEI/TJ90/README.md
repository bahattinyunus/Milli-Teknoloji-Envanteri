# ⚙️ Proje: TEI-TJ90 Mikro Turbojet Motoru

<div align="center">

[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00f2fe?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/%C3%9CRET%C4%B0C%C4%B0-TEI-orange?style=for-the-badge&logo=target&logoColor=white)](../README.md)
[![TRL](https://img.shields.io/badge/TRL-9%20(Seri%20%C3%9Cretim%20%2F%20Envanterde)-00E676?style=for-the-badge&logo=speedtest&logoColor=black)](../../../docs/TRL_GUIDE.md)
[![Durum](https://img.shields.io/badge/DURUM-Envanterde%20%2F%20Y%C3%BCksek%20UÃ§u%C5%9F%20Say%C4%B1s%C4%B1-ff007f?style=for-the-badge&logo=shield&logoColor=white)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/TJ90.jpg" alt="TJ90" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
**TEI-TJ90**, yüksek hızlı hedef uçaklar (TUSAŞ Şimşek) ve mini taktik seyir füzeleri için milli imkanlarla geliştirilmiş kompakt, yüksek devirli mikro turbojet motorudur. Yaklaşık 4 kilogramlık toplam gövde ağırlığına rağmen 400 Newton (90 lbf) itki üretebilen TJ90; hava savunma tatbikatlarında savaş uçağı ve füzeleri taklit eden hedef İHA'ların 500+ km/s süratlere ulaşmasını sağlar. Türk Silahlı Kuvvetleri'nin hava savunma unsurlarını (HİSAR, KORKUT, SİPER) en gerçekçi tehdit simülasyonlarıyla eğitmesinde ve harbe hazır tutulmasında sessiz kahramandır.

---

## 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Motor Sınıfı** | Mikro Turbojet İtki Sistemi | Kompakt Yüksek Devirli Jet Motoru |
| **Üretilen İtki** | 400 N (~90 lbf) @ Deniz Seviyesi | Yüksek hız tırmanma ve seyir gücü |
| **Çalışma Devri** | 96.000 - 100.000 RPM | Dakikada 100 bin devir dönen mikro türbin |
| **Kuru Motor Ağırlığı** | ~3.9 - 4.2 kg | Ultra hafif gövde mimarisi |
| **Dış Çap** | ~150 mm | Dar tüp ve kanat altı pod uyumu |
| **Platform Sürati** | 400 - 500+ km/s (Target Drone) | Gerçek savaş uçağı ve füze yaklaşma hızı |
| **Yakıt Tipi** | Jet-A1, JP-8 + %5 Özel Yağlama Karışımı | Basit ve güvenilir besleme mimarisi |
| **Başlatma Yöntemi** | Entegre Elektrikli Fırçasız Marş Motoru | Hızlı ve güvenilir yer/hava ateşlemesi |
| **Kontrol Mimarisi** | Milli Kompakt Dijital ECU Kartı | Otopilot ile tam entegre dijital yönetim |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu

```mermaid
flowchart LR
    subgraph Baslatma_Fazı["Ateşleme ve Marş"]
        STARTER["Entegre BLDC Elektrikli Marş Motoru"]
        AIR_SUCTION["Ön Hava Girişi (150 mm Çap)"]
        STARTER --> AIR_SUCTION
    end

    subgraph Turbojet_Cekirdek["TJ90 Çekirdek Yapısı"]
        CENT_COMP["Tek Kademe Santrifüj Kompresör"]
        BURNER["Halka Yanma Odası (100.000 RPM)"]
        AXIAL_TURBINE["Yüksek Isı Alaşımlı Eksenel Türbin"]
        EXHAUST["Egzoz Lülesi (400 N İtki)"]
        
        AIR_SUCTION --> CENT_COMP
        CENT_COMP --> BURNER
        BURNER --> AXIAL_TURBINE
        AXIAL_TURBINE --> EXHAUST
    end

    subgraph Sayisal_Kontrol["Mikro ECU & Telemetri"]
        ECU_TJ90["TEI Mikro Dijital Motor Kontrol Kartı"]
        ECU_TJ90 --> BURNER
        AXIAL_TURBINE --> STARTER
    end
```

- **100.000 RPM Rotor Kararlılığı:** Dakikada 100.000 devir yapan milin dinamik balans ve mikro seramik rulmanlarla titreşimsiz çalışması sağlanmıştır.
- **Yekpare Santrifüj Çark:** Havayı merkezkaç kuvvetiyle radyal olarak hızlandıran yüksek mukavemetli alüminyum alaşım kompresör.
- **Entegre Marş/Jeneratör:** Motoru çalıştıran marş motoru, motor rölantiye ulaştıktan sonra jeneratör moduna geçerek hedef uçağın elektroniklerini besler.

---

## 🎯 Uygulama Alanları ve Hedef Platformlar

### 1. TUSAŞ Şimşek Yüksek Hızlı Hedef Uçak
Hava savunma radarları ve füzeleri için dost kuvvet tatbikatlarında süpersonik/yüksek hızlı düşman hava hedeflerini simüle eder.

### 2. Kamikaze Hedef ve Sahte Hedef (Decoy)
Düşman hava savunmasını aldatmak ve mühimmatını boşa harcatmak üzere fırlatılan sahte hedef mühimmatlarında itki kaynağıdır.

### 3. Hafif Taktik Seyir ve Loitering Füzeleri
Geleceğin otonom mini seyir füzeleri ve sürü taarruz platformları için maliyet etkin itki alternatifi sunar.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

```
[██████████] TRL 9 - Seri Üretimde, TSK Tarafından Yaygın Kullanımda
```

- [x] **TRL 1-4:** TEI bünyesinde mikro turbojet motor tasarımı ve aerodinamik akış çözümleri.
- [x] **TRL 5-6:** Prototip üretimi, test standında 400 Newton itki ve 100.000 RPM doğrulaması.
- [x] **TRL 7:** TUSAŞ Şimşek platformuna entegrasyon ve ilk başarılı uçuş testi (2017).
- [x] **TRL 8:** Çoklu irtifa uçuşları, yüksek hız dalışları ve askeri çevre kalifikasyonu.
- [x] **TRL 9:** Seri üretim teslimatları, TSK atış poligonlarında kesintisiz operasyonel hizmet.

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
