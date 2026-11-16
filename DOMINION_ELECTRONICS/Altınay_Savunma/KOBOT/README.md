# 🤖 Proje: Altınay Savunma KOBOT (Taktik Hafif Sınıf İnsansız Kara Aracı)

[![TRL](https://img.shields.io/badge/TRL-9_Saha_Kanıtlanmış-success?style=for-the-badge&logo=shield)](https://www.altinay.com)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-Altınay_Savunma-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Aktif_Kullanımda-brightgreen?style=for-the-badge)](#)

<p align="center">
  <img src="../../../_ASSETS/platforms/KOBOT.jpg" alt="Altınay Savunma KOBOT" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>

<div align="center">
  
</div>

> **Üretici:** Altınay Savunma Teknolojileri  
> **Sınıf:** Hafif Sınıf Taktik İnsansız Kara Aracı (İKA) & Bomba İmha Robotu  
> **Stratejik Önem:** Meskun mahal, dar bina içi, tünel, mağara ve şüpheli paket incelemelerinde askeri ve emniyet timlerinin hayati tehlikesini sıfırlayan, sırtta taşınabilir yüksek çeviklikte taktik robotik platform.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
Altınay Savunma KOBOT, zorlu arazi ve kapalı alan koşullarında güvenlik güçlerinin keşif, gözetleme, patlayıcı madde imhası (EOD) ve asimetrik tehdit müdahale görevlerini uzaktan güvenle icra etmesi amacıyla üretilmiş hafif sınıf bir insansız kara platformudur. Modüler mafsallı robotik kolu, paletli hareket mimarisi ve yüksek torklu elektrik motorları sayesinde merdiven tırmanabilir, dik engelleri aşabilir ve enkaz altında ilerleyebilir. Taşınabilir dayanıklı operatör kontrol ünitesi (OCU) üzerinden çift yönlü şifreli veri ve HD görüntü aktarımı gerçekleştirerek askerin can güvenliğini ön planda tutar.

```mermaid
flowchart TD
    subgraph Operatör_Kontrol_Birimi["Taktik Operatör Kontrol İstasyonu (OCU)"]
        TAB["Sağlamlaştırılmış Askeri Dokunmatik Tablet (Mil-Std)"]
        JOY["Çok Fonksiyonlu Taktik Joystick & Manipülatör Kumandası"]
        LINK["Kriptolu Çift Bantlı Taktik RF Link (MIMO / Mesh)"]
        TAB <--> JOY <--> LINK
    end

    subgraph KOBOT_Gövde_Ve_Mekanizma["Altınay KOBOT İKA Platformu"]
        direction TB
        DRIVE["Yüksek Torklu Paletli Çekiş Sistemi & Çevirmeli Palet Kolları (Flipper)"]
        ARM["Çok Eksenli Yüksek Hassasiyetli Robotik Kol (Manipülatör)"]
        CAM["360° Pan-Tilt Gözetleme Kamerası & Gece Görüş LED"]
        GRIP["Kavrayıcı Pençe & Bomba İmha Su Topu Arayüzü"]
        PWR["Hızlı Değiştirilebilir Li-Ion Akıllı Batarya Paketi"]
        
        ARM --- GRIP
        DRIVE --- ARM
        DRIVE --- CAM
        PWR --> DRIVE & ARM & CAM
    end

    subgraph Müdahale_Görevleri["Operasyonel Müdahale"]
        IED["El Yapımı Patlayıcı / Şüpheli Çanta İmhası"]
        TUNNEL["Mağara & Tünel İçi Mayın / Tuzak Keşfi"]
        BLD["Bina İçi Rehine / Oda Temizleme İstihbaratı"]
    end

    LINK <===>|Sayısal Komuta & Video Yayını| KOBOT_Gövde_Ve_Mekanizma
    GRIP -.->|Hassas Yakalama & Taşıma| IED
    CAM -.->|Karanlık Ortam Termal/Görsel Tespit| TUNNEL
    DRIVE -.->|Merdiven Tırmanma & Oda İçi Sızma| BLD
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Araç Ağırlığı** | ~20 - 35 kg (Modüler zırh ve robot kol donanımına göre sırtta taşınabilir) |
| **Tahrik Sistemi** | Çift Bağımsız Palet + Ön/Arka Açı Ayarlı Yardımcı Palet Kolları (Flippers) |
| **Engel ve Merdiven Tırmanma**| 45° Eğim Tırmanma, 25-30 cm Dik Engel Aşma, Standart Merdiven İnip Çıkabilme |
| **Azami Hız** | 5 - 8 km/s (Operasyonel Taktik Hız) |
| **Çalışma Süresi** | 3 ila 5 Saat Kesintisiz Görev (Hızlı değiştirilebilir Lityum-İyon batarya) |
| **Robotik Kol Taşıma Gücü** | Tam açık kolda 5+ kg, gövdeye yakın tutuşta 15+ kg kaldırma kapasitesi |
| **Haberleşme Menzili** | Açık Arazide 1.000+ metre / Şehir İçi ve Bina İçi 300+ metre Kriptolu Link |
| **Çevre Koruma Sınıfı** | IP67 Su, Toz ve Çamur Geçirmezlik; MIL-STD-810H Askeri Şok/Düşme Dayanımı |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **6 Eksenli Robotik Manipülatör Kol:** Kapı kolu açma, araba bagajı kaldırma ve şüpheli paketlerin hassas biçimde incelenmesini sağlayan mikro pozisyonlama motorları.
- **Entegre Bomba İmha Donanımları:** Robotik kola takılabilen su jeti (disruptor), fünye yerleştirici ve X-ray görüntüleme cihazı entegrasyonu.
- **Karanlık Alan ve Gece Görüşü:** Gövde ön/arka ve kol üzerinde kızılötesi aydınlatıcılar, yüksek çözünürlüklü gündüz/gece kameraları.
- **Düşme / Ters Dönme Kurtarma (Self-Righting):** Robot takla attığında flipper kolları vasıtasıyla kendi kendini doğrultarak göreve devam edebilme.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Şüpheli Paket ve Bomba İmhası:** Kalabalık şehir meydanlarında veya araç altlarında tespit edilen patlayıcıları güvenli mesafeden inceleme ve su jetiyle patlatmadan etkisizleştirme.
- **Mağara ve Tünel Operasyonları:** Terör unsurlarının sığındığı dar mağara ağızlarına ve tuzaklı tünellere asker girmeden önce gönderilerek bubi tuzaklarını tespit etme.
- **KBRN Keşif Görevi:** Kimyasal, biyolojik ve radyasyon algılayıcı sensörler takılarak tehlikeli gaz sızıntısı olan binalara girip ortam ölçümü yapma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 9 (Saha Kanıtlanmış Seri Üretim)**
- [x] Zorlu Arazi ve Şok Kalifikasyon Testleri Tamamlandı
- [x] TSK ve Emniyet Genel Müdürlüğü (Bomba İmha Şubeleri) Envanterine Giriş
- [x] Meskun Mahal ve İç Güvenlik Operasyonlarında Aktif Kullanım
- [ ] Otonom Geri Dönüş ve Lidar Destekli Kapalı Alan 3D Haritalama Entegrasyonu
- [ ] BARKAN ve Diğer İnsansız Kara Araçlarıyla Müşterek Ağ Koordinasyonu

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
