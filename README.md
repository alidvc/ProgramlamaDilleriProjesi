# Gerçek Zamanlı Sözdizimi Vurgulayıcı

Bu proje, gerçek zamanlı sözdizimi vurgulama özelliği sunan bir GUI uygulamasıdır. Python ve Tkinter kullanılarak geliştirilmiştir ve herhangi bir sözdizimi vurgulama kütüphanesi kullanılmamıştır.

## Özellikler

- **Sözcüksel Analiz**: Tablo tabanlı durum diyagramı ile düzenli ifadeler kullanılarak token'lar ayrılır
- **Sözdizimsel Analiz**: Bottom-up shift-reduce parser ile token akışı bağlamdan bağımsız bir dilbilgisine göre doğrulanır
- **Gerçek Zamanlı Vurgulama**: Tkinter Text widget'ında token türlerine göre renkli vurgulama
- **GUI**: Kullanıcı dostu arayüz, hata mesajları ve gerçek zamanlı güncellemeler
- **Testler**: Birim testleri ile bileşenlerin doğruluğu kontrol edilir

## Dosya Yapısı

Project/
├── src/
│ ├── lexer.py # Sözcüksel analizci
│ ├── parser.py # Sözdizimsel analizci ve parser
│ ├── highlighter.py # Vurgulama mantığı
│ ├── gui.py # GUI uygulaması
│ ├── main.py # Ana uygulama başlatıcısı
├── docs/
│ ├── grammar.txt # Dilbilgisi tanımı
│ ├── Dokümantasyon.pdf # Tasarım dokümantasyonu
├── tests/
│ ├── test_lexer.py # Sözcüksel analizci testleri
│ ├── test_parser.py # Sözdizimsel analizci testleri
│ ├── test_highlighter.py # Vurgulama testleri
├── examples/
│ ├── sample_code.txt # Geçerli kod örneği
│ ├── invalid_code.txt # Hatalı kod örneği
├── README.md # Bu dosya
├── requirements.txt # Bağımlılıklar


## Kurulum

1. **Python Kurulumu**: Python 3.8 veya üzeri bir sürümün yüklü olduğundan emin olun.

2. **Bağımlılıkları Yükleme**: Proje kök dizininde aşağıdaki komutu çalıştırın:
   ```bash
   pip install -r requirements.txt
      ```

3. **Uygulamayı Çalıştırma**: Proje kök dizininde aşağıdaki komutu çalıştırın:
    ```bash
   python src/main.py
      ```
## Kullanım

Uygulama açıldığında, metin alanına kod yazabilirsiniz (örneğin, `if x = 42 + 10 // comment`).

Yazılan kod, gerçek zamanlı olarak analiz edilir ve token türlerine göre vurgulanır:

- **Anahtar kelimeler:** Mavi  
- **Tanımlayıcılar:** Siyah  
- **Sayılar:** Yeşil  
- **Operatörler:** Mor  
- **Yorumlar:** Gri  

Sözdizimi hataları, metin alanı altında **kırmızı bir etikette** gösterilir.

Örnek kodları test etmek için `examples/` klasöründeki `sample_code.txt` veya `invalid_code.txt` dosyalarını metin alanına kopyalayabilirsiniz.

## Testler

Birim testlerini çalıştırmak için proje kök dizininde şu komutu kullanın:

```bash
python -m unittest discover tests
```

## Dokümantasyon

- **grammar.txt**: Tanımlı dilbilgisinin formal tanımı.
- **Dokümantasyon.pdf**: Tasarım kararları ve yöntemlerin açıklaması.

## Makale

[Proje Makalesi]( https://docs.google.com/document/d/1Uv3gnT_9vbvMekNI20225fH9YNka1nWZL8r6Jky1ckM/edit?usp=sharing)

