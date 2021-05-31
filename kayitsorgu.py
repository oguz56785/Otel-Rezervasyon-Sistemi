
def kayitSorgu(musteriler, tcNum, i):
    while True:
        i = i + 1
        if (len(musteriler) != 0):
            if (musteriler[i].tcNo == tcNum):
                print("\nTc Kimlik Numarası: ", musteriler[i].tcNo)
                print("\nAd: ", musteriler[i].ad)
                print("\nSoyad: ", musteriler[i].soyAd)
                print("\nTel Numarası: ", musteriler[i].telNo)
                print("\nTarih : ", musteriler[i].tarih)
                print("\nKalınacak gün sayısı : ", musteriler[i].kalinacakGun)
                print("\nOda numarası : ", musteriler[i].odaNo)
                print(f"\nÜcret : {musteriler[i].ucret}(ÖDENMİŞ)")
                break
            else:
                return True
        else:
            break

def kayitSorgu2(musteriler, tcNum, j):
    while True:
        j = j + 1
        if (len(musteriler) != 0):
            if (musteriler[j].tcNo == tcNum):
                return True
            else:
                return False
        else:
            print("\n!!OTELDE KAYIT BULUNMUYOR!!\n")
            break  


# def odaNoSorgu(musteriler, odaNo, hesap, restaurantGelir):
#     for i in range(len(musteriler)):
#         if (musteriler[i].odaNo == odaNo):
#             restaurantGelir = restaurantGelir + hesap
#             musteriler[i].ucret = musteriler[i].ucret + hesap

def personelSorgu(sifre):
    if (sifre == 123456):
        return True
    else:
        return False
        




