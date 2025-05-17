# 🏋️‍♂️ Gelişmiş Sporcu Takip Sistemi - Python GUI Uygulaması

Bu proje, sporcuların antrenmanlarını, gelişimlerini ve performanslarını takip etmek için geliştirilmiş kapsamlı bir Python grafik kullanıcı arayüzü (GUI) uygulamasıdır. `customtkinter` kütüphanesi ile modern bir görünüme sahip olan bu uygulama, `MySQL` veritabanı ile güvenilir veri yönetimi sunar.

---

## 🚀 Özellikler

* **🔐 Güvenli Kullanıcı Girişi:** Kullanıcıların sisteme güvenli bir şekilde giriş yapmasını sağlar. İlk çalıştırmada otomatik olarak "admin" kullanıcı adı ve "1234" şifresi ile bir yönetici hesabı oluşturulur.
* **🧍 Sporcu Yönetimi:**
    * Yeni sporcuların ad, soyad, spor dalı, doğum tarihi ve cinsiyet bilgilerini kaydetme.
    * Kayıtlı sporcuları kolayca listeleme ve yönetme.
* **🏋️ Antrenman Takibi:**
    * Belirli sporcular için tarih, antrenman adı, süresi ve açıklaması gibi detayları içeren antrenman kayıtları oluşturma.
    * Sporcuları açılır menüden seçerek antrenmanları ilişkilendirme.
* **📊 İlerleme Kaydı:**
    * Sporcuların belirli tarihlerdeki kilo, tekrar ve not gibi ilerleme bilgilerini kaydetme.
    * Sporcuları açılır menüden seçerek ilerleme kayıtlarını ilişkilendirme.
* **📈 Performans Grafikleri:**
    * Seçilen bir sporcunun kilo ve tekrar bilgilerinin zaman içindeki değişimini gösteren interaktif grafikler oluşturma (`matplotlib` ile).
    * Grafikler, sporcunun performans gelişimini görsel olarak analiz etmeyi kolaylaştırır.
* **⚖️ Karşılaştırmalı Analiz:**
    * İki farklı sporcunun kilo gelişimlerini karşılaştırmalı olarak grafik üzerinde görüntüleme.
    * Ayrıca, seçilen bir sporcunun kendi geçmiş kilo ve tekrar verilerini de grafik üzerinde inceleme imkanı sunar.
* **✨ Modern ve Kullanıcı Dostu Arayüz:** `customtkinter` kütüphanesi sayesinde karanlık tema (dark mode) desteği ve modern widget'lar ile geliştirilmiş şık bir kullanıcı arayüzü.
* **🗓️ Tarih Seçimi:** `tkcalendar` kütüphanesi ile kolay ve kullanıcı dostu tarih seçimi imkanı.
* **💾 Güvenilir Veritabanı:** `MySQL` veritabanı ile sporcu, antrenman ve ilerleme verilerinin güvenli ve kalıcı olarak saklanması. Uygulama ilk kez çalıştırıldığında veritabanı ve tablolar otomatik olarak oluşturulur.
* **🖼️ Arka Plan Desteği:** Uygulamanın görsel çekiciliğini artıran özelleştirilebilir arka plan resmi özelliği (varsayılan olarak `image/bg.jpg` dosyası beklenmektedir).

---

## 🧱 Kullanılan Teknolojiler

* **Python 3.x:** Uygulamanın temel programlama dili.
* **`tkinter`:** Temel GUI bileşenleri için kullanılan standart Python kütüphanesi.
* **`customtkinter`:** Modern görünümlü ve özelleştirilebilir GUI bileşenleri sağlayan kütüphane.
* **`mysql-connector-python`:** Python uygulamalarının MySQL veritabanı ile iletişim kurmasını sağlayan bağlayıcı.
* **`tkcalendar`:** Kullanıcıların kolayca tarih seçebilmesi için takvim widget'ı.
* **`matplotlib`:** Veri görselleştirme ve grafik oluşturma kütüphanesi.
* **`Pillow (PIL)`:** Görüntü işleme yetenekleri sağlayan kütüphane (arka plan resmi için).

---

## ⚙️ Kurulum Talimatları

1.  **Gerekli Kütüphaneleri Yükleyin:**

    ```bash
    pip install customtkinter mysql-connector-python tkcalendar matplotlib Pillow
    ```

2.  **MySQL Kurulumu ve Yapılandırması:**

    * Eğer sisteminizde MySQL kurulu değilse, öncelikle MySQL Community Server'ı kurmanız gerekmektedir.
    * Uygulama, varsayılan olarak `localhost` üzerindeki bir MySQL sunucusuna bağlanmaya çalışır. Bağlantı bilgileri kod içinde şu şekilde tanımlanmıştır:

        ```python
        host="localhost",
        user="root",
        password="1234"
        ```

        Gerekirse bu bilgileri kendi MySQL kurulumunuza göre güncelleyin.


3.  **Uygulamayı Çalıştırın:**

    Uygulama dosyasını (genellikle `.py` uzantılı olan ana dosya) Python yorumlayıcısı ile çalıştırın:

    ```bash
    python ana_dosya_adı.py
    ```

    (Yukarıdaki `ana_dosya_adı.py` yerine gerçek dosya adınızı yazın.)

---

## 🖼️ Uygulama Arayüzünden Görseller

*(Bu bölüme uygulama arayüzünün ekran görüntülerini ekleyebilirsiniz. Örneğin:)*

### 🔐 Giriş Ekranı

![Giriş Ekranı](image/login.png)

### 🏠 Ana Menü

![Ana Menü](image/arayüz.png)

### 🧍 Sporcu Ekleme

![Sporcu Ekleme](image/sporcu_ekle.png)

### 🏋️ Antrenman Ekleme

![Antrenman Ekleme](image/antrenman_ekle.png)

### 📊 Performans Grafiği

![Performans Grafiği](image/grafik.png)

### ⚖️ Karşılaştırmalı Analiz

![Karşılaştırmalı Analiz](image/karsılastırma.png)  


---

## 👨‍💻 Geliştirici
    
###  Mehmet Akif Balcı
<br>

## Versiyon  1.0
---

