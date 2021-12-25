import menu_yonetimi
from .musteri import Musteri
from . import musteri_yonetimi
import random
import os
import time

__menu_metni =("""
            ===========================
            Müşteri Yönetim Menüsü
            ===========================
            Lütfen bir seçenek seçiniz:
            (1) Müşteri Ekle
            (2) Müşteri Listele
            (3) Müşteri Sil
            (4) Müşteri Düzenle
            (5) Ana Menüye Dön
            ===========================
            """)

def __musteri_ekle(musteri:Musteri):
    if musteri == None:
        musteri_benzersiz_kod   = random.randint(1, 1000000)
        musteri_tckn            = input("Lütfen 11 Haneli Müşteri TCKN Giriniz : ")
        musteri_adi             = input("Müşteri Adını Giriniz : ")
        musteri_soyadi          = input("Müşteri Soyadını Giriniz : ")
        musteri_adresi          = input("Müşteri Adresini Giriniz : ")
        musteri_telefonu        = input("Müşteri Telefonunu Başında '0' Olmadan Giriniz : ")
        musteri = Musteri(musteri_benzersiz_kod, musteri_tckn, musteri_adi, musteri_soyadi, musteri_adresi, musteri_telefonu)

        sonuc = musteri_yonetimi.musteri_ekle(musteri)

        if sonuc[0] == False:
            print(sonuc[1])
            __musteri_ekle(musteri)
        else:
            print("Müşteri Başarıyla Kaydedildi.") 
    
    else:
        print("Daha Önce Girdiğiniz Değeri Kabul Etmek için Enter Tuşuna Basınız.")
        musteri_tckn        = input(f"Lütfen 11 Haneli Müşteri TCKN Giriniz ({musteri.tckn}) : ")
        musteri_adi         = input(f"Müşteri Adını Giriniz ({musteri.adi}): ")
        musteri_soyadi      = input(f"Müşteri Soyadını Giriniz ({musteri.soyadi}) : ")
        musteri_adresi      = input(f"Müşteri Adresini Giriniz ({musteri.adres}) : ")
        musteri_telefonu    = input(f"Müşteri Telefonunu Başında '0' Olmadan Giriniz ({musteri.tel}) : ")

        if musteri_tckn == "":
            musteri_tckn = musteri.tckn
        
        if musteri_adi == "":
            musteri_adi = musteri.adi

        if musteri_soyadi == "":
            musteri_soyadi = musteri.soyadi
        
        if musteri_adresi == "":
            musteri_adresi = musteri.adres
        
        if musteri_telefonu == "":
            musteri_telefonu = musteri.tel

        musteri = Musteri(musteri.benzersiz_kod, musteri_tckn, musteri_adi, musteri_soyadi, musteri_adresi, musteri_telefonu)

        sonuc = musteri_yonetimi.musteri_ekle(musteri)

        if sonuc[0] == False:
            print(sonuc[1])
            __musteri_ekle(musteri)
        else:
            print("Müşteri Başarıyla Kaydedildi.") 

def menu_getir(): 
    while True:
        print(__menu_metni)
        secenek = int(input("Müşteri Yönetimi Menü Seçiminizi Yapınız: "))
        if secenek == 1:
            print("Müşteri Ekleme Çalışıyor")
            time.sleep(1)
            __musteri_ekle(None)
        elif secenek == 2:
            os.system("cls")
            print("Müşteriler listeleniyor...")
            time.sleep(1)
            musteri_listesi = musteri_yonetimi.musteri_listele()
            for musteri in musteri_listesi.items():
                print(musteri)
            print(input("Devam Etmek için Bir Tuşa Basınız..."))                
        elif secenek == 3:
            os.system("cls")
            print("Müşteri Silme Çalışıyor...")   
            time.sleep(1)               
            musteri_listesi = musteri_yonetimi.musteri_listele()
            for musteri in musteri_listesi.items():
                print(musteri)
            musteri_yonetimi.musteri_sil(int(input("Lütfen Silmek İstediğiniz Müşterinin Benzersiz Kodunu Giriniz : ")))
        elif secenek == 4:
            os.system("cls")
            print("Müşteri Düzenleme Çalışıyor...")   
            time.sleep(1)                     
            musteri_listesi = musteri_yonetimi.musteri_listele()
            for musteri in musteri_listesi.items(): 
                print(musteri)
            musteri_yonetimi.arac_duzenle(int(input("Lütfen Düzenlemek İstediğiniz Müşterinin Benzersiz Kodunu Giriniz : ")))
        elif secenek == 5:
            menu_yonetimi.ana_menu_getir()
        else:
            print("Lütfen Doğru Seçeneği Seçiniz!")              
            