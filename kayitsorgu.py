
def kayitSorgu(im, tcNum):
    im.execute(f"SELECT * FROM musteriler WHERE TCNO = '{tcNum}'")
    veri = im.fetchall()
    if (len(veri) != 0):
        print("\nTc Kimlik Numarası: ", veri[0][0])
        print("\nAd: ", veri[0][1])
        print("\nSoyad: ", veri[0][2])
        print("\nTel Numarası: ", veri[0][3])
        print("\nTarih : ", veri[0][4])
        print("\nKalınacak gün sayısı : ", veri[0][5])
        print("\nOda numarası : ", veri[0][6])
        print(f"\nÜcret : {veri[0][7]} TL(ÖDENMİŞ)")
    else:
        print("\n!!KAYIT BULUNAMADI!!\n")

def personelSorgu(sifre):
    if (sifre == 123456):
        return True
    else:
        return False