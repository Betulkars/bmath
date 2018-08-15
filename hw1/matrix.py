m1=[[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
m2=[[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
çarpım=[]
for i in range(len(m1)):
    m_yeni=list()
    for j in range(len(m2[0])):
        for k in range(len(m2[0])):
            m1_sayı=m1[i][k]
            m2_sayi=m2[k][j]
            çarpım += (m1_sayı * m2_sayi)
    m_yeni.append(çarpım)

    m.append(m_yeni)
for s in çarpım:
    print(s)

# m3.append(m3[i][j]+(m1[i][k]*m2[k][j]))