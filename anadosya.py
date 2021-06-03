import rezervasyon
import kayitsorgu
import rezervbitir
import restaurant
import os
import sqlite3
musteriler = []
gelir = 0
restaurantGelir = 0
anlikGelir= 0 
hesap = 0
i = -1

baglanti = sqlite3.connect("Musteriler.db")
im = baglanti.cursor()

while True:
    print("\nMüşteri rezervasyon işlemleri için 1'e basınız.\n")

    print("Kayıtlı rezervasyon ve hesap bilgisini sorgulamak için 2'ye basınız.\n")

    print("Rezervasyonunuzu sonlandırıp otelden ayrılmak için 3'e basınız.\n")

    print("Restaurant için 4'e basınız.\n")

    print("Otel gelir bilgisi için 5'e basınız.\n") #? Bu if bloğuna sadece şifreyi bilen personeller girebilecektir.

    print("Çıkış yapmak için 99'u tuşlayınız.\n")
    
    sorgu = int(input())

    if (sorgu == 1):
        os.system("cls || clear")
        gelir = gelir + rezervasyon.kayit(gelir, im, baglanti)
    elif (sorgu == 2):
        os.system("cls || clear")
        tcNum = int(input("\nTc Kimlik Numaranızı Giriniz: "))
        kayitsorgu.kayitSorgu(im, tcNum)
    elif (sorgu == 3):
        os.system("cls || clear")
        odaNo = int(input("\nOda Numaranızı Giriniz: "))
        rezervbitir.rezervSil(im, baglanti, odaNo)
    elif (sorgu == 4):
        os.system("cls || clear")
        hesap = restaurant.istek(anlikGelir)
        anlikGelir = 0
        restaurantGelir = restaurantGelir + hesap
        print(f"Hesabınız: {hesap} TL")
        hesap = 0
    elif (sorgu == 5):
        os.system("cls || clear")
        sifre = int(input("\nlütfen personel şifresini giriniz: "))
        if(kayitsorgu.personelSorgu(sifre)):
            f = open("gelir.txt", "w")
            f.write(f"""                        Anlık toplam otel geliri: {gelir}
                        Anlık toplam restaurant geliri: {restaurantGelir}
                        Anlık net otel geliri: {restaurantGelir + gelir}""")
            print("\nGelir bilgisi raporlandı. Görüntülemek için gelir.txt dosyasını açınız. Ekrana yazdırmak için 1'e basınız...\n")
            yazdirma = int(input())
            if (yazdirma == 1):
                f = open("gelir.txt","r")
                print(f.read())
        else:
            print("\n!!!ŞİFRE YANLIŞ!!!\n")
        
    elif (sorgu == 99):
        os.system("cls || clear")
        baglanti.close()
        break
    else:
        os.system("cls || clear")
        print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")

