import os
odalar = {
    "Tek" : {
        "adet" : 50,
        "gunlukFiyat" : 200,
        "no" : 1000
    },
    "Çift" : {
        "adet" : 30,
        "gunlukFiyat" : 400,
        "no" : 2000
    },
    "Uc" : {
        "adet" : 25,
        "gunlukFiyat" : 600,
        "no" : 3000
    },
    "Dort" : {
        "adet" : 20,
        "gunlukFiyat" : 800,
        "no" : 4000
    }
}

class Musteri():
    tcNo = 0
    ad = ""
    soyAd = ""
    telNo = 0
    tarih = ""
    kalinacakGun = 0
    odaNo = 0
    ucret = 0
    def __init__(self, odaNo):
        self.tcNo = int(input("\nTc Kimlik Numarası: "))
        self.ad = input("\nAd: ")
        self.soyAd = input("\nSoyad: ")
        self.telNo = input("\nTelefon Numarası: ")
        self.tarih = input("\nTarih: ")
        self.kalinacakGun = int(input("\nKalınacak gün sayısı: "))
        self.odaNo = odaNo

def kayit(musteriler, gelir):
    while True:
        print("REZERVASYON SİSTEMİNE HOŞGELDİNİZ!\n\n")
        print(f"""Toplam tek kişilik oda: {odalar["Tek"]["adet"]}
                Toplam çift kişilik oda: {odalar["Çift"]["adet"]}
                Toplam üç kişilik oda: {odalar["Uc"]["adet"]}
                Toplam dört kişilik oda: {odalar["Dort"]["adet"]}\n\n""")

        kisiSayisi = int(input("Kaç kişilik rezervasyon yaptıracaksınız?")) #Kişi sayısı ile oda seçimi bağlantılıdır.
        os.system("cls || clear")
        if (kisiSayisi == 1):
            odalar["Tek"]["no"] = odalar["Tek"]["no"] + 1
            odalar["Tek"]["adet"] = odalar["Tek"]["adet"] - 1
            musteri = Musteri(odalar["Tek"]["no"])
            musteri.ucret = odalar["Tek"]["gunlukFiyat"] * musteri.kalinacakGun
            musteriler.append(musteri)
            gelir = gelir + musteri.ucret
            print(f"\nOda Numaranız: {musteri.odaNo}")
            break
        elif (kisiSayisi == 2):
            odalar["Çift"]["no"] = odalar["Çift"]["no"] + 1
            odalar["Çift"]["adet"] = odalar["Çift"]["adet"] - 1
            for musteri in range(2):
                musteri = Musteri(odalar["Çift"]["no"])
                musteri.ucret = odalar["Çift"]["gunlukFiyat"] * musteri.kalinacakGun #? 2 kişilik odada her bir müşteri için de odanın ücreti kayıtta görünecek ama hesap olarak sadece birinin ücret bilgisi hesaba yansıyacak.
                musteriler.append(musteri)
            gelir = gelir + musteri.ucret
            print(f"\nOda Numaranız: {musteri.odaNo}")
            break
        elif (kisiSayisi == 3):
            odalar["Uc"]["no"] = odalar["Uc"]["no"] + 1
            odalar["Uc"]["adet"] = odalar["Uc"]["adet"] - 1
            for musteri in range(3):
                musteri = Musteri(odalar["Uc"]["no"])
                musteri.ucret = odalar["Uc"]["gunlukFiyat"] * musteri.kalinacakGun
                musteriler.append(musteri)
            gelir = gelir + musteri.ucret
            print(f"\nOda Numaranız: {musteri.odaNo}")
            break
        elif (kisiSayisi == 4):
            odalar["Dort"]["no"] = odalar["Dort"]["no"] + 1
            odalar["Dort"]["adet"] = odalar["Dort"]["adet"] - 1
            for musteri in range(4):
                musteri = Musteri(odalar["Dort"]["no"])
                musteri.ucret = odalar["Dort"]["gunlukFiyat"] * musteri.kalinacakGun
                musteriler.append(musteri)
            gelir = gelir + musteri.ucret
            print(f"\nOda Numaranız: {musteri.odaNo}")
            break
        else:
            os.system("cls || clear")
            print("\nHatalı tuşlama yaptınız!!\n")
    return gelir