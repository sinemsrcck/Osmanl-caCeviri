# 📜 Osmanlıca Belge Analiz ve Çeviri Platformu
> **Görselden Günümüz Türkçesine:** Basılı Osmanlıca belgeleri mobil kamera aracılığıyla dijitalleştiren, görüntü kusurlarını iyileştiren, transkripsiyonunu çıkaran ve LLM desteğiyle günümüz Türkçesine sadeleştiren uçtan uca mobil platform.

## 📌 Proje Hakkında

Bu proje, tarihî ve matbu Osmanlıca belgelerin okunması ve anlaşılması süreçlerindeki zorlukları çözmek amacıyla geliştirilmiştir. Saha koşullarında (mobil kamera ile) çekilen belgelerdeki eğiklik, gölge ve düşük çözünürlük gibi problemleri **OpenCV** ile giderir; ardından metni **OCR**, **Transkripsiyon** ve **Büyük Dil Modelleri (LLM)** aşamalarından geçirerek kullanıcıya sunar.

### 🌟 Öne Çıkan Özellikler

* 📸 **Mobil Ön İşleme (OpenCV):** Eğiklik düzeltme (Deskew), perspektif hizalama ve noktalama işaretlerini koruyan gürültü temizleme.
* 🔍 **Arap Harfli Osmanlıca OCR:** Matbu metinler üzerinde optimize edilmiş karakter tanıma motoru.
* 🔤 **Aşamalı Transkripsiyon:** Kural tabanlı ve LLM destekli melez yapısıyla Osmanlıca metni Latin harflerine aktarma.
* 🤖 **LLM Sadeleştirme:** Eski kelimeleri ve karmaşık cümle yapılarını günümüz Türkçesine dönüştürme.
* ✍️ **Kullanıcı Onaylı Düzenleme (Human-in-the-Loop):** Her aşamada kullanıcının çıktılara müdahale edebildiği ve düzeltebildiği esnek arayüz. ??????
* 📱 **Uçtan Uca Mobil Deneyim:** React Native (Expo) ile geliştirilmiş, hızlı ve kullanıcı dostu arayüz.

## 🏗️ Sistem Mimarisi (Pipeline)

Proje 4 ana işlem modülünün ardışık (sequential) olarak çalışmasıyla sonuç üretir: