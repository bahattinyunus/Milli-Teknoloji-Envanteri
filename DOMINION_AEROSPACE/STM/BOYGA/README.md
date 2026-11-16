# 💣 Proje: STM BOYGA (Havan Mühimmatı Bırakan Taktik İHA)

<div align="center">

[![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-00f2fe?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md)
[![Üretici](https://img.shields.io/badge/%C3%9CRET%C4%B0C%C4%B0-STM%20%26%20MKE-orange?style=for-the-badge&logo=target&logoColor=white)](../README.md)
[![TRL](https://img.shields.io/badge/TRL-9%20(Muharebe%20Kan%C4%B1tlanm%C4%B1%C5%9F)-00E676?style=for-the-badge&logo=speedtest&logoColor=black)](../../../docs/TRL_GUIDE.md)
[![Durum](https://img.shields.io/badge/DURUM-Envanterde%20%2F%20Seri%20%C3%9Cretim-ff007f?style=for-the-badge&logo=shield&logoColor=white)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/BOYGA.jpg" alt="BOYGA" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

</div>

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
**STM BOYGA**, Savunma Teknolojileri Mühendislik (STM) ve Makine ve Kimya Endüstrisi (MKE) ortaklığıyla geliştirilen, özel mühimmat bırakma mekanizmasına ve balistik kestirim bilgisayarına sahip döner kanatlı taktik İHA sistemidir. Geleneksel piyade havan atışlarındaki dağılım payını ve mevzilenme zorluklarını ortadan kaldıran BOYGA; MKE tarafından özelleştirilmiş 81 mm havan mühimmatını düşmanın sığınak, siper veya zırhsız araçlarının üzerine santimetre hassasiyetiyle dikey olarak bırakır. Asimetrik harpte piyade timlerine dikey hava topçusu gücü sağlayan benzersiz bir taktik platformdur.

---

## 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik | Açıklama |
| :--- | :--- | :--- |
| **Sistem Sınıfı** | Döner Kanatlı Mühimmat Bırakan Taktik İHA | Dikey Kalkış-İniş (VTOL) Taktik Mühimmat Bırakıcı |
| **Faydalı Yük / Mühimmat** | 1 Adet MKE 81 mm Özelleştirilmiş Havan Mühimmatı | Optimize edilmiş tapa ve yönlendirici kuyruk |
| **Havada Kalış Süresi** | 30 Dakika (Mühimmat Yüklü) / 45 Dakika (Yüksüz) | Görev bölgesine intikal ve hassas nişan süresi |
| **Operasyonel Tavan** | 1.500 Metre AGL (Yer Seviyesinden Yüksek) | Düşman hafif silah menzilinin üstünde güvenli atış |
| **Haberleşme Menzili** | 5 km (Görüş Hattı - LOS) | Güvenli şifreli askeri veri bağı |
| **Ağırlık (Boş / MTOW)** | 13.5 kg / ~17 kg | İki kişilik tim tarafından taşınabilir modüler yapı |
| **Bırakma Doğruluğu** | < 1 Metre CEP | Balistik kestirim algoritması sayesinde |
| **Emniyet Mimarisi** | Çift Kademeli Mekanik & Elektronik Arming | Bırakma sonrası belirli mesafede tapa kurulması |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu

```mermaid
graph TD
    subgraph Komuta_ve_Kontrol["Operatör & Yer Kontrol (GCS)"]
        PILOT["Operatör Yer Kontrol İstasyonu (GCS)"]
        ANT["Kriptolu Çift Bant RF Veri Linki"]
        PILOT --> ANT
    end

    subgraph BOYGA_Platform["BOYGA Hava Platformu"]
        FC["Otonom Uçuş Kontrol Bilgisayarı"]
        GIMBAL["3 Eksenli Stabilize Elektro-Optik/Termal Kamera"]
        BALLISTIC_PC["STM Balistik Kestirim & Rüzgar Hesaplayıcı"]
        RELEASE["MKE Akıllı Mühimmat Salıcı Mekanizması"]
        
        ANT --> FC
        FC --> GIMBAL
        GIMBAL --> BALLISTIC_PC
        BALLISTIC_PC --> FC
        FC --> RELEASE
    end

    subgraph Muhimmat["81 mm Özel Mühimmat"]
        MORTAR["MKE 81 mm Parça Tesirli Havan"]
        FUZE["Güvenli Kurulabilir Akıllı Tapa"]
        RELEASE --> MORTAR
        MORTAR --> FUZE
    end
```

- **Milli Balistik Kestirim Algoritması:** Dronun anlık yer hızı, irtifası, yatış açıları ve harici rüzgar sensörlerinden gelen verileri saniyede onlarca kez işleyerek kameradaki nişangah dairesini hedefe kilitler.
- **Akıllı Bırakma Mekanizması:** Mühimmatı bırakırken dronun ağırlık merkezi değişimini anında telafi eden otopilot kompanzasyonu.
- **MKE Tapa Emniyeti:** Dron düşse dahi patlamayan, serbest düşüşte belirli irtifa ve dönüş devrine ulaştığında kurulan milli tapa mimarisi.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi

### 1. Siper ve Mevzi Arkasındaki Tehditleri İmha
Geleneksel tüfek ve roketlerin ulaşamadığı kum torbası arkasına veya beton mevzilere saklanmış keskin nişancı ve makineli tüfek yuvaları dik düşüşle etkisiz hale getirilir.

### 2. Meskun Mahal ve Bina Bacası Girişleri
Şehir çatışmalarında açık kapı, avlu veya sığınak havalandırma boşluklarına mühimmat bırakılarak sivil zayiat olmaksızın cerrahi tahribat sağlanır.

### 3. Pusu ve Yol Kontrol Tehditlerini Önleme
Konvoy güzergahındaki şüpheli menfez ve yol kenarı mevzileri güvenli mesafeden BOYGA ile taranıp anında imha edilir.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası

```
[██████████] TRL 9 - Seri Üretim ve Güvenlik Güçlerine Teslim Edildi
```

- [x] **TRL 1-4:** Konsept tasarımı, MKE 81 mm havan mühimmatı aerodinamik modifikasyonu.
- [x] **TRL 5-6:** Rüzgar tüneli testleri, prototip salıcı mekanizması ve yer testleri.
- [x] **TRL 7:** Saha testlerinde canlı havan mühimmatı bırakışları ve balistik algoritma doğrulaması.
- [x] **TRL 8:** TSK kabul ve kalifikasyon testlerinin sıfır hatayla tamamlanması.
- [x] **TRL 9:** Türk Kara Kuvvetleri Komutanlığı'na seri teslimat, aktif terörle mücadele görevleri.

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
