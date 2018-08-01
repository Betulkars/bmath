password =input("Lütfen parolanızı giriniz:")
if not password:
    print("Lütfen geçerli bir parola giriniz.Parola bölümü boş bırakılamaz!")
elif len(password)<8 or len(password)>32:
    print("Parola uzunluğu 8 karakterden küçük ve 32 karakterden büyük olamaz!")
else:
    terstrnakişrtvarmi=False
    tektrnkişrtvarmi=False
    tırnakiştvarmi=False
    boslukvarmi=False
    zorunlukrkyokmu=True
    büyükharfyokmu=True
    küçükharfyokmu=True
    sayiyokmu=True
    # k = 0
    # b = 0
    # c = 0
    for karakter in password:
        if karakter == ' ':
            boslukvarmi=True
        if karakter =='"':
            tırnakiştvarmi=True
        if karakter == "'":
            tektrnkişrtvarmi=True
        if karakter == "`":
            terstrnakişrtvarmi=True
        if karakter == "!" or karakter =="@" or karakter==  "#"  or karakter == "$" or karakter == "%" or karakter== "^" or karakter== "&":
            zorunlukrkyokmu=False
        if karakter.islower():
            büyükharfyokmu=False
            # k+=1
        if karakter.isupper():
            küçükharfyokmu=False

            # b+=1
        if karakter.isnumeric():
            sayiyokmu=False
            # c+=1


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
    if büyükharfyokmu:
        print("En az bir küçük harfkullanın.")
    if küçükharfyokmu:
        print("En az bir büyük harf kullanın")
    if sayiyokmu:
        print("En az bir sayı kullanın")

