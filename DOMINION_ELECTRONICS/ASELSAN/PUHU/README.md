# 📻 Proje: ASELSAN PUHU (Taşınabilir Dinleme ve Kestirim Sistemi)

<p align="center">
  <img src="https://img.shields.io/badge/TRL-9_Operasyonel-00E676?style=for-the-badge&logo=shield&logoColor=white" alt="TRL Seviyesi">
  <img src="https://img.shields.io/badge/Dominion-ELECTRONICS_%26_AI-blue?style=for-the-badge&logo=cpu&logoColor=white" alt="Dominion">
  <img src="https://img.shields.io/badge/Üretici-ASELSAN-0052cc?style=for-the-badge&logo=target&logoColor=white" alt="Üretici">
  <img src="https://img.shields.io/badge/Muharebe_Durumu-Combat_Proven_%28Manpack%29-ff0055?style=for-the-badge&logo=flame&logoColor=white" alt="Muharebe Durumu">
</p>

<p align="center">
  <img src="https://www.aselsan.com.tr/uploads/puhu.jpg" alt="PUHU" width="750" style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</p>




## 🛡️ Stratejik Tanım & Doktriner Öncelik
**ASELSAN PUHU**, taktik sahada en ön hatta görev yapan özel kuvvetler, komando timleri, hudut birlikleri ve istihbarat unsurları için geliştirilmiş, tek bir askerin sırt çantasında taşıyabildiği (Manpack) ya da hafif taktik araç üzerine dakikalar içinde monte edilebilen Taşınabilir V/UHF Taktik Dinleme ve Yön Kestirim Sistemidir (COMINT / Direction Finding - DF). Düşmanın telsiz konuşmalarını, frekans atlamalı yayınlarını ve el telsizlerini geniş bantta anında yakalayan PUHU; interferometrik yön bulma algoritmalarıyla konuşmanın yapıldığı coğrafi koordinatı harita üzerinde milimetrik hassasiyetle çıkararak ateş destek vasıtalarına (topçu bataryaları, SİHA'lar) anlık hedef koordinatı aktarır.

```mermaid
flowchart TD
    subgraph TacticalSignalDetection [Sinyal Yakalama & Yön Kestirimi]
        EnemyRadio[Düşman El Telsizi / Frekans Atlamalı Taktik Muhabere] --> CompactAntenna[Taşınabilir Kompakt DF Anten Dizini]
        CompactAntenna --> MultiReceiver[Çok Kanallı Sayısal Almaç Ünitesi]
        MultiReceiver --> InterfAlgorithm[Koralitatif İnterferometrik DF Algoritması]
    end

    subgraph OperatorInterface [Taktik Kullanıcı Terminali]
        InterfAlgorithm --> TabletGUI[Sağlamlaştırılmış Askeri Tablet Ekranı]
        GPS[Dahili Askeri GNSS & Pusula] --> TabletGUI
        TabletGUI --> MapPlot[Sayısal Askeri Haritada Kesin Hedef Koordinatı]
    end

    subgraph FireSupportHandoff [Ateş Destek Entegrasyonu]
        MapPlot -->|Taktik Veri Bağı / Telsiz Linki| Artillery[FIRTINA II Obüsü / BORAN Çekili Top]
        MapPlot -->|KEMENT Veri Bağı| UCAV[Bayraktar TB2 / AKINCI SİHA]
        Artillery & UCAV --> DirectStrike[Anlık Nokta Vuruşu ile Hedef İmhası]
    end
```

## 📊 Kapsamlı Teknik Özellikler

| Parametre | Değer / Açıklama |
| :--- | :--- |
| **Sistem Tipi** | Taşınabilir Muhabere Elektronik İstihbarat ve Yön Kestirim Sistemi (COMINT/DF) |
| **Frekans Kapsamı** | V/UHF Bantları (20 MHz - 3.000 MHz Geniş Kapsama) |
| **Yön Kestirim Doğruluğu** | < 2° RMS (Gelişmiş koralitatif interferometrik algoritmalar ile) |
| **Konfigürasyon** | Taşınabilir Sırt Çantalı (Manpack), Sabit Mevzi veya Hafif Taktik Araç Üstü |
| **Kurulum Süresi** | Tek personel tarafından 3 dakikadan kısa sürede operasyona hazır hale getirme |
| **Batarya Ömrü** | Dahili askeri lityum iyon bataryalar ile 12+ saat kesintisiz görev süresi |
| **Konumlandırma** | Entegre askeri GPS/GNSS ve dahili elektronik pusula |
| **Harita Desteği** | Sayısal taktik askeri vektörel ve uydu haritası katmanları |
| **Ağırlık** | Sınıfının en hafif manpack çözümü (< 15 kg tam sırt çantası konfigürasyonu) |
| **Çalışma Sıcaklığı** | -30°C ile +50°C (MIL-STD-810G çevre koşullarına tam uyum) |

## 🧩 Alt Sistemler ve Aviyonik/Elektronik Entegrasyonu
- **Kompakt Çok Elemanlı DF Anteni:** Hafif kompozit direk üzerine tek hareketle kilitlenen hassas anten yapısı.
- **Geniş Bant Çok Kanallı Sayısal Almaç:** Frekans atlamalı (frequency hopping) telsiz yayınlarını dahi kaçırmayan paralel dinleme mimarisi.
- **Sağlamlaştırılmış Taktik Tablet:** Güneş ışığı altında okunabilir, su geçirmez, dokunmatik askeri kullanıcı arayüzü.
- **Otomatik Ses Kayıt ve Sinyal Analizi:** Telsiz konuşmalarını otomatik kaydedip ses frekans analizini yapan sayısal işlemci.
- **Ateş İdare Sistemi Arayüzü:** Belirlenen koordinatları tek dokunuşla milli topçu atış idare yazılımlarına iletme kabiliyeti.

## 🎯 Görev Profili, Muharebe Senaryoları & Operasyonel Yetenek
- **Taktik İstihbarat ve Keşif:** Düşman unsurlarının dağlık ve ormanlık arazideki gizli mevzilerinden yaptığı telsiz yayınlarını yakalama.
- **Sensörden Silaha Anlık Angajman:** Tespit edilen telsiz koordinatını 30 saniye içinde SİHA'ya veya en yakın topçu birliğine aktararak düşmanı hareket edemeden imha etme.
- **Sınır ve Karakol Güvenliği:** Sınır hattına yaklaşan sızma gruplarının kendi aralarındaki telsiz konuşmalarını erken aşamada ikaz etme.
- **Muharebe Başarısı:** TSK ve Güvenlik Güçlerinin tüm terörle mücadele ve sınır ötesi harekatlarında yüzlerce hedef tespiti gerçekleştirmiştir.

## 🚀 TRL Seviyesi ve Gelişim Yol Haritası
- **Mevcut Seviye: TRL 9 (Seri Üretimde / Muharebe Alanında Yaygın Kullanımda - Combat Proven)**
- [x] Manpack ve araç üstü prototip tasarımları ve zorlu saha kalifikasyonları.
- [x] TSK, Jandarma Genel Komutanlığı ve Emniyet Genel Müdürlüğü'ne yüzlerce adet teslimat.
- [x] Sınır içi ve sınır ötesi operasyonlarda aktif ve kesintisiz saha kullanımı.
- [x] Yeni nesil PUHU-2 taşınabilir sisteminin geliştirilmesi ve sahaya sürülmesi.
- [ ] Yapay zeka tabanlı konuşmacı tanıma ve ses analizi modüllerinin entegrasyonu.

---
[⬅️ Üst Dizine](../README.md) | [🏛️ Dominion Hub](../../README.md) | [🏠 Ana Sayfa](../../../README.md)
