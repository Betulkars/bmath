def asalMi(sayi):
    sonuc = True
    for i in range(2, sayi):
        if (sayi % i == 0):
            sonuc = False
    return sonuc


sayi = int(input("Sayi giriniz:"))
if (sayi==1):
    print("En küçük asal sayı 2 dir.Tekrar deneyiniz.")
elif asalMi(sayi):
    print("Asal Sayıdır")
else:
    print("Asal Sayı Değildir")


    def tamBolen(sayi):
        tamBolenler = []
        for i in range(2, sayi + 1):
            if sayi % i == 0:
                tamBolenler.append(i)
        return tamBolenler


    print("Tam Bölenler:", tamBolen(sayi))







