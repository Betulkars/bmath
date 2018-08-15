m1=[[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
m2=[[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
m3=[]
for i in range(len(m1)):
    pivot=[]
    for j in range(len(m2[0])):
        toplam=0
        for k in range(len(m2)):
            toplam+=m1[i][k]*m2[k][j]
        pivot.append(toplam)
    m3.append(pivot)
print(m3)
