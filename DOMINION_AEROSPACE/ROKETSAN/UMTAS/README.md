# 🎯 Proje: ROKETSAN UMTAS & L-UMTAS (Uzun Menzilli Tanksavar Füzesi)

<div align="center">

[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00f2fe?style=for-the-badge&logo=spacex&logoColor=white)

<p align="center">
  <img src="https://www.roketsan.com.tr/uploads/umtas.jpg" alt="UMTAS" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](../../README.md)
[![Üretici](https://img.shields.io/badge/%C3%9CRET%C4%B0C%C4%B0-ROKETSAN-orange?style=for-the-badge&logo=target&logoColor=white)](../README.md)
[![TRL](https://img.shields.io/badge/TRL-9%20(Muharebe%20Kan%C4%B1tlanm%C4%B1%C5%9F)-00E676?style=for-the-badge&logo=speedtest&logoColor=black)](../../../docs/TRL_GUIDE.md)
[![Durum](https://img.shields.io/badge/DURUM-Envanterde%20%2F%20%C4%B0hra%C3%A7%20Edildi-ff007f?style=for-the-badge&logo=shield&logoColor=white)](#)



</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
**UMTAS** (Uzun Menzilli Tanksavar Füze Sistemi) ve yarı aktif lazer arayıcı başlıklı varyantı **L-UMTAS**, modern muharebe sahasındaki tüm reaktif zırhlı ana muharebe tanklarına (MBT) ve ağır tahkimatlara karşı geliştirilmiş birincil milli tanksavar vurucu gücüdür. T129 ATAK taarruz helikopterinin ana mühimmatı olarak tasarlanan sistem; günümüzde SİHA'lar (Bayraktar TB2/TB3/AKINCI, ANKA/AKSUNGUR), hafif taarruz uçakları, zırhlı kara araçları ve hücumbotlara entegre edilmiştir. Sütre gerisinden atış ve uçuş esnasında çift yönlü RF veri bağı ile hedef güncelleme yetenekleri, dost unsurları düşman menziline girmeden mutlak zaferle buluşturur.

---

## 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Sistem Sınıfı** | Uzun Menzilli Hassas Güdümlü Tanksavar Füzesi (ATGM) | Havadan-Karaya ve Karadan-Karaya |
| **Füze Çapı** | 160 mm | Yüksek tandem patlayıcı çapı |
| **Füze Uzunluğu** | 1.75 Metre | Aerodinamik katlanır kanat mimarisi |
| **Toplam Ağırlık** | 37.5 kg | Helikopter ve SİHA pylonları için optimize |
| **Etkili Menzil** | 500 m - 8.000 m (8 km) | Helikopter stand-off taarruz kabiliyeti |
| **Güdüm Tipleri** | IIR (Görüntüleyici Kızılötesi) / YAL (L-UMTAS Yarı Aktif Lazer) | Gece/gündüz ve her türlü hava şartı |
| **Harp Başlığı** | Çift Kademeli Tandem Zırh Delici / Parçacık Etkili | Reaktif Zırh (ERA) arkasındaki ana zırhı eritir |
| **Kullanım Modları** | At-Unut (Fire & Forget) / At-Güncelle (Fire & Update) | LOBL (Atış Öncesi Kilit) / LOAL (Atış Sonrası Kilit) |
| **Veri Bağı** | Çift Yönlü RF Taktik Veri Bağı | Füze kamerasından kokpite anlık video aktarımı |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph Tasiyici_Platform["Taşıyıcı Platform Entegrasyonu"]
        ATAK["T129 ATAK / T929 ATAK-II"]
        SIHA["AKINCI / ANKA / AKSUNGUR / TB2"]
        LAND["KAPLAN / PARS 4x4 Tanksavar Aracı"]
        EO_POD["ASELFLIR-500 / MILDAR Radarı"]
    end

    subgraph Fuze_Gudum_Mimarisi["UMTAS Füze Mimarisi"]
        SEEKER_IIR["IIR Kızılötesi Görüntüleyici Arayıcı"]
        SEEKER_LASER["L-UMTAS Yarı Aktif Lazer Başlık"]
        DATALINK["İki Yönlü RF Veri Linki Modülü"]
        AUTOPILOT["Dijital Otopilot & Ataletsel Ölçüm (IMU)"]
    end

    subgraph Harp_Basligi_ve_Itki["İtki & Tahrip Mimarisi"]
        ROCKET_MOTOR["Düşük Dumanlı Katı Yakıtlı Roket Motoru"]
        TANDEM["Öncü Şarj (Precursor) + Ana Tandem Boşluklu İmla"]
    end

    EO_POD --> ATAK
    EO_POD --> SIHA
    ATAK --> DATALINK
    SIHA --> DATALINK
    LAND --> DATALINK
    DATALINK --> AUTOPILOT
    SEEKER_IIR --> AUTOPILOT
    SEEKER_LASER --> AUTOPILOT
    AUTOPILOT --> ROCKET_MOTOR
    AUTOPILOT --> TANDEM
```

- **IIR Görüntüleyici Arayıcı:** Termal kontrast farkından yararlanarak kamuflajlı, duman perdesi ardındaki veya ağaçlık alandaki araçları anında filtreleyip takip eder.
- **Sütre Gerisinden Atış (LOAL):** Helikopter dağın ardında gizlenirken füze ateşlenir; füze tepeyi aştığında kokpitteki pilota hedefin görüntüsünü yansıtır ve pilot ekrandan hedef tankı seçerek vuruşu tamamlar.
- **Tandem Zırh Delici Başlık:** Birinci kademe patlayıcı tankın üzerindeki patlayıcı reaktif zırhı (ERA) nötralize eder, ana şekillendirilmiş zırh delici mühimmat ise 1.000 mm+ haddelenmiş homojen çelik zırhı (RHA) delip içeri nüfuz eder.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi

### 1. Zırhlı Birliklerin Karşı Taarruzunun Kırılması
Düşman tank taburları ve zırhlı muharebe araçları, 8 km mesafeden ATAK helikopterlerinin 4'lü lançerlerinden art arda ateşlenen UMTAS füzeleriyle imha edilir.

### 2. Kıyı Savunması ve Hücumbot Engelleme
Deniz platformlarına yerleştirilen L-UMTAS lançerleri, adalar ve dar boğazlarda yaklaşan düşman hücumbotlarını ve amfibi çıkarma gemilerini lazer işaretleme ile batırır.

### 3. Taktik SİHA Hassas Angajmanı
AKINCI ve AKSUNGUR SİHA'ları yüksek irtifadan lazerle işaretlenen korunaklı komuta mevzilerini ve düşman havan mevzilerini L-UMTAS ile imha eder.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

```
[██████████] TRL 9 - Seri Üretim ve Muharebe Kanıtlanmış (Combat Proven)
```

- [x] **TRL 1-6:** ROKETSAN Ar-Ge laboratuvarlarında motor, kanatçık ve arayıcı başlık tasarımı.
- [x] **TRL 7:** T129 ATAK üzerinden canlı atış testleri ve hareketli hedeflere doğrudan isabet.
- [x] **TRL 8:** Zırh delme kalifikasyonu ve zorlu çevre koşulları (çöl sıcağı, dondurucu soğuk) testleri.
- [x] **TRL 9:** Türk Kara Kuvvetleri, Deniz Kuvvetleri ve Jandarma envanterine giriş; sınır ötesi harekâtlarda yoğun kullanım ve dost ülkelere ihracat.
- [ ] **Gelecek Vizyonu:** UMTAS-GM (Genişletilmiş Menzil) varyantı ile karadan 16+ km, havadan 30+ km menzile erişim.

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
