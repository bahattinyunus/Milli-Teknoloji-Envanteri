# 🛡️ Proje: HAVELSAN SİBER GÜVENLİK SÜİTİ (Milli Siber Savunma Mimarisi)

[![TRL](https://img.shields.io/badge/TRL-9_Saha_Kanıtlanmış-success?style=for-the-badge&logo=shield)](https://www.havelsan.com.tr)
[![Dominion](https://img.shields.io/badge/Dominion-ELECTRONICS-blue?style=for-the-badge&logo=cpu)](../../README.md)
[![Üretici](https://img.shields.io/badge/Üretici-HAVELSAN-red?style=for-the-badge)](../README.md)
[![Durum](https://img.shields.io/badge/Durum-Aktif_Hizmette-brightgreen?style=for-the-badge)](#)

<div align="center">
  <img src="../../../_ASSETS/defense_icon.png" alt="Dominion Electronics Varlık İkonu" width="120" />
</div>

> **Geliştirici:** HAVELSAN  
> **Sınıf:** Askeri Düzey Kurumsal ve Kritik Altyapı Siber Güvenlik Süiti (SIEM, SOAR, EDR, Malware Analizi)  
> **Stratejik Önem:** Cumhurbaşkanlığı, TSK askeri veri hatları, bakanlıklar, bankacılık ve kritik enerji şebekelerini yabancı siber güvenlik yazılımlarına (Splunk, QRadar, CrowdStrike) bağımlı kalmadan koruyan %100 milli siber savunma kalkanı.

---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
HAVELSAN Siber Güvenlik Süiti, siber uzayın modern harp doktrinlerinde 5. harekât alanı haline gelmesi doğrultusunda Türkiye'nin stratejik dijital varlıklarını gelişmiş kalıcı tehditlere (APT), fidye yazılımlarına (ransomware) ve devlet destekli siber saldırılara karşı korumak amacıyla geliştirilmiştir. Yabancı menşeili güvenlik ürünlerinin arka kapı (backdoor) barındırma riskini tamamen elimine eden sistem; gerçek zamanlı log yönetimi (SIEM), yapay zeka destekli siber olay müdahalesi (SOAR), uç nokta tehdit algılama (EDR) ve otomatik zararlı yazılım analiz laboratuvarını tek bir çatı altında birleştirir.

```mermaid
flowchart TD
    subgraph Siber_Tehdit_Kaynakları["Dış Tehditler & Saldırı Vektörleri"]
        APT["Devlet Destekli APT Grupları & Sıfır-Gün Saldırıları"]
        DDOS["DDoS & Ağ Taşkın Taarruzları"]
        RANSOM["Fidye Yazılımları & Casus Casus Yazılımlar"]
        INSIDER["İç Ağ Tehditleri & Veri Sızıntısı (DLP)"]
    end

    subgraph HAVELSAN_Siber_Merkezi["HAVELSAN Milli Siber Savunma Omurgası"]
        direction TB
        GOC["HAVELSAN Siber Güvenlik Operasyon Merkezi (SOC 7/24)"]
        SIEM["Milli SIEM (Büyük Veri & Log Korelasyon Motoru)"]
        SOAR["Milli SOAR (Yapay Zeka Destekli Otomatik Olay Müdahale)"]
        EDR["Kalkan Uç Nokta Tehdit Algılama ve Yanıt"]
        MAL["Zararlı Yazılım Analiz ve Dinamik Kum Havuzu (Sandbox)"]
        
        SIEM --> GOC
        EDR --> SIEM
        SIEM --> SOAR
        MAL <--> SOAR
    end

    subgraph Korunan_Stratejik_Altyapı["Kritik Ulusal Ağlar"]
        TSK["TSK Muhabere ve Karargah Ağları"]
        GOV["e-Devlet & Cumhurbaşkanlığı Dijital Altyapısı"]
        ENERGY["TEİAŞ / BOTAŞ Kritik Enerji ve SCADA Sistemleri"]
    end

    APT & DDOS & RANSOM & INSIDER -.->|Saldırı Girişimi| HAVELSAN_Siber_Merkezi
    SOAR ==>|Otomatik Karantina & IP Blokajı| Korunan_Stratejik_Altyapı
    GOC ==>|7/24 Taktik İzleme & Müdahale| Korunan_Stratejik_Altyapı
```

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Detay |
| :--- | :--- |
| **Yazılım Mimarisi** | Mikroservis Tabanlı, Yüksek Erişilebilir Dağıtık Büyük Veri Mimarisi |
| **Log İşleme Kapasitesi**| Saniyede 1.000.000+ EPS (Events Per Second) anlık korelasyon ve indeksleme |
| **Tehdit İstihbaratı** | Milli Tehdit İstihbarat Veri Tabanı + Global STIX/TAXII Entegrasyonu |
| **Analiz Yöntemleri** | Statik Kod Analizi, Dinamik Kum Havuzu (Sandbox) Davranış Analizi, Bellek Adli Bilişimi |
| **Yapay Zeka Yeteneği** | Anomali Tespiti, Kullanıcı ve Varlık Davranış Analizi (UEBA), Otomatik Oyun Kitabı (Playbook) |
| **Uyumluluk Standartları**| ISO 27001, Common Criteria EAL4+, Askeri Kripto ve Gizlilik Seviyeleri |
| **Dağıtım Modeli** | %100 Kurum İçi (On-Premise / Air-Gapped) & Güvenli Kamu Bulut Desteği |

---

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Milli SIEM / SOAR Korelasyonu:** Milyarlarca log satırı arasından saniyeler içinde anomaliyi tespit edip insan müdahalesi beklemeden saldırgan sunucuları güvenlik duvarlarında izole etme.
- **SCADA ve Endüstriyel Ağ Güvenliği:** Barajlar, nükleer/termik santraller ve boru hatlarının PLC cihazlarını hedef alan siber-fiziksel saldırıları protokol bazında ayrıştırma.
- **Askeri Platform Entegrasyonu:** Harp gemileri (ADVENT) ve hava araçlarının komuta kontrol ağlarının siber dayanıklılığını denetleyen uç nokta sensörleri.
- **Zararlı Yazılım Analiz Platformu (Sandbox):** Şüpheli e-posta ekleri ve dosyaları izole sanal makinelerde çalıştırarak sıfır-gün açıklarını deşifre etme.

---

## 🎯 Görev Profili, Muharebe Senaryoları & Mühimmat Yelpazesi
- **Kritik Kurum Savunması:** Devlet kurumlarına yönelik kimlik avı (phishing), fidye yazılımı ve veri hırsızlığı girişimlerinin gerçek zamanlı engellenmesi.
- **NATO ve Ulusal Siber Tatbikatlar:** Kilitli Kalkan (Locked Shields) ve Cyber Coalition tatbikatlarında Türkiye milli siber savunma kalkanı olarak birincil rol alma.
- **Siber İstihbarat ve Tehdit Avcılığı:** Düşman hacker gruplarının taktik, teknik ve prosedürlerini (TTP) önceden modelleyerek saldırı başlamadan önlem alma.

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye:** **TRL 9 (Saha Kanıtlanmış Hizmet ve Geniş Ölçekli Kullanım)**
- [x] Tüm Kritik Modüllerin Geliştirilmesi ve Güvenlik Sertifikasyonları
- [x] Cumhurbaşkanlığı, Bakanlıklar ve TSK Ağlarında Aktif 7/24 Koruma
- [x] Uluslararası NATO Siber Tatbikatlarında Üstün Başarı ve Doğrulama
- [x] Kritik Enerji ve Ulaştırma SCADA Ağlarına Tam Entegrasyon
- [ ] Kuantum Sonrası Kriptografi (PQC) ve LLM Destekli Otonom Siber Savunma Botları

---

[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
