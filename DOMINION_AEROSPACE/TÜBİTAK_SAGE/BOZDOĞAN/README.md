# 🦅 Proje: BOZDOĞAN (Görüş İçi Hava-Hava Füzesi - WVRAAM)

[![TRL](https://img.shields.io/badge/TRL-9_Envanter_Kabul_ve_Seri_Üretim-success?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TÜBİTAK_SAGE-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Hava_Kuvvetleri_Envanterinde-green?style=for-the-badge)](README.md)

<p align="center">
  <img src="https://www.sage.tubitak.gov.tr/uploads/bozdogan.jpg" alt="BOZDOĞAN" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![TÜBİTAK SAGE BOZDOĞAN Görüş İçi Hava-Hava Füzesi](https://www.sage.tubitak.gov.tr/sites/default/files/inline-images/bozdogan.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
BOZDOĞAN, Türk Hava Kuvvetleri'nin hava-hava muharebelerinde mutlak üstünlük sağlaması amacıyla TÜBİTAK SAGE tarafından 'GÖKTUĞ' projesi kapsamında milli imkanlarla geliştirilen kısa menzilli Görüş İçi Hava-Hava Füzesidir (Within Visual Range Air-to-Air Missile - WVRAAM). ABD menşeili AIM-9X Sidewinder füzesinin yerini alan BOZDOĞAN; çift renkli Kızılötesi Görüntüleyici Arayıcı Başlığı (IIR), itki vektör kontrol sistemi (TVC) ve kaska monteli nişangah entegrasyonu sayesinde pilotun kaskıyla baktığı açıdaki en çevik düşman uçaklarını ve füzelerini 'off-boresight' (görüş ekseni dışı) kabiliyetiyle yüksek manevra yaparak avlayabilmektedir. F-16 PO-III/ÖZGÜR, KAAN, HÜRJET, AKINCI ve KIZILELMA için kritik bir caydırıcılık unsurudur.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Füze Tipi** | Kısa Menzilli Görüş İçi Hava-Hava Füzesi (WVRAAM) |
| **Arayıcı Başlık Tipi** | Yüksek Çözünürlüklü Çift Renkli Kızılötesi Görüntüleyici (IIR - Imaging Infrared) |
| **Arayıcı Başlık Görüş Açısı** | ±90° Off-Boresight Geniş Açı Hedef Kilitlenme |
| **Maksimum Hız** | Mach 4+ (Süpersonik) |
| **Etkili Menzil** | 25+ km |
| **Manevra Kabiliyeti** | İtki Vektör Kontrolü (TVC) ile 50g+ Yüksek G Manevra |
| **İtki Motoru** | Düşük Dumanlı Katı Yakıtlı Roket Motoru |
| **Harp Başlığı** | Yüksek İnfilaklı Lazer Yaklaşma Tapalı Parçacık Tesirli Harp Başlığı |
| **Füze Ağırlığı / Çapı** | ~140 kg / 160 mm |
| **Entegrasyon Platformları** | F-16 (ÖZGÜR / CCIP), KAAN, HÜRJET, AKINCI, KIZILELMA, ANKA-3 |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **IIR Arayıcı Başlık:** ASELSAN/TÜBİTAK SAGE tasarımı çift spektral termal dedektör; flare ve kızılötesi karıştırıcılara (DIRCM) karşı üstün hedef ayırt etme algoritmaları.
- **İtki Vektör Kontrol Sistemi (TVC):** Roket motor çıkış lülesinde hareketli kanatçıklar ile fırlatma anından itibaren füzenin anında hedefe dönmesini sağlayan aşırı manevra kontrolü.
- **Kask Nişangah Entegrasyonu:** TULGAR veya kaska monteli görüş sistemleri ile pilotun hedefe sadece bakması ve kilitlenmesiyle fırlatılabilme.
- **Atış Öncesi / Sonrası Kilitlenme:** LOAL (Lock-On After Launch) ve LOBL (Lock-On Before Launch) yeteneği.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **İt Dalaşı (Dogfight):** Yüksek manevralı yakın hava muharebelerinde düşman savaş uçaklarının ani manevralarını TVC desteğiyle karşılayıp arkadan, önden veya yandan imha.
- **Seyir Füzesi & İHA Önleme:** Alçaktan uçan seyir füzeleri veya intihar İHA'larını yüksek termal hassasiyetle tespit edip havada parçalama.
- **SİHA Hava Savunması:** AKINCI ve KIZILELMA üzerinden fırlatılarak dost SİHA'ları düşman avcı uçaklarına karşı koruma altına alma.
- **Görüş Hattı Dışı Angajman:** Hedefin uçağın arkasında veya dik açısında olduğu durumlarda bile fırlatılıp 180 derece dönüşle hedefi vurma.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Pilot & Platform Sensörleri"
        P1["Uçak Radarı / IRST (MURAD / KARAT)"]
        P2["Kask Monteli Nişangah (TULGAR HMDS)"]
        P3["F-16 ÖZGÜR / KAAN Görev Bilgisayarı"]
    end
    subgraph "Füze Güdüm & Algılama"
        B1["IIR Çift Spektral Kızılötesi Arayıcı Başlık"]
        B2["Off-Boresight ±90° Açısal Kilitlenme"]
        B3["Atış Öncesi / Sonrası Kilitlenme (LOBL/LOAL)"]
    end
    subgraph "İtki & Yüksek Manevra Vuruşu"
        M1["Düşük Dumanlı Katı Yakıtlı Motor (Mach 4+)"]
        M2["İtki Vektör Kontrolü (TVC Kanatçıkları)"]
        M3["50g+ Manevra ile Hedefe Cerrahi Vuruş"]
    end
    P1 --> P3
    P2 --> P3
    P3 --> B2 --> B1
    B1 --> M2
    M1 --> M2 --> M3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] GÖKTUĞ Projesi Kapsamında Tasarım ve Simülasyon
- [x] Yer ve Rüzgar Tüneli Testleri
- [x] F-16 Kanat Altından Ayrılma ve Balistik Uçuş Testleri
- [x] Canlı Hedef Uçağa (ŞİMŞEK) Karşı Güdümlü Tam İsabetli Atış Testi
- [x] Düşük Yoğunluklu Seri Üretim Sözleşmesi İmzalanması
- [x] Hava Kuvvetleri Komutanlığı Envanterine Giriş ve TRL 9 Doğrulaması

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
