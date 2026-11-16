# ✈️ Proje: ACMI POD (Hava Muharebesi Manevra Enstrümantasyon Podu)

<p align="center">
  <img src="https://img.shields.io/badge/TRL-9%20(Muharebe%20Kanıtlanmış)-00E676?style=for-the-badge&logo=shield&logoColor=white" alt="TRL 9" />
  <img src="https://img.shields.io/badge/DOMINION-ELECTRONICS-00f2fe?style=for-the-badge&logo=radar&logoColor=black" alt="Dominion" />
  <img src="https://img.shields.io/badge/ÜRETİCİ-SDT%20Savunma-7928CA?style=for-the-badge&logo=probot&logoColor=white" alt="Üretici" />
  <img src="https://img.shields.io/badge/DURUM-MUHAREBE%20KANITLANMIŞ%20%2F%20ENVANTERDE-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Durum" />
</p>

<p align="center">
  <img src="https://www.sdt.com.tr/uploads/acmi-pod.jpg" alt="ACMI POD" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>




---

## 🛡️ Stratejik Tanım & Doktriner Öncelik
ACMI (Air Combat Maneuvering Instrumentation) Podu, SDT Uzay ve Savunma Teknolojileri tarafından muharip jet pilotlarının gerçek uçuş koşullarında hava-hava ve hava-yer muharebe eğitimlerini en yüksek gerçekçilik seviyesinde gerçekleştirmeleri için geliştirilmiş ileri bir harici pod sistemidir. Muharip uçakların kanat ucu füze raylarına (AIM-9 Sidewinder / Bozdoğan istasyonlarına) takılan pod, gerçek mühimmat harcamadan füzelerin güdüm algoritmalarını sanal olarak çalıştırır.

Türk Hava Kuvvetleri'nin dünyaca ünlü "Anadolu Kartalı" (Anatolian Eagle) uluslararası tatbikatlarında standart olarak kullanılan SDT ACMI sistemi; yüzlerce uçağın katıldığı devasa hava muharebelerinde her uçağın 3B konumunu, hızını, tetiğe basma anını ve sanal füze vuruşlarını milisaniyelik hassasiyetle yer kontrol istasyonuna aktararak uçuş sonrası 3 boyutlu analiz (debriefing) imkanı sunar.

---

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Özellik | Operasyonel Karşılık |
| :--- | :--- | :--- |
| **Montaj Standardı** | AIM-9 / AIM-120 Kanat Ucu Standart Füze Rayı | Modifikasyonsuz hızlı tak-çalıştır |
| **Konumlandırma Hassasiyeti**| Santimetre Seviyesinde GPS + INS Entegrasyonu | Yüksek G altında kesintisiz telemetri |
| **Veri Bağı (Data Link)** | Yüksek Hızlı, Kriptolu RF Ağ Mimarisi | Podlar arası ve pod-yer istasyonu bağı |
| **Eşzamanlı Takip Kapasitesi**| 100+ Muharip Uçak ve Platform | Büyük ölçekli karma hava harekatı |
| **Sanal Silah Simülasyonu** | GÖKDOĞAN, BOZDOĞAN, AIM-120, AIM-9, Top | Gerçek mühimmat kinematiği simülasyonu |
| **Maksimum Manevra Limiti** | -3G ila +9G Muharebe Manevrası | Süpersonik uçuş şartlarına dayanıklı |
| **Kayıt Süresi** | 8+ Saat Dahili Katı Hal Kayıt Ünitesi | Tam uçuş verisinin kara kutu kaydı |

---

## 🧩 Alt Sistemler ve Aviyonik Entegrasyonu
- **Dahili Ataletsel Seyrüsefer ve GNSS Birimi:** Yüksek dinamikli askeri GPS/INS sensör paketi ile anlık tutum ve koordinat tayini.
- **Hava Veri Bilgisayarı Sensörleri:** Pod üzerindeki pitot tüpleri ve basınç algılayıcılarla bağımsız hücum açısı (AoA) ve Mach hızı ölçümü.
- **Gerçek Zamanlı Silah Simülasyon Motoru (Real-Time Kill Notification):** Pilot atış yaptığında hedefin vurulup vurulmadığını anında hesaplayarak pilota kask içi sesli ikaz iletir.
- **Yer Kontrol ve Debriefing İstasyonu:** Görev bitiminde pilotların uçuşlarını her açıdan 3B olarak yeniden izleyebileceği interaktif analiz yazılımı.

---

## 🎯 Görev Profili ve Muharebe Senaryoları
- **İt Dalaşı (WVR - Within Visual Range) Eğitimi:** Yüksek G kuvvetleri altında yakın hava muharebesinde pilot reaksiyonlarının ve nişan alma açılarının analizi.
- **Görüş Ötesi (BVR - Beyond Visual Range) Taktikleri:** Elektronik harp altında radar güdümlü uzun menzilli füze taktiklerinin denenmesi.
- **Uluslararası İhracat:** Pakistan Hava Kuvvetleri'nin JF-17 Block III filolarına ihraç edilerek başarısını küresel çapta kanıtlamıştır.

---

## 🌐 Sistem Mimarisi ve Gerçek Zamanlı Eğitim Ağı

```mermaid
flowchart TD
    subgraph HAVADA["Havadaki Muharip Jetler (Podlar Arası Ağ)"]
        F1["F-16 Kol Lideri (ACMI Pod)"]
        F2["F-16 Numara (ACMI Pod)"]
        F3["Düşman / Red Air (ACMI Pod)"]
    end

    subgraph TELEMETRI["Kriptolu RF Veri Bağı"]
        T1["Pod-to-Pod Sanal Angajman"]
        T2["Pod-to-Ground Canlı Telemetri"]
    end

    subgraph YER["Yer Kontrol & 3B Debriefing"]
        Y1["Canlı Tatbikat İzleme Ekranı"]
        Y2["Gerçek Zamanlı Vuruş Teyidi (Kill/No-Kill)"]
        Y3["Uçuş Sonrası 3B Debriefing Tiyatrosu"]
    end

    F1 <-->|P2P Ağ| F2
    F2 <-->|P2P Ağ| F3
    F1 & F2 & F3 -->|Telemetri İletimi| T2
    T2 --> Y1 --> Y2 --> Y3
```

---

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası (TRL 9)
- [x] Pod aerodinamik yapısı ve kanat ucu mukavemet testlerinin tamamlanması
- [x] Anadolu Kartalı tatbikatlarında binlerce sorti uçuş tecrübesi (Combat Proven)
- [x] Türk Hava Kuvvetleri F-16 filolarında standart envanter sistemi olması
- [x] Pakistan Hava Kuvvetleri JF-17 uçakları için başarılı ihracat teslimatı
- [/] KAAN ve HÜRJET platformları için yeni nesil dahili gömülü ACMI kütüphanelerinin geliştirilmesi

---

## 🔗 İç Dizin Navigasyonu
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
