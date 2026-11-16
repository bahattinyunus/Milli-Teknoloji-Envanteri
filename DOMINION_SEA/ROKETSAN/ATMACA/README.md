# 🦅 Proje: ATMACA (Satıhtan Satıha Hassas Gemisavar Füzesi)

[![TRL](https://img.shields.io/badge/TRL-9%20(Muharebede%20Kanıtlanmış)

<p align="center">
  <img src="https://www.roketsan.com.tr/uploads/atmaca.jpg" alt="ATMACA" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
-00e676?style=for-the-badge&logo=shield)](../../../README.md)
[![Dominion](https://img.shields.io/badge/Dominion-SEA%20(Mühimmat)-0077be?style=for-the-badge&logo=target)](../../README.md)
[![Manufacturer](https://img.shields.io/badge/Üretici-ROKETSAN-e63946?style=for-the-badge)](../README.md)
[![Status](https://img.shields.io/badge/Durum-Envanterde%20%2F%20Seri%20Üretim-success?style=for-the-badge)]()

<div align="center">
  
</div>

![ATMACA](https://www.roketsan.com.tr/uploads/docs/1655105658_atmaca-tr-web.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
ATMACA, ROKETSAN tarafından her türlü hava şartında görev yapabilen, satıhtan satıha uzun menzilli, yüksek hassasiyetli bir gemisavar ve kıyı savunma seyir füzesi olarak geliştirilmiştir. "Mavi Vatan'ın Çelik Kılıcı" olarak adlandırılan ATMACA; Türk Deniz Kuvvetleri'nin Amerikan üretimi Harpoon (RGM-84) füzelerine bağımlılığını tamamen ortadan kaldırmıştır. Süper deniz yalama (sea-skimming: su yüzeyinden 3-5 metre irtifada seyir), gelişmiş 3B görev planlama, radar izini gizleyen kompozit gövde ve radar arayıcı başlık özellikleriyle donatılmıştır. Yerli Kale Arge KTJ-3200 turbojet motoruyla seri üretime geçen füze; MİLGEM korvetleri, İ-Sınıfı fırkateynler ve kıyı bataryalarında tam operasyonel statüde hizmet vermektedir.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Füze Tipi** | Satıhtan Satıha / Kıyı Konuşlu Hassas Gemisavar Füzesi | Çok maksatlı gemi ve kıyı hedefleri |
| **Menzil** | 220+ Kilometre (120+ Deniz Mili) | Harpoon Blok II'nin ötesinde menzil |
| **Uçuş Hızı** | Mach 0.85 - 0.90 (Yüksek Subsonik) | Radara yakalanma süresini minimize eder |
| **Füze Ağırlığı** | ~750 kg (Katı yakıtlı fırlatma motoru dahil) | Çap: 350 mm / Kanat Açıklığı: 1.4 m |
| **Harp Başlığı** | 220 kg Yüksek Patlayıcılı / Yarı Zırh Delici | Penetrasyon ve gecikmeli patlama |
| **Motor Sistemi** | Katı Yakıtlı Booster + Kale Arge KTJ-3200 Turbojet | Yerli ve milli itki sistemi |
| **Güdüm Mimarisi** | INS + GPS + Barometrik/Radar Altimetre + Aktif RF | Karıştırmaya dayanıklı anti-jamming GPS |
| **Veri Bağı** | KEMENT İki Yönlü RF Taktik Veri Bağı | Uçuş sırasında hedef güncelleme & iptal |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Aktif RF Radar Arayıcı Başlık:** ASELSAN tarafından geliştirilen yüksek çözünürlüklü X-Bant aktif radar; elektronik harp karıştırmalarına karşı frekans atlama ve sahte hedefleri filtreleme algoritmalarına sahiptir.
- **KEMENT Veri Bağı Entegrasyonu:** Meteksan Savunma KEMENT veri bağı sayesinde; fırlatıldıktan sonra dahi hedefin konum güncellemelerini alabilme, filo içindeki diğer platformlardan hedef koordinatı transfer etme ve yeniden angajman (re-attack) manevrası yapabilme.
- **3B Dinamik Görev Planlama:** Adalar Denizi gibi coğrafi engellerin arkasından dolaşabilen, belirlenen arazi noktalarından sakınarak rotayı büken çoklu büküm noktası (waypoint) programlama yeteneği.
- **Deniz Yalama (Sea-Skimming):** Son yaklaşma fazında dalga tepelerini yalayarak radar ufkunun altında tespit edilemez irtifada intikal.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Su Üstü Görev Grubu İmhası:** Salvo atış modunda fırlatılan çoklu ATMACA füzelerinin farklı açılardan ve aynı anda hedefe varması (Time-on-Target) ile düşman hava savunma radarlarını doyuma uğratma.
- **Kıyı ve Liman Taarruzu:** Limanda demirli kritik lojistik gemileri veya kıyı radar üslerini hassas vuruşla tahrip etme.
- **Mobil Kıyı Savunma (BARBAROS):** 8x8 tekerlekli taktik araçlara monte edilen kıyı bataryalarıyla boğazları ve stratejik geçiş hatlarını kıyıdan kapatma.

---

### 📐 Özel Sistem Mimarisi & Görev Akışı

```mermaid
flowchart TD
    subgraph FIRLATMA["🚀 Fırlatma ve Tırmanış"]
        LANCER["Gemi Lançeri / Kıyı Bataryası"]
        BOOSTER["Katı Yakıtlı Hızlandırıcı (Booster)"]
        TURBOJET["Kale Arge KTJ-3200 Turbojet Motoru"]
        LANCER --> BOOSTER
        BOOSTER --> TURBOJET
    end

    subgraph SEYIR["🗺️ Seyir ve Veri Bağı Fazı"]
        INS_GPS["INS / Anti-Jam GPS Seyrüsefer"]
        WAYPOINTS["3B Çoklu Rota Büküm Noktaları"]
        KEMENT["KEMENT İki Yönlü RF Veri Bağı"]
        INS_GPS --> WAYPOINTS
        WAYPOINTS <==> KEMENT
    end

    subgraph TERMINAL["💥 Terminal Faz ve Vuruş"]
        SEASKIM["Süper Deniz Yalama (<3-5m İrtifa)"]
        RF_SEEKER["ASELSAN Aktif RF Arayıcı Başlık Kilidi"]
        POP_UP["Pop-Up veya Doğrudan Vuruş Manevrası"]
        HIT["220 kg Yarı Zırh Delici İnfilak"]
        
        WAYPOINTS --> SEASKIM
        SEASKIM --> RF_SEEKER
        RF_SEEKER --> POP_UP
        POP_UP --> HIT
    end
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
**Mevcut Olgunluk Seviyesi: TRL 9 (Muharebede Kanıtlanmış & Donanmada Aktif)**
- [x] TCG KINALIADA'dan telemetri ve harp başlıklı hedef batırma atışları
- [x] KTJ-3200 yerli turbojet motoru kalifikasyonu ve başarılı test uçuşu
- [x] Seri üretim hattının kurulması ve TCG İSTANBUL'a 16 adetlik tam konfigürasyon teslimi
- [x] BARBAROS Kıyı Savunma Sistemi kapsamında kara bataryasından atış başarısı
- [ ] Görüntüleyici Kızılötesi (IIR) arayıcı başlıklı ve denizaltı atımlı varyantlar

---
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)\n