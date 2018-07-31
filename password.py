password =input("Lütfen parolanızı giriniz:")
if not password:
    print("Lütfen geçerli bir parola giriniz.Parola bölümü boş bırakılamaz!")
elif len(password)<8 or len(password)>32:
    print("Parola uzunluğu 8 karakterden küçük ve 32 karakterden büyük olamaz!")
else:
    sayıvarmi=True
    terstrnakişrtvarmi=False
    tektrnkişrtvarmi=False
    tırnakiştvarmi=False
    boslukvarmi=False
    zorunlukrkyokmu=True
    küçükharfvarmi=True
    büyükharfvarmi=True
    for karakter in password:
        if karakter == ' ':
            boslukvarmi=True
        if karakter ==' " ':
            tırnakiştvarmi=True
        if karakter == "'":
            tektrnkişrtvarmi=True
        if karakter == "`":
            terstrnakişrtvarmi=True
        if karakter != "!" or karakter !="@" or karakter!=  "#"  or karakter != "$" or karakter != "%" or karakter!= "^" or karakter!= "&":
            zorunlukrkyokmu=False
        if karakter.islower()==False:
            print("En az bir küçük harf bulundurunuz.")
            break
        if karakter.isupper()==False:
            print("En az bir büyük harf bulundurunuz.")
            break
        if karakter.isnumeric()==False:
            print("En az bir sayı bulundurunuz.")
            break
    if boslukvarmi:
        print("Parolanızda boşluk olamaz.")
    if tırnakiştvarmi:
        print('Parolanızda " işareti bulunamaz.')
    if tektrnkişrtvarmi:
        print("Parolanızda tek tırnak işareti olamaz.")
    if terstrnakişrtvarmi:
        print("Parolanızda ters tırnak işareti bulunamaz.")
    if zorunlukrkyokmu:
        print("Parolanızda !@#$%^& karakterlerinden birini bulundurunuz.")




