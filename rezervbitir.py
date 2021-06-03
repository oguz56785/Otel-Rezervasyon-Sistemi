import os
def rezervSil(im, baglanti, odaNum):
    im.execute(f"SELECT * FROM musteriler WHERE ODANO = '{odaNum}'")
    data = im.fetchall()
    if (len(data) != 0):
        im.execute(f"DELETE FROM musteriler WHERE ODANO = '{odaNum}'")
        baglanti.commit()
        print("\nMÜŞTERİ KAYDI BAŞARIYLA SİLİNDİ!!\n")
    else:
        os.system("cls || clear")
        print("\n!!KAYIT BULUNAMADI!!")

