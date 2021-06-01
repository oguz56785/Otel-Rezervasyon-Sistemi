import rezervasyon
import kayitsorgu
import rezervbitir
import restaurant
import os
musteriler = []
gelir = 0
restaurantGelir = 0
anlikGelir= 0 
hesap = 0
i = -1
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
        gelir = gelir + rezervasyon.kayit(musteriler, gelir)
    elif (sorgu == 2):
        os.system("cls || clear")
        tcNum = int(input("\nTc Kimlik Numaranızı Giriniz: "))
        kayitsorgu.kayitSorgu(musteriler, tcNum, i)
        if (kayitsorgu.kayitSorgu2(musteriler, tcNum, i) != True):
            print("\n!!!KAYIT BULUNAMADI!!!\n")
    elif (sorgu == 3):
        os.system("cls || clear")
        odaNo = int(input("\nOda Numaranızı Giriniz: "))
        rezervbitir.rezervSil(musteriler, odaNo)
        os.system("cls || clear")
    elif (sorgu == 4):
        os.system("cls || clear")
        hesap = restaurant.istek(anlikGelir)
        anlikGelir = 0
        restaurantGelir = restaurantGelir + hesap
        print(f"Hesabınız: {hesap}")
        hesap = 0
    elif (sorgu == 5):
        os.system("cls || clear")
        sifre = int(input("\nlütfen personel şifresini giriniz: "))
        if(kayitsorgu.personelSorgu(sifre)):
            print(f"Anlık toplam otel geliri: {gelir}")
            print(f"Anlık toplam restaurant geliri: {restaurantGelir}")
            print(f"Anlık net otel geliri: {restaurantGelir + gelir}")
        else:
            print("\n!!!ŞİFRE YANLIŞ!!!\n")
        
    elif (sorgu == 99):
        os.system("cls || clear")
        break
    else:
        os.system("cls || clear")
        print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")