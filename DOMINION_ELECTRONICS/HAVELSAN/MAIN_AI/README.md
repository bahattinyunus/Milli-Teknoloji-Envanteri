# 🧠 Proje: HAVELSAN MAIN AI (Milli Kurumsal Büyük Dil Modeli)

[![TRL](https://img.shields.io/badge/TRL-7%2F8_Pilot_Hizmette-yellowgreen?style=for-the-badge&logo=shield)

<p align="center">
  <img src="https://www.havelsan.com.tr/uploads/main-ai.jpg" alt="MAIN AI" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>
](https://www.havelsan.com.tr)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-HAVELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Kamu_ve_Savunma_Kullanımında-brightgreen?style=for-the-badge)](#)

<div align="center">
  
</div>

> **Geliştirici:** HAVELSAN  
> **Sınıf:** Güvenli ve Kapalı Devre Kurumsal Büyük Dil Modeli (LLM) & Üretken Yapay Zeka (GenAI) Platformu  
> **Stratejik Önem:** Türkiye'nin kamu kurumları, askeri karargahları ve savunma sanayii kuruluşlarının "Çok Gizli" dereceli verilerini yabancı bulut ve yapay zeka sunucularına (OpenAI, Microsoft, Google) göndermeksizin, tamamen kurum sunucularında (On-Premise / Air-Gapped) çalıştıran milli yapay zeka asistanı ("Türkiye'nin Savunma GPT'si").

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
HAVELSAN MAIN (Multifunctional Artificial Intelligence Network), ulusal veri egemenliği doktrini doğrultusunda kurumların stratejik bilgi birikimini koruyarak üretken yapay zeka devriminden güvenle faydalanmalarını sağlamak amacıyla tasarlanmış milli kurumsal büyük dil modelidir. Şubatı 2024'te kamuoyuna tanıtılan sistem; Türkçenin zengin morfolojik ve eklemeli yapısına tam uyumlu olarak milyarlarca tokenlik Türkçe veri kümesiyle eğitilmiştir. Gelişmiş Bilgi Getirimi ile Zenginleştirilmiş Üretim (RAG) mimarisi sayesinde kurumların binlerce sayfalık gizli şartnamelerini, askeri doktrinlerini, hukuki mevzuatlarını ve yazılım kaynak kodlarını indeksleyerek halüsinasyonsuz, kaynak göstererek anında analiz eder ve özetler.

```mermaid
flowchart TD
    subgraph Kurumsal_Gizli_Veri_Havuzu["Kurum İçi Güvenli Veri Kaynakları (Air-Gapped)"]
        DOCS["Gizli Askeri Şartnameler & Teknik Raporlar"]
        LEGAL["Kamu Mevzuatı & Hukuki Belgeler"]
        CODE["Milli Savunma Yazılım Kaynak Kodları"]
    end

    subgraph MAIN_AI_Cekirdek_Mimarisi["HAVELSAN MAIN AI Çekirdeği"]
        direction TB
        PARSE["Güvenli Doküman Ayrıştırma & OCR Motoru"]
        EMBED["Milli Türkçe Gömme (Embedding) Modeli"]
        VDB["Yüksek Hızlı Vektör Veritabanı (Vector DB)"]
        RAG["Semantik Arama & RAG Orkestrasyonu"]
        LLM["MAIN Türkçe Optimize Edilmiş Büyük Dil Modeli (LLM)"]
        GUARD["Güvenlik Filtresi & Veri Sızıntısı Önleme (DLP/Prompt Injection Guard)"]
        
        DOCS & LEGAL & CODE ==> PARSE
        PARSE --> EMBED --> VDB
        VDB <--> RAG
        RAG <--> LLM
        LLM --> GUARD
    end

    subgraph Son_Kullanıcı_Ve_Sistemler["Kullanım Alanları"]
        USER["Askeri Karargah / Kamu Yöneticisi Arayüzü"]
        DEV["Savunma Yazılım Mühendisi (Kod Üretimi/Analizi)"]
        C4I["ADVENT / HAKİM Karar Destek Ajanı"]
    end

    GUARD ==>|Doğrulanmış & Kaynak Atıflı Cevap| USER
    GUARD ==>|Milli Kod Üretimi & Güvenlik Denetimi| DEV
    GUARD ==>|Taktik Bilgi & Rapor Özetleme| C4I
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Model Mimarisi** | Transformer Tabanlı Derin Öğrenme / Causal Decoder LLM Mimarisi |
| **Dil Uzmanlığı** | Türkçe (Öncelikli Yüksek Morfolojik Doğruluk) ve İngilizce |
| **Dağıtım Modeli** | %100 Kurum İçi Donanım (On-Premise), İzole Ağ (Air-Gapped) ve Güvenli Özel Bulut |
| **Bağlam Penceresi (Context)**| 8K - 32K+ Token (Geniş doküman ve kitapçık analiz kapasitesi) |
| **Arama & Geri Çağırma (RAG)**| Hibrit Arama (Dense Vector Search + Sparse BM25) ile Sıfır Halüsinasyon Prensibi |
| **Donanım Uyumluluğu** | NVIDIA Tensor Core GPU Sunucuları (A100, H100, L40S) & Yerli Hızlandırıcı Kartlar |
| **Veri Güvenliği Seviyesi** | İnternet bağlantısı gerektirmez, veri dışarı sızmaz, loglar kurumda kalır |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **RAG (Retrieval-Augmented Generation) Motoru:** Kullanıcının sorduğu soruya karşılık kurum içi belgelerden birebir alıntı yaparak cevabın altına sayfa numarası ve paragraf referansı ekleme.
- **Askeri Kod Üretimi ve Güvenlik Denetimi:** C/C++, Python, Ada ve Java dillerinde savunma yazılımları geliştirilirken güvenlik açıklarını (Buffer Overflow, SQLi) tespit eden dahili model.
- **Komuta Kontrol (C4I) Entegrasyonu:** Taktik harekat merkezlerinde gelen yüzlerce sayfalık istihbarat ve durum raporunu tek paragraflık yönetici özetine dönüştürme.
- **Prompt Enjeksiyon Koruması:** Kullanıcı tarafından gelebilecek manipülatif ve güvenlik duvarlarını delmeye yönelik "Jailbreak" girişimlerini engelleyen emniyet katmanı.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Kamu Kurumlarında Karar Destek:** Bakanlıklar ve devlet dairelerinde kanun ve yönetmeliklere uygunluk denetimlerini saniyeler içinde tamamlama.
- **Askeri Doktrin ve İstihbarat Analizi:** Uydu fotoğrafları raporları ve saha keşif tutanaklarını ilişkilendirerek düşman birlik hareketlerini sentezleme.
- **Gizli AR-GE Desteği:** ASELSAN, TUSAŞ, ROKETSAN ve HAVELSAN mühendislerine patent ve tasarım aşamalarında internete çıkmadan yapay zeka asistanlığı sağlama.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 7/8 (Sistem Operasyonel Ortamda Kanıtlandı / Pilot Kurulumlar Aktif)**
- [x] Temel Model Eğitimi ve Türkçe Dil Yetenekleri Kalifikasyonu (Şubat 2024 Lansmanı)
- [x] Kamu Kurumları ve Savunma Şirketlerinde Kapalı Devre Pilot Dağıtımlar
- [x] Güvenli RAG ve Kurumsal Arama Modüllerinin Entegrasyonu
- [ ] Çok Modlu (Multimodal - Ses, Görüntü, Radar Sinyali İşleme) Yeteneklerin Eklenmesi
- [ ] Taktik Sahada Askeri Araç Üstü Kompakt Donanımlarda Çalışabilen Hafif Sürüm (Edge MAIN)

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
