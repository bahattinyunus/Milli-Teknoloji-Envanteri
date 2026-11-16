# ☀️ Proje: TÜBİTAK SAGE GÜNEŞ (Akıllı Güdüm Kiti ve Arayıcı Başlık Ailesi)

[![TRL](https://img.shields.io/badge/TRL-9_Sertifiye_ve_Seri_Üretimde-success?style=for-the-badge&logo=shield)](README.md) [![Dominion](https://img.shields.io/badge/DOMINION-AEROSPACE-0052cc?style=for-the-badge&logo=spacex&logoColor=white)](../../README.md) [![Üretici](https://img.shields.io/badge/ÜRETİCİ-TÜBİTAK_SAGE-red?style=for-the-badge)](../README.md) [![Durum](https://img.shields.io/badge/DURUM-Envanterde_ve_Operasyonel-green?style=for-the-badge)](README.md)

<p align="center">
  <img src="../../../_ASSETS/platforms/GUNES.jpg" alt="GÜNEŞ" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>



![TÜBİTAK SAGE GÜNEŞ Akıllı Güdüm Kiti ve Arayıcı Başlık Donanımı](https://www.sage.tubitak.gov.tr/sites/default/files/gunes.jpg)

---

### 🛡️ Stratejik Tanım & Doktriner Öncelik
TÜBİTAK SAGE GÜNEŞ, Türk Silahlı Kuvvetleri'nin envanterindeki güdümsüz konvansiyonel genel maksat mühimmatlarını ve hafif hava mühimmatlarını her türlü hava koşulunda hareketli ve sabit hedeflere karşı cerrahi nokta vuruşu yapabilen akıllı füzelere dönüştürmek amacıyla geliştirilen modüler arayıcı başlık ve akıllı güdüm kiti ailesidir. Lazer Arayıcı Başlık (LAB) ve Kızılötesi Görüntüleyici (IIR) konfigürasyonlarına sahip olan GÜNEŞ mimarisi; düşmanın yoğun elektronik karıştırma ve GPS köreltmesi yaptığı zorlu harekat sahalarında dahi hedefini bağımsız olarak teşhis edip 1 metrenin altında dairesel sapma (CEP) hassasiyetiyle imha etme kabiliyeti sunmaktadır.

---

### 📊 Kapsamlı Teknik Özellikler Tablosu

| Parametre | Değer / Özellik |
| :--- | :--- |
| **Sistem Tipi** | Modüler Akıllı Güdüm Kiti ve Terminal Arayıcı Başlık |
| **Arayıcı Başlık Seçenekleri** | Yarı Aktif Lazer Arayıcı (LAB) / Soğutmalı IIR (Kızılötesi Görüntüleyici) |
| **Vuruş Hassasiyeti (CEP)** | <1 metre (Lazer / IIR terminal güdüm ile) |
| **Güdüm Algoritması** | Oransal Seyrüsefer (Proportional Navigation) ve Optimal Terminal Dalış Kontrolü |
| **Uyumlu Mühimmat Sınıfları** | MK-81, MK-82, MK-83 genel maksat bombaları ve minyatür hafif hava bombaları |
| **Elektronik Karıştırma Direnci** | GNSS köreltmesinden etkilenmeyen otonom elektro-optik hedef takibi |
| **Atış İrtifası / Bırakma Zarfı** | 5.000 ft - 40.000 ft irtifa aralığı |
| **Hedef Hızı Kapasitesi** | 100 km/s üzeri yüksek hızlı hareketli kara ve deniz hedeflerine kilitlenme |
| **Ayrılma Sonrası Kilitlenme** | Uçuş sırasında dinamik hedef yakalama ve kilitlenme (LOAL yeteneği) |
| **Entegre Platformlar** | F-16 ÖZGÜR/CCIP, KAAN, HÜRJET, AKINCI, AKSUNGUR, ANKA-3 |

---

### 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Modüler Sensör Başlığı:** Değiştirilebilir burun konisi mimarisi; lazer lekesi izleyici detektör veya termal matris arayıcı.
- **Kriptolu Otopilot ve Kanat Tahrik:** Hızlı tepki süresine sahip fırçasız DC servo motorlu yönlendirme kanatçıkları (CAS - Control Actuator System).
- **Hedef Tanıma & Karar Algoritmaları:** Hedefin kamuflaj arkasına geçmesi veya duman perdesi oluşturması durumunda son bilinen vektöre göre vuruş tamamlama yazılımı.
- **Entegre Güç Ünitesi:** Yüksek deşarjlı termal batarya ile uzun süzülüş sürelerinde kesintisiz enerji temini.

---

### 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Yüksek Hızlı Hareketli Hedef Vuruşu:** Seyir halindeki düşman zırhlı araçları, hücumbotlar veya terörist konvoylarına hareket halinde tam isabet.
- **GPS-Korumalı Cerrahi Taarruz:** GPS sinyallerinin tamamen kesildiği yoğun elektronik harp cephelerinde lazer veya optik güdümle tahkimatları imha.
- **Şehir İçi Hassas Operasyonlar:** Sivil yerleşim bölgelerine yakın askeri mevzilerin tali hasarsız ve sıfır yan hasar riskiyle bertaraf edilmesi.
- **SİHA Taarruzu:** AKINCI ve AKSUNGUR SİHA'lardan yüksek irtifadan bırakılarak hava savunma menzili dışından derin hedeflere angajman.

---

### 📐 Özel Mimari ve Görev Akış Şeması
```mermaid
graph TD
    subgraph "Arayıcı Başlık Seçenekleri"
        S1["Yarı Aktif Lazer Arayıcı Başlık (LAB)"]
        S2["Kızılötesi Görüntüleyici Arayıcı Başlık (IIR)"]
    end
    subgraph "GÜNEŞ Merkezi Güdüm & Kontrol"
        G1["Sayısal Otopilot & Seyrüsefer İşlemcisi"]
        G2["Anti-Jam GNSS / INS Destek Ünitesi"]
        G3["Fırçasız Elektromekanik Kanat Tahrik (CAS)"]
    end
    subgraph "Uygulama Mühimmatları & Vuruş"
        W1["MK Serisi Genel Maksat Bombaları"]
        W2["Hassas Minyatür Bombalar"]
        W3["CEP < 1 Metre Cerrahi Vuruş"]
    end
    S1 --> G1
    S2 --> G1
    G2 --> G1
    G1 --> G3
    G3 --> W1
    G3 --> W2
    W1 --> W3
    W2 --> W3
```

---

### 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- [x] Lazer ve IIR Arayıcı Başlık Algoritma Tasarımı
- [x] Rüzgar Tüneli ve Donanım-Döngüde (HIL) Testleri
- [x] F-16 ve SİHA Bırakma Testleri
- [x] Hareketli Hedeflere Karşı Canlı Atış Doğrulamaları
- [x] Seri Üretim Sertifikasyonu ve TSK Envanter Girişi (TRL 9)
- [ ] Yeni Nesil Yapay Zekalı Görüntü İşleme Yazılım Güncellemeleri

---

### 🔗 Sağlam İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
