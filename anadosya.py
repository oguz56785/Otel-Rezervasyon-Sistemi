import rezervasyon

musteriler = []

while True:
    print("\nMüşteri rezervasyon işlemleri için 1'e basınız.\n")

    print("Kayıtlı rezervasyon sorgulamak için 2'ye basınız.\n")

    print("Rezervasyonunuzu sonlandırıp otelden ayrılmak için 3'e basınız.\n")

    print("Restorant ve kafetarya hizmeti için 4^e basınız.\n")

    print("Çıkış yapmak için 99'u tuşlayınız.\n")
    
    sorgu = int(input())

    if (sorgu == 1):
        rezervasyon.kayit(musteriler)