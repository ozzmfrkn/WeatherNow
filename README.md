# WeatherNow

## Proje Hakkında
WeatherNow, OpenWeatherMap API'sini kullanarak gerçek zamanlı hava durumu verilerini çeken ve modern bir arayüzle sunan bir web uygulamasıdır. Kullanıcılar, şehir adı girerek güncel hava durumu (sıcaklık, hissedilen sıcaklık, nem, rüzgar hızı ve durum) ile 3 günlük tahmini ayrı sekmelerde görebilir. Uygulama, Bootstrap (Slate teması), Font Awesome ve Animate.css ile şık ve duyarlı bir tasarım sunar.

## Kurulum

1. Depoyu klonla:
   ```bash
   git clone https://github.com/kullaniciadi/WeatherNow.git
   cd WeatherNow

2. Gerekli bağımlılıkları kur:
    pip3 install flask requests

3. API anahtarını ayarla:
    API_KEY = "sizin_api_anahtariniz_buraya"

4. Uygulamayı çalıştır:
    python3 app.py

5. Tarayıcıda aç:
    Adres: http://127.0.0.1:5000

Kullanım
    Ana sayfada bir şehir adı girin (örneğin, "Ankara") ve "Hava Durumunu Göster" butonuna tıklayın.
    "Güncel Durum" sekmesinde anlık hava durumu detaylarını, "3 Günlük Tahmin" sekmesinde gelecek 3 günün tahminlerini görün.
    Geçersiz şehir girildiğinde uyarı mesajı (SweetAlert2) çıkar.
Kullanılan Teknolojiler
    Python: Flask ile arka uç geliştirme.
    HTML/CSS: Bootstrap (Slate teması), Font Awesome ikonları, Animate.css animasyonları.
    JavaScript: Dinamik arka plan ve sekme geçiş animasyonları.
    API: OpenWeatherMap için hava durumu verileri.

Ekip:
    Furkan

Zorluklar ve Çözümler
    Zorluk 1: Flask kurulum hatası (ModuleNotFoundError).
        Çözüm: pip3 install flask requests ile bağımlılıklar kuruldu, yol ayarları yapıldı.
    Zorluk 2: Arayüzde çiftleme sorunu.
        Çözüm: HTML grid yapısı düzeltildi, tarayıcı önbelleği temizlendi.
    Zorluk 3: API anahtarı hataları.
        Çözüm: Anahtar test edildi ve config.py güncellendi.

Ek Bilgi
    Proje, COMP1002 - Advanced Python dersi için geliştirilmiştir.
    Teslim tarihi: 25 Mayıs 2025, 23:59.


---

### **Nasıl Kullanılır?**

1. **Dosyayı Oluştur**:
   - Terminalde `WeatherNow` klasörüne git:
     ```bash
     cd ~/Desktop/WeatherNow