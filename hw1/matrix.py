m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[9,8,7],[6,5,4],[3,2,1]]
m3=[]
for i in range(3):
    k_satir=list()
    for j in range(3):
        m1_sayi=m1[i][j]
        m2_sayi=m2[i][j]
        toplam=m1_sayi+m2_sayi


        k_satir.append(toplam)
    m3.append(k_satir)
print(m3)
