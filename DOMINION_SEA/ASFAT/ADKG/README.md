# ⚓ Proje: Açık Deniz Karakol Gemisi (ADKG)

<div align="center">



[![TRL](https://img.shields.io/badge/TRL-8-00b0ff?style=for-the-badge&logo=shield&logoColor=white)

<p align="center">
  <img src="https://www.asfat.com.tr/uploads/adkg.jpg" alt="ADKG" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](../../../docs/TRL_GUIDE.md)
[![Dominion](https://img.shields.io/badge/DOMINION-SEA-blue?style=for-the-badge&logo=anchor&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/MANUFACTURER-ASFAT-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/STATUS-DEN%C4%B0Z%20KABUL%20TESTLER%C4%B0%20%2F%20DONATIM-ff9100?style=for-the-badge)]()

</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik

**Açık Deniz Karakol Gemisi (ADKG)** projesi, Milli Savunma Bakanlığı ASFAT (Askeri Fabrika ve Tersane İşletme A.Ş.) ana yükleniciliğinde İstanbul Tersanesi Komutanlığı'nda Türk Deniz Kuvvetleri için inşa edilen stratejik deniz platformudur. Türkiye'nin MİLGEM ADA Sınıfı korvetlerden elde ettiği dünya çapındaki yerli tekne form ve gövde mühendisliği tecrübesi üzerine temellenmiştir.

ADKG projesinin temel doktrinel felsefesi **"Fitted For But Not With" (Gerektiğinde Donatılabilir)** konseptidir. Barış döneminde arama-kurtarma, deniz haydutluğuyla mücadele, terörizmle mücadele ve MEB karakol görevlerini düşük işletme maliyeti ve yüksek yakıt ekonomisi ile yürütürken; gerginlik ve savaş döneminde üzerine saatler/günler içinde milli gemisavar füzeleri (ATMACA), dikey atım hava savunma lançerleri (MİDLAS / HİSAR) ve modern sonar sistemleri takılarak tam donanımlı bir savaş fırkateynine/korvetine dönüştürülebilir.

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Tam Boy (LOA)** | 99.56 Metre | Optimize edilmiş MİLGEM ADA sınıfı form |
| **Genişlik (Beam)** | 14.42 Metre | Geniş helikopter pisti ve operasyonel güverte |
| **Su Çekimi (Draft)** | 3.77 Metre | Açık deniz seyrüseferi için hidrodinamik tasarım |
| **Deplasman** | ~2.300 Ton | Yüksek mukavemetli gemi inşa çeliği gövde |
| **Azami Sürat** | 24+ Knot | İntikal ve önleme hızı |
| **Ekonomik Seyir Hızı** | 12 - 15 Knot | Uzun süreli okyanus ve açık deniz devriyesi |
| **Seyir Siası (Menzil)** | 4.500+ Deniz Mili (NM) | İkmal yapmaksızın 21 gün kesintisiz seyir |
| **Tahrik Mimarisi** | CODELOD (Kombine Dizel-Elektrik veya Dizel) | Yüksek yakıt verimliliği ve düşük işletme maliyeti |
| **Hava Araçları Kapasitesi** | 10 Tonluk Helikopter (Seahawk) & Döner/Sabit Kanat İHA | Tam donanımlı kapalı hangar ve uçuş güvertesi |
| **Mürettebat Kapasitesi** | 104 Kişi (+ Görev Kuvveti Konaklama) | Modern kamaralar ve uzun seyir lojistik desteği |

---

## 🧩 Alt Sistemler ve Aviyonik / Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph ADKG_PLATFORM["ADKG Gemi Omurgası & Tahrik"]
        HULL_MILGEM["MİLGEM ADA Sınıfı Optimize Çelik Gövde"]
        CODELOD_PROP["CODELOD Dizel-Elektrik / Dizel Tahrik Ünitesi"]
        FLIGHT_DECK["10 Ton Helikopter Pisti & İHA Hangarı"]
    end

    subgraph COMBAT_ELECTRONICS["Sensör, Radar ve Savaş Yönetimi"]
        ADVENT_SYS["HAVELSAN ADVENT Ağ-Merkezli Savaş Yönetim Sistemi"]
        SMART_RADAR["ASELSAN 3D Arama Radarı / MAR-D"]
        YAKAMOZ_SONAR["Meteksan YAKAMOZ Karinalı Sonar (Rezerv Alan)"]
        ARES_2N["ASELSAN ARES-2N Elektronik Destek (ED) Sistemi"]
    end

    subgraph WEAPON_PAYLOAD["Modüler Silah & Savunma Mimarisi"]
        MAIN_GUN["MKE 76/62mm Milli Deniz Topu"]
        GOKDENIZ["ASELSAN GÖKDENİZ 35mm Çift Namlulu CIWS"]
        ATMACA_SLOTS["8x ATMACA Gemisavar Füzesi (Rezerv Montaj Yuvası)"]
        MIDLAS_SLOTS["MİDLAS / HİSAR-D Dikey Atım Sistemi (Rezerv Alan)"]
    end

    ADKG_PLATFORM --> COMBAT_ELECTRONICS
    ADKG_PLATFORM --> WEAPON_PAYLOAD
    COMBAT_ELECTRONICS <===> WEAPON_PAYLOAD
```

- **ADVENT Savaş Yönetim Sistemi:** Dünyanın en modern ağ-merkezli savaş yönetim sistemlerinden biri olan HAVELSAN ADVENT ile diğer savaş gemileri, SİHA'lar ve denizaltılar ile ortak taktik veri paylaşımı.
- **Milli 76/62mm Deniz Topu:** MKE tarafından yerli imkanlarla üretilen dijital atış kontrollü baş topu ile su üstü ve hava hedeflerine dakikada 80+ atım.
- **Hava Savunma Kalkanı:** Yakın hava savunması için ASELSAN GÖKDENİZ 35mm parçacıklı mühimmat atan CIWS sistemi ve kızılötesi arama takip (IRST) entegrasyonu.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi

1. **Açık Deniz ve MEB Karakolu:** Doğu Akdeniz ve Karadeniz hidrokarbon sahalarında sondaj gemilerimize kesintisiz eskort ve koruma.
2. **Deniz Haydutluğu ve Asimetrik Tehdit Önleme:** Aden Körfezi, Somali açıkları ve Kızıldeniz'de uluslararası görev kuvvetlerinde bayrak gösterme ve ticari gemileri koruma.
3. **MUM-T Deniz-Hava Entegrasyonu:** Gemiden kalkan insansız hava araçlarının (TB3, ANKA) sağladığı radar ve hedef verileriyle yüzlerce mil ötedeki hedefleri takip etme.
4. **Savaş Dönemi Korvet Rolü:** Kriz anında rezerv yuvalarına 8 adet ATMACA gemisavar füzesi ve MİDLAS hava savunma lançeri yüklenerek taarruz gemisine dönüşme.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

- **Mevcut Durum:** `TRL 8` (Sınıfın ilk iki gemisi TCG AKHİSAR ve TCG KOÇHİSAR denize indirilmiş olup, deniz kabul testleri ve donatım faaliyetleri devam etmektedir).
- [x] Detay mühendislik tasarımı ve sözleşme fazı
- [x] Blok imalatı, kızaktan indirme ve tekne bütünlüğü doğrulaması
- [x] ADVENT, MAR-D ve milli 76mm deniz topu entegrasyonu
- [ ] Deniz kabul tecrübeleri (HAT & SAT) ve atışlı sistem kalifikasyonu
- [ ] Türk Deniz Kuvvetleri'ne bayrak çekme ve sancak teslim töreni

---

## 🔗 İç Dizin Navigasyonu

[⬅️ Üst Dizine (ASFAT)](../README.md) | [🏛️ Dominion Hub (DOMINION_SEA)](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
