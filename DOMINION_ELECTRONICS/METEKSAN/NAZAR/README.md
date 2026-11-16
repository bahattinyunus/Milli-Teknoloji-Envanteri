# 🔮 Proje: NAZAR (Lazer Elektronik Harp Sistemi)

<p align="center">
  <img src="https://img.shields.io/badge/TRL-9%20(Muharebe%20Kanıtlanmış)-00E676?style=for-the-badge&logo=shield&logoColor=white" alt="TRL 9" />
  <img src="https://img.shields.io/badge/DOMINION-ELECTRONICS-00f2fe?style=for-the-badge&logo=radar&logoColor=black" alt="Dominion" />
  <img src="https://img.shields.io/badge/ÜRETİCİ-METEKSAN-7928CA?style=for-the-badge&logo=probot&logoColor=white" alt="Üretici" />
  <img src="https://img.shields.io/badge/DURUM-OPERASYONEL%20%2F%20DzKK%20ENVANTERİ-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Durum" />
</p>

<p align="center">
  <img src="https://www.meteksan.com/uploads/nazar.jpg" alt="NAZAR" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>




---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
NAZAR Lazer Elektronik Harp Sistemi, Deniz Kuvvetleri Komutanlığı'nın kritik suüstü muharip unsurlarını (MİLGEM korvet ve fırkateynleri, TCG ANADOLU) 3. ve 4. nesil elektro-optik (EO) ve kızılötesi (IIR) arayıcı başlıklı gemisavar füzelerine (AShM) karşı korumak için METEKSAN Savunma tarafından geliştirilmiş dünyadaki en ileri yönlendirilmiş lazer karşı tedbir (DIRCM) sistemlerinden biridir.

Geleneksel chaff/flare veya nokta hava savunma füzelerinin (RAM, Phalanx) aksine NAZAR; çok bantlı yönlendirilmiş lazer enerjisi kullanarak tehdit füzeyi henüz onlarca kilometre uzaktayken optik penceresinden yakalar, dedektörünü kalıcı olarak körleştirir (Soft-Kill) veya termal tahribat yaratarak (Hard-Kill) rotasından saptırır. Bu teknoloji, mühimmat sınırlamasını ortadan kaldırarak sınırsız angajman derinliği kazandırmaktadır.

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Operasyonel Karşılık |
| :--- | :--- | :--- |
| **Dalga Boyu Yelpazesi** | Çok Bantlı (Multi-Spectral IR & Lazer Bandı) | IIR, SWIR, MWIR, LWIR dedektör körleme |
| **Etki Menzili** | Çift Haneli Kilometreler (Geniş Ufuk Ötesi) | Geleneksel CIWS menzilinin 3 katı |
| **Kapsama Alanı** | 360° Azimut, -10° ila +85° Elevasyon | Tam küresel gemi savunma kubbesi |
| **Reaksiyon Süresi** | < 1.5 saniye (Tehdit bildiriminden ışımaya) | Süpersonik füzelere karşı reaktif savunma |
| **Etki Mekanizması** | Dazzling (Körleştirme) + Damping (Tahrip) | Soft-Kill ve Hard-Kill hibrit taarruz |
| **Hedef Tipi** | IIR Başlıklı Gemisavar Füzeleri, Kamikaze İHA'lar | Güdümlü tüm optik tehditler |
| **Güç & Soğutma** | Dahili Jeneratör & Kapalı Devre Sıvı Soğutma | Gemi ana güç ağından bağımsız çalışabilme |

---

## 🧩 Alt Sistemler ve Elektronik Entegrasyonu
- **Geniş Bant Dedektör ve Tehdit Algılama Birimi:** Yaklaşan optik ve lazer güdümlü mühimmatın dalga boyunu anında tespit eden optik alıcılar.
- **Yüksek Hassasiyetli Lazer Taret Sistemi:** Deniz şartlarında gemi yalpalamasını nötralize eden cayro-stabilize yönlendirme platformu.
- **Çok Bantlı Lazer Kaynağı:** Farklı arayıcı başlık malzemelerine (InSb, HgCdTe) göre frekans değiştirebilen katı-hal lazer mimarisi.
- **ADVENT Savaş Yönetim Sistemi Entegrasyonu:** Geminin merkezi radarları, optik gözetleme sistemleri ve taktik konsolları ile iki yönlü tam senkronizasyon.

---

## 🎯 Görev Profili ve Muharebe Senaryoları
- **Asimetrik ve Füze Doyurma Saldırıları:** Aynı anda farklı yönlerden gelen çoklu IIR füzelerin ardışık olarak lazer enerjisiyle körleştirilmesi.
- **Mavi Vatan Karasuları Koruması:** Boğaz geçişleri ve adalar denizinde dar su yollarında kıyıdan ateşlenen güdümlü mühimmatların savuşturulması.
- **Kara Konuşlu Varyant (NAZAR-K):** Stratejik hava üsleri, radar mevkileri ve komuta merkezlerinin korunması için mobil treyler entegrasyonu.

---

## 🌐 Sistem Mimarisi ve Karşı Tedbir Döngüsü

```mermaid
flowchart TD
    subgraph ALGILAMA["Tehdit Algılama & Uyarı"]
        A1["ADVENT / Gemi Arama Radarı"] --> A2["Erken İhbar & Rota Tespiti"]
        A3["NAZAR Elektro-Optik Takip"] --> A4["Hassas Hedef Kilidi"]
    end

    subgraph ISIMA["Lazer Tahsis & Yönlendirme"]
        B1["Cayro-Stabilize Optik Taret"]
        B2["Çok Bantlı Lazer Kaynağı"]
    end

    subgraph KORLEME["Hedef İmhası / Soft-Kill"]
        C1["Dazzling (Optik Körleştirme)"]
        C2["Füze Arayıcı Başlık Doyumu"]
        C3["Rotadan Sapma & Denize Düşüş"]
    end

    A2 --> A3
    A4 --> B1
    B1 --> B2
    B2 --> C1
    C1 --> C2 --> C3
```

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası (TRL 9)
- [x] Lazer kaynağı ve optik yönlendirici prototip geliştirme fazı
- [x] Karada sabit test sahasında atışlı körleştirme ve dedektör imha testleri
- [x] DzKK TCG İSTANBUL ve MİLGEM platformlarında deniz kabul testleri
- [x] Deniz Kuvvetleri Komutanlığı envanterine kabul ve operasyonel görev icrası
- [/] Mobil kara konuşlu NAZAR-K sisteminin seri üretim teslimatları

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
