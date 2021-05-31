import os
#? "urunadı" : fiyatı
urunler = {
    "corbalar" : {
        "domates" : 20,
        "balik" : 35,
        "mantar" : 25,
        "tavuk" : 30
    },
    "yemekler" : {
        "balikizgara" : 50,
        "karides" : 55,
        "etsnitzel" : 65,
        "kebap" : 60,
        "spagetti" : 40,
        "pirzola" : 70
    },
    "salatalar" : {
        "sezonsalata" : 15,
        "tonbaligisalata" : 25,
        "akdenizsalata" : 20
    },
    "tatlılar" :{
        "sutlac" : 30,
        "gullac" : 35,
        "kadayif" : 25,
        "baklava" : 40
    },
    "icecekler" :{
        "ayran" : 25,
        "meyvesuyu" : 20,
        "su" : 7,
        "sampanya" : 40,
        "sarap" : 40
    }
}
corbalar = list(urunler["corbalar"].keys())
yemekler = list(urunler["yemekler"].keys())
salatalar = list(urunler["salatalar"].keys())
tatlılar = list(urunler["tatlılar"].keys())
icecekler = list(urunler["icecekler"].keys())
def istek(restaurantGelir):
    print("\nRESTAURANTIMIZA HOŞGELDİNİZ\n")
    while True:
        print("""                    Çorba için 1'i
                    Yemek için 2'yi
                    Salata için 3'ü
                    Tatlı için 4'ü
                    İçecek için 5'i
                    Çıkış için 99'u
                Tuşlayınız...\n""")
        secim = int(input())
        if (secim == 1):
            os.system("cls || clear")
            while True:
                print(f"""                            {corbalar[0]} için 1'i
                            {corbalar[1]} için 2'yi
                            {corbalar[2]} için 3'ü
                            {corbalar[3]} için 4'ü
                        Tuşlayınız...\n""")
                secimCorba = int(input())
                secimCorba2 = int(input("\nKaç porsiyon almak istiyorsunuz? "))
                if (secimCorba == 1):
                    restaurantGelir = restaurantGelir + (urunler["corbalar"]["domates"]*secimCorba2)
                    os.system("cls || clear")
                    break
                elif (secimCorba == 2):
                    restaurantGelir = restaurantGelir + (urunler["corbalar"]["balik"]*secimCorba2)
                    os.system("cls || clear")
                    break
                elif (secimCorba == 3):
                    restaurantGelir = restaurantGelir + (urunler["corbalar"]["mantar"]*secimCorba2)
                    os.system("cls || clear")
                    break
                elif (secimCorba == 4):
                    restaurantGelir = restaurantGelir + (urunler["corbalar"]["tavuk"]*secimCorba2)
                    os.system("cls || clear")
                    break
                else:
                    os.system("cls || clear")
                    print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
            os.system("cls || clear")
        elif (secim == 2):
            os.system("cls || clear")
            while True:
                print(f"""                            {yemekler[0]} için 1'i
                            {yemekler[1]} için 2'yi
                            {yemekler[2]} için 3'ü
                            {yemekler[3]} için 4'ü
                            {yemekler[4]} için 5'i
                            {yemekler[5]} için 6'yı
                        Tuşlayınız...\n""")
                secimYemek = int(input())
                secimYemek2 = int(input("\nKaç porsiyon almak istiyorsunuz? "))
                if (secimYemek == 1):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["balikizgara"]*secimYemek2)
                    os.system("cls || clear")
                    break
                elif (secimYemek == 2):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["karides"]*secimYemek2)
                    os.system("cls || clear")
                    break
                elif (secimYemek == 3):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["etsnitzel"]*secimYemek2)
                    os.system("cls || clear")
                    break
                elif (secimYemek == 4):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["kebap"]*secimYemek2)
                    os.system("cls || clear")
                    break
                elif (secimYemek == 5):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["spagetti"]*secimYemek2)
                    os.system("cls || clear")
                    break
                elif (secimYemek == 6):
                    restaurantGelir = restaurantGelir + (urunler["yemekler"]["pirzola"]*secimYemek2)
                    os.system("cls || clear")
                    break
                else:
                    os.system("cls || clear")
                    print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
            os.system("cls || clear")
        elif (secim == 3):
            os.system("cls || clear")
            while True:
                print(f"""                            {salatalar[0]} için 1'i
                            {salatalar[1]} için 2'yi
                            {salatalar[2]} için 3'ü
                        Tuşlayınız...\n""")
                secimSalata = int(input())
                secimSalata2 = int(input("\nKaç porsiyon almak istiyorsunuz? "))
                if (secimSalata == 1):
                    restaurantGelir = restaurantGelir + (urunler["salatalar"]["sezonsalata"]*secimSalata2)
                    os.system("cls || clear")
                    break
                elif (secimSalata == 2):
                    restaurantGelir = restaurantGelir + (urunler["salatalar"]["tonbaligisalata"]*secimSalata2)
                    os.system("cls || clear")
                    break
                elif (secimSalata == 3):
                    restaurantGelir = restaurantGelir + (urunler["salatalar"]["akdenizsalata"]*secimSalata2)
                    os.system("cls || clear")
                    break
                else:
                    os.system("cls || clear")
                    print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
            os.system("cls || clear")
        elif (secim == 4):
            os.system("cls || clear")
            while True:
                print(f"""                            {tatlılar[0]} için 1'i
                            {tatlılar[1]} için 2'yi
                            {tatlılar[2]} için 3'ü
                            {tatlılar[3]} için 4'ü
                        Tuşlayınız...\n""")
                secimTatli = int(input())
                secimTatli2 = int(input("\nKaç porsiyon almak istiyorsunuz? "))
                if (secimTatli == 1):
                    restaurantGelir = restaurantGelir + (urunler["tatlılar"]["sutlac"]*secimTatli2)
                    os.system("cls || clear")
                    break
                elif (secimTatli == 2):
                    restaurantGelir = restaurantGelir + (urunler["tatlılar"]["gullac"]*secimTatli2)
                    os.system("cls || clear")
                    break
                elif (secimTatli == 3):
                    restaurantGelir = restaurantGelir + (urunler["tatlılar"]["kadayif"]*secimTatli2)
                    os.system("cls || clear")
                    break
                elif (secimTatli == 4):
                    restaurantGelir = restaurantGelir + (urunler["tatlılar"]["baklava"]*secimTatli2)
                    os.system("cls || clear")
                    break
                else:
                    os.system("cls || clear")
                    print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
            os.system("cls || clear")
        elif (secim == 5):
            os.system("cls || clear")
            while True:
                print(f"""                            {icecekler[0]} için 1'i
                            {icecekler[1]} için 2'yi
                            {icecekler[2]} için 3'ü
                            {icecekler[3]} için 4'ü
                            {icecekler[4]} için 5'i
                        Tuşlayınız...\n""")
                secimIcecek = int(input())
                secimIcecek2 = int(input("\nKaç adet almak istiyorsunuz? "))
                if (secimIcecek == 1):
                    restaurantGelir = restaurantGelir + (urunler["icecekler"]["ayran"]*secimIcecek2)
                    os.system("cls || clear")
                    break
                elif (secimIcecek == 2):
                    restaurantGelir = restaurantGelir + (urunler["icecekler"]["meyvesuyu"]*secimIcecek2)
                    os.system("cls || clear")
                    break
                elif (secimIcecek == 3):
                    restaurantGelir = restaurantGelir + (urunler["icecekler"]["su"]*secimIcecek2)
                    os.system("cls || clear")
                    break
                elif (secimIcecek == 4):
                    restaurantGelir = restaurantGelir + (urunler["icecekler"]["sampanya"]*secimIcecek2)
                    os.system("cls || clear")
                    break
                elif (secimIcecek == 5):
                    restaurantGelir = restaurantGelir + (urunler["icecekler"]["sarap"]*secimIcecek2)
                    os.system("cls || clear")
                    break
                else:
                    os.system("cls || clear")
                    print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
            os.system("cls || clear")
        elif (secim == 99):
            print(restaurantGelir)
            break
        else:
            os.system("cls || clear")
            print("\n!!!HATALI TUŞLAMA YAPTINIZ!!!\n")
    return restaurantGelir
