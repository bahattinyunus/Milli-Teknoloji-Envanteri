# 🎯 Proje: ŞİMŞEK (Yüksek Hızlı Hedef Uçak ve Dolanan Mühimmat)

[![TRL](https://img.shields.io/badge/TRL-9_Envanterde_ve_Operasyonel-success?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TUSAŞ-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Hizmette_ve_Seri_Üretimde-green?style=for-the-badge)](README.md)

<p align="center">
  <img src="../../../_ASSETS/platforms/SIMSEK.jpg" alt="ŞİMŞEK" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![TUSAŞ ŞİMŞEK Yüksek Hızlı Hedef Uçak Sistemi](https://www.tusas.com/uploads/2021/04/simsek-1.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
TUSAŞ ŞİMŞEK, Türk Silahlı Kuvvetleri'nin hava savunma birliklerinin eğitim ve tatbikatlarında düşman savaş uçaklarını, seyir füzelerini ve yüksek hızlı hava tehditlerini simüle etmek üzere özgün olarak geliştirilmiş yüksek hızlı hedef uçak sistemidir. Turbojet motoruyla 400 knot hıza ulaşabilen ŞİMŞEK; HİSAR, SİPER, KORKUT ve deniz hava savunma sistemlerinin atışlı testlerinde kilit rol oynamaktadır. Son yıllarda kazanılan ilave kabiliyetlerle, üzerine patlayıcı harp başlığı ve arayıcı başlık entegre edilerek ANKA ve AKSUNGUR SİHA'lardan atılabilen yüksek hızlı bir kamikaze dolanan mühimmata (Loitering Munition) dönüştürülmüştür.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Maksimum Kalkış Ağırlığı** | 75 kg |
| **Faydalı Yük Kapasitesi** | İzleme cihazları, duman üreteci, Lünberg lensi veya harp başlığı |
| **Motor** | 1 x Mini Turbojet Motoru (TEI TJ90 / 400N İtki) |
| **Azami Hız** | 740 km/s (400 Knots / Mach 0.6) |
| **Maksimum Uçuş İrtifası** | 25.000 ft (7.620 m) |
| **Havada Kalış Süresi** | 45 - 60 dakika |
| **Fırlatma Sistemi** | Basınçlı Katapult veya ANKA / AKSUNGUR kanat altı salıcı |
| **Kurtarma Sistemi** | Paraşüt ve deniz üzerine iniş için yüzdürücü yastıklar (Hedef modunda) |
| **Menzil / Veri Bağı** | 50+ km (Görüş hattı LOS) / Uydu destekli otonom rota |
| **G Manevra Limiti** | +5g / -2g yüksek manevra taklidi |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Otopilot & Seyrüsefer:** TUSAŞ özgün uçuş kontrol bilgisayarı, GPS destekli otonom rota takip ve rota acil geri dönüş modları.
- **Radar İzi Artırıcı:** Karşı hava savunma radarlarına savaş uçağı gibi görünmesini sağlayan pasif ve aktif radar yansıtıcı Lünberg lensi.
- **Akustik ve Duman İzleyiciler:** Mermi ıskalama mesafesini ölçen akustik sensör (MDI - Miss Distance Indicator) ve görsel takip için duman jeneratörü.
- **Yer Kontrol İstasyonu:** Taşınabilir GCS üzerinden telemetri takibi ve formasyon uçuş yönetimi.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Hava Savunma Test ve Doğrulama:** HİSAR-A+, HİSAR-O+, SİPER ve KORKUT sistemlerinin canlı hedef önleme tatbikatları.
- **Kamikaze Saldırı Misyonu:** AKSUNGUR ve ANKA'dan salınarak düşman radar mevzileri veya komuta binalarına yüksek hızla dalış.
- **Sahte Hedef Görevi:** Düşman erken ihbar radarlarını meşgul ederek gerçek taarruz unsurlarının tespit edilmesini engelleme.
- **Deniz Hava Savunma Eğitimi:** MİLGEM korvetleri ve fırkateynlerinin hava savunma topları için alçaktan uçan gemisavar füzesi profili simülasyonu.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Fırlatma ve Ayrılma"
        L1["Kara Konuşlu Pnömatik Katapult"]
        L2["AKSUNGUR / ANKA Kanat Altı Salımı"]
    end
    subgraph "Uçuş ve İtki"
        J1["TEI TJ90 Turbojet Motoru (400N)"]
        J2["Otonom Otopilot (Mach 0.6 Uçuş)"]
    end
    subgraph "Görev Modları"
        M1["Hedef Modu: Radar Yansıtıcı Lünberg Lensi & Duman"]
        M2["Kamikaze Modu: Harp Başlığı & Dalış Güdümü"]
        M3["Kurtarma Modu: Paraşütle Karaya/Denize İniş"]
    end
    L1 --> J1
    L2 --> J1
    J1 --> J2
    J2 --> M1
    J2 --> M2
    J2 --> M3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] Orijinal ŞİMŞEK Hedef Uçak Geliştirme ve Kabulü
- [x] TSK ve Deniz Kuvvetleri Atışlı Tatbikatlarında Seri Kullanım
- [x] TEI TJ90 Yerli Turbojet Motoru Entegrasyonu
- [x] ANKA ve AKSUNGUR SİHA'lardan Havadan Fırlatma Testleri
- [x] Kamikaze Mühimmat Yeteneği Kazanımı ve Başarılı Hedef Vuruşu
- [ ] İhracat Faaliyetleri ve Sürü Görev Algoritmaları

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
