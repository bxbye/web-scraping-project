# Proje Adi
Web Kazima Test Uygulamasi

### Yazar
*Kadir KAYA*

kadirkaya2050@gmail.com

## Kullanilan Teknolojiler
1. Python
2. MongoDB
3. BeautifulSoup and Requests libraries
4. OOP Principles

## Kutuphane Yuklemeleri
##### download mongodb to Mac OS
```bash
brew install mongodb-community@6.0
```
mongodb documents page: [how to install](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

##### download bs4 and requests
```bash
pip3 install beautifulsoup4
pip3 install requests
```

##### import to project
```bash
from bs4 import BeautifulSoup
import requests
```

## Programin Ozellikleri
Proje icerisinde web kazima yapilabilen 2 adet website vardir. Uygulama tasarimindan dolayi bu sayi artirilabilmektedir. Cunku her site icin 2 adet class tanimlanmistir. Yeni bir sitede kazima yapilacaksa onun icin 2 adet daha class eklenip bu islem yapilabilir.

Bu 2 class; ProductPage ve CategoryPage class'laridir. Bunlar parent class'dir. Bunlardan turetilen sitelere farkli ozellikler de eklenebilir.
CategoryPage class'i kategori sayfasinin linkini alir ve o kategorideki tum sayfalari tarar. Kategorinin altindaki tum kitap(product) linklerini toplar ve bize verir. Bunu class icindeki get_all_product_links() metoduyla yapar.

ProductPage class'i ise urunun sayfasindaki html etiketlerinde kazima yapar. Urune ait tum detay bilgiler buradan kazinir. Su an sadece title, publisher, writers, price bilgileri kazinmaktadir.

> kitapsepeti.com sitesinde page parametresi yanlis da olsa ilk sayfaya yonlendirdigi icin bu sitenin CategoryPage class'ina set_pagination_limit() metodu eklenmistir. Son sayfa bilgisini bu metod ile kaziyip diger islemlerde kullaniyoruz.

## Proje nasil Calistirilir
Projenin root klasorunde 4 adet python(.py) dosyasi mevcuttur. Bunlari calistirarak istenen islemlerin gerceklestigini goruntuleyebiliriz.

mongodb servisinin bu projenin calistirilmak istendigi bilgisayarda calisir halde olmasi gerekmektedir. kurulumu yukadirdaki mongodb linki uzerinden gerceklestirdikten sonra bu islem yapilabilir.

```bash
brew services start mongodb-community@6.0
```

Asagidaki komutlar projenin root klasorunde calistirilmalidir.

> kitapyurdu.com sitesinde arama kismindan **python** kelimesini arattigimizda satistakiler butonuna bastigimizda filtrelenen tum kitaplari bu komutla calistirdigimiz python dosyasi web kazima yaparak veritabanina kaydetmektedir.
```bash
python3 ky_python_sale.py
```
> kitapyurdu.com sitesindeki herhangi bir kategoriye girdigimiz zaman, o kategorideki tum kitaplari listeledigimizde tum kitaplari bizim icin web kazima yaparak veritabanina kaydeden python dosyasi asagidaki komutla calistirilmaktadir.
```bash
python3 ky_pagination.py
```
> kitapsepeti.com sitesinde arama kismindan **python** kelimesini arattigimizda satistakiler butonuna bastigimizda filtrelenen tum kitaplari bu komutla calistirdigimiz python dosyasi web kazima yaparak veritabanina kaydetmektedir.
```bash
python3 ks_python_sale.py
```
> kitapsepeti.com sitesindeki herhangi bir kategoriye girdigimiz zaman, o kategorideki tum kitaplari listeledigimizde tum kitaplari bizim icin web kazima yaparak veritabanina kaydeden python dosyasi asagidaki komutla calistirilmaktadir.
```bash
python3 ks_pagination.py
```

#### Projede gelistirilmeye ihtiyac olan konular
Web kazima islemleri yapilirken teker teker once kategorilerdeki linkler kaziniyor, bu islem tamamlaninca da urun sayfalari tek tek kaziniyor. Bazi kategorilerde 1000 adetten fazla urun mevcut oldugu icin bu islemlerin tamamlanmasi oldukca fazla zaman aliyor. Bu sorunu gidermek icin asenkron programlama ozellikleri kullanarak ayni anda birden fazla sayfanin kazima islemi yaptirilabilirdi. Fakat baslangicta algoritmami kurarken asenkron calisma ozelligine gore tasarlamamistim. Oncelik,  verilerin dogru bir sekilde kazinmasi ve veritabanina kaydedilmesiydi.
Projeyi tamamladiktan sonra asenkron ozelliklerini eklemek belki de projeyi bastan yazmama sebep olur dusuncesiyle zaman maliyetimi dusurmek icin o ise baslamadim.
