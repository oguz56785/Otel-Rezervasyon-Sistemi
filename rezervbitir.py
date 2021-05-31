import os
def rezervSil(musteriler, odaNum):
    for i in range(len(musteriler)):
        if (musteriler[i].odaNo == odaNum):
            musteriler.pop(i)
        else:
            os.system("cls || clear")
            print("\n!!KAYIT BULUNAMADI!!")

