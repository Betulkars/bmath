def asalMi(sayi):
    tamBolenler = []
    for i in range(2, int(sayi // 2) + 1):
        if (sayi % i == 0):
            tamBolenler.append(i)
            return tamBolenler

try:
    sayi = int(input("Sayi giriniz:"))
    tamBolenler = asalMi(sayi)
    if (sayi == 1):
        print("En küçük asal sayı 2 dir.Tekrar deneyiniz.")
    elif len(tamBolenler) == 0:
         print("Asal Sayıdır")
    else:
        print("Asal Sayı Değildir, Tam Bölenler:", tamBolenler)
except ValueError:
    print("Lütfen pozitif tamsayı giriniz.")

