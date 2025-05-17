import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
import mysql.connector
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import os

class SporcuTakipApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sporcu Takip Sistemi")
        self.root.geometry("800x600")
        self.db = self.connect_db()
        self.cursor = self.db.cursor()
        self.create_tables()
        self.add_background()
        self.login_screen()
        self.root.mainloop()

    def connect_db(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS sporcu_takip")
        cursor.execute("USE sporcu_takip")
        db.database = "sporcu_takip"
        return db

    def create_tables(self):
        # Kullanıcılar tablosu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS kullanicilar (
                id INT AUTO_INCREMENT PRIMARY KEY,
                kullanici_adi VARCHAR(50) UNIQUE,
                sifre VARCHAR(50)
            )
        """)
        # Varsayılan kullanıcı ekleme (ilk çalıştırmada)
        self.cursor.execute("SELECT COUNT(*) FROM kullanicilar")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre) VALUES (%s, %s)", ("admin", "1234"))
        
        # Sporcular tablosu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sporcular (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ad VARCHAR(100),
                soyad VARCHAR(100),
                spor_dali VARCHAR(100),
                dogum_tarihi DATE,
                cinsiyet VARCHAR(10)
            )
        """)
        # Antrenmanlar tablosu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS antrenmanlar (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sporcu_id INT,
                tarih DATE,
                ad VARCHAR(100),
                sure INT,
                aciklama TEXT,
                FOREIGN KEY (sporcu_id) REFERENCES sporcular(id)
            )
        """)
        # İlerlemeler tablosu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ilerlemeler (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sporcu_id INT,
                tarih DATE,
                kilo FLOAT,
                tekrar INT,
                notlar TEXT,
                FOREIGN KEY (sporcu_id) REFERENCES sporcular(id)
            )
        """)
        self.db.commit()

    def add_background(self):
        # Arka plan resmi yükleme (resim dosyasının yolunu güncelleyin)
        image_path = "image/bg.jpg"  # Resmi proje klasörüne ekleyin
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((800, 600), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            print("Arka plan resmi bulunamadı:", image_path)

    def login_screen(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
                
            window_width = 600  # İstediğiniz genişlik
        window_height = 400 # İstediğiniz yükseklik

        # Ekran boyutlarını al
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Pencereyi ortalamak için x ve y koordinatlarını hesapla
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        # Pencerenin geometrisini ayarla (konum + boyut)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Giriş Yap", font=("Arial", 24, "bold")).pack(pady=20)
        kullanici_adi = ctk.CTkEntry(frame, placeholder_text="Kullanıcı Adı", width=250)
        kullanici_adi.pack(pady=10)
        sifre = ctk.CTkEntry(frame, placeholder_text="Şifre", show="*", width=250)
        sifre.pack(pady=10)

        def giris_yap():
            self.cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = %s AND sifre = %s",
                               (kullanici_adi.get(), sifre.get()))
            if self.cursor.fetchone():
                frame.destroy()
                self.main_screen()
            else:
                messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

        ctk.CTkButton(frame, text="Giriş Yap", command=giris_yap, width=200).pack(pady=20)

    def main_screen(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()

        # Pencere boyutlarını al
        window_width = 800  # İstediğiniz genişlik
        window_height = 600 # İstediğiniz yükseklik

        # Ekran boyutlarını al
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Pencereyi ortalamak için x ve y koordinatlarını hesapla
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        # Pencerenin geometrisini ayarla (konum + boyut)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        title = ctk.CTkLabel(self.root, text="Sporcu Takip Sistemi", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        buttons = [
            ("Sporcu Ekle", self.add_sporcu),
            ("Antrenman Ekle", self.add_antrenman),
            ("İlerleme Kaydı", self.add_ilerleme),
            ("Performans Grafiği", self.show_graph),
            ("Karşılaştırmalı Analiz", self.compare_performance)
        ]
        for text, cmd in buttons:
            ctk.CTkButton(self.root, text=text, command=cmd, width=200, bg_color='black', fg_color='black').pack(pady=25)
            
    def add_sporcu(self):
        win = ctk.CTkToplevel(self.root)
        win.title("Sporcu Ekle")
        win.geometry("400x400")
        win.attributes("-topmost", True)  # Pencereyi üstte tut
        ad = ctk.CTkEntry(win, placeholder_text="Ad"); ad.pack(pady=5)
        soyad = ctk.CTkEntry(win, placeholder_text="Soyad"); soyad.pack(pady=5)
        dal = ctk.CTkEntry(win, placeholder_text="Spor Dalı"); dal.pack(pady=5)
        tarih = DateEntry(win); tarih.pack(pady=5)
        cinsiyet = ctk.CTkEntry(win, placeholder_text="Cinsiyet"); cinsiyet.pack(pady=5)

        def kaydet():
            self.cursor.execute("""
                INSERT INTO sporcular (ad, soyad, spor_dali, dogum_tarihi, cinsiyet)
                VALUES (%s, %s, %s, %s, %s)
            """, (ad.get(), soyad.get(), dal.get(), tarih.get_date(), cinsiyet.get()))
            self.db.commit()
            messagebox.showinfo("Başarılı", "Sporcu eklendi")
            win.destroy()

        ctk.CTkButton(win, text="Kaydet", command=kaydet).pack(pady=20)

    def add_antrenman(self):
        win = ctk.CTkToplevel(self.root)
        win.title("Antrenman Ekle")
        win.geometry("400x400")
        win.attributes("-topmost", True)
        self.cursor.execute("SELECT id, ad FROM sporcular")
        sporcular = [f"{r[0]} - {r[1]}" for r in self.cursor.fetchall()]
        box = ctk.CTkComboBox(win, values=sporcular); box.pack(pady=5)
        tarih = DateEntry(win); tarih.pack(pady=5)
        ad = ctk.CTkEntry(win, placeholder_text="Antrenman Adı"); ad.pack(pady=5)
        sure = ctk.CTkEntry(win, placeholder_text="Süre (dk)"); sure.pack(pady=5)
        aciklama = ctk.CTkEntry(win, placeholder_text="Açıklama"); aciklama.pack(pady=5)

        def kaydet():
            sporcu_id = int(box.get().split(" - ")[0])
            self.cursor.execute("""
                INSERT INTO antrenmanlar (sporcu_id, tarih, ad, sure, aciklama)
                VALUES (%s, %s, %s, %s, %s)
            """, (sporcu_id, tarih.get_date(), ad.get(), sure.get(), aciklama.get()))
            self.db.commit()
            messagebox.showinfo("Başarılı", "Antrenman kaydedildi")
            win.destroy()

        ctk.CTkButton(win, text="Kaydet", command=kaydet).pack(pady=20)

    def add_ilerleme(self):
        win = ctk.CTkToplevel(self.root)
        win.title("İlerleme Kaydı")
        win.geometry("400x400")
        win.attributes("-topmost", True)
        self.cursor.execute("SELECT id, ad FROM sporcular")
        sporcular = [f"{r[0]} - {r[1]}" for r in self.cursor.fetchall()]
        box = ctk.CTkComboBox(win, values=sporcular); box.pack(pady=5)
        tarih = DateEntry(win); tarih.pack(pady=5)
        kilo = ctk.CTkEntry(win, placeholder_text="Kilo"); kilo.pack(pady=5)
        tekrar = ctk.CTkEntry(win, placeholder_text="Tekrar"); tekrar.pack(pady=5)
        notlar = ctk.CTkEntry(win, placeholder_text="Notlar"); notlar.pack(pady=5)

        def kaydet():
            sporcu_id = int(box.get().split(" - ")[0])
            self.cursor.execute("""
                INSERT INTO ilerlemeler (sporcu_id, tarih, kilo, tekrar, notlar)
                VALUES (%s, %s, %s, %s, %s)
            """, (sporcu_id, tarih.get_date(), kilo.get(), tekrar.get(), notlar.get()))
            self.db.commit()
            messagebox.showinfo("Başarılı", "İlerleme kaydedildi")
            win.destroy()

        ctk.CTkButton(win, text="Kaydet", command=kaydet).pack(pady=20)

    def show_graph(self):
        win = ctk.CTkToplevel(self.root)
        win.title("Performans Grafiği")
        win.geometry("900x600")
        win.attributes("-topmost", True)
        self.cursor.execute("SELECT id, ad FROM sporcular")
        sporcular = [f"{r[0]} - {r[1]}" for r in self.cursor.fetchall()]
        box = ctk.CTkComboBox(win, values=sporcular); box.pack(pady=5)

        def ciz():
            sporcu_id = int(box.get().split(" - ")[0])
            self.cursor.execute("SELECT tarih, kilo, tekrar FROM ilerlemeler WHERE sporcu_id = %s ORDER BY tarih", (sporcu_id,))
            data = self.cursor.fetchall()
            if not data:
                messagebox.showinfo("Veri Yok", "Bu sporcu için ilerleme verisi bulunamadı.")
                return
            tarih = [d[0].strftime("%Y-%m-%d") for d in data]
            kilo = [d[1] for d in data]
            tekrar = [d[2] for d in data]

            fig = Figure(figsize=(8, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(tarih, kilo, label="Kilo", marker="o")
            ax.plot(tarih, tekrar, label="Tekrar", marker="x")
            ax.set_title("Sporcu Performans Grafiği")
            ax.set_xlabel("Tarih")
            ax.set_ylabel("Değer")
            ax.legend()
            ax.grid(True)

            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas.get_tk_widget().pack()

        ctk.CTkButton(win, text="Grafiği Çiz", command=ciz).pack(pady=20)

    def compare_performance(self):
        win = ctk.CTkToplevel(self.root)
        win.title("Karşılaştırmalı Analiz")
        win.geometry("900x600")
        win.attributes("-topmost", True)
        self.cursor.execute("SELECT id, ad FROM sporcular")
        sporcular = [f"{r[0]} - {r[1]}" for r in self.cursor.fetchall()]
        box1 = ctk.CTkComboBox(win, values=sporcular, width=300); box1.pack(pady=5)
        box2 = ctk.CTkComboBox(win, values=["Kendi Geçmişi"] + sporcular, width=300); box2.pack(pady=5)

        def karsilastir():
            sporcu1_id = int(box1.get().split(" - ")[0])
            if box2.get() == "Kendi Geçmişi":
                self.cursor.execute("SELECT tarih, kilo, tekrar FROM ilerlemeler WHERE sporcu_id = %s ORDER BY tarih", (sporcu1_id,))
                data = self.cursor.fetchall()
                if not data:
                    messagebox.showinfo("Veri Yok", "Bu sporcu için veri bulunamadı.")
                    return
                tarih = [d[0].strftime("%Y-%m-%d") for d in data]
                kilo = [d[1] for d in data]
                tekrar = [d[2] for d in data]

                fig = Figure(figsize=(8, 4), dpi=100)
                ax = fig.add_subplot(111)
                ax.plot(tarih, kilo, label="Kilo", marker="o")
                ax.plot(tarih, tekrar, label="Tekrar", marker="x")
                ax.set_title(f"Sporcu {box1.get()} - Kendi Geçmişi")
                ax.set_xlabel("Tarih")
                ax.set_ylabel("Değer")
                ax.legend()
                ax.grid(True)
            else:
                sporcu2_id = int(box2.get().split(" - ")[0])
                self.cursor.execute("SELECT tarih, kilo, tekrar FROM ilerlemeler WHERE sporcu_id = %s ORDER BY tarih", (sporcu1_id,))
                data1 = self.cursor.fetchall()
                self.cursor.execute("SELECT tarih, kilo, tekrar FROM ilerlemeler WHERE sporcu_id = %s ORDER BY tarih", (sporcu2_id,))
                data2 = self.cursor.fetchall()
                if not (data1 and data2):
                    messagebox.showinfo("Veri Yok", "Seçilen sporculardan biri için veri bulunamadı.")
                    return
                tarih1 = [d[0].strftime("%Y-%m-%d") for d in data1]
                kilo1 = [d[1] for d in data1]
                tarih2 = [d[0].strftime("%Y-%m-%d") for d in data2]
                kilo2 = [d[1] for d in data2]

                fig = Figure(figsize=(8, 4), dpi=100)
                ax = fig.add_subplot(111)
                ax.plot(tarih1, kilo1, label=f"Kilo ({box1.get()})", marker="o")
                ax.plot(tarih2, kilo2, label=f"Kilo (Anonim Sporcu)", marker="x")
                ax.set_title("Sporcu Kilo Karşılaştırması")
                ax.set_xlabel("Tarih")
                ax.set_ylabel("Kilo")
                ax.legend()
                ax.grid(True)

            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas.get_tk_widget().pack()

        ctk.CTkButton(win, text="Karşılaştır", command=karsilastir).pack(pady=20)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    SporcuTakipApp()