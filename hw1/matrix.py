m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[9,8,7],[6,5,4],[3,2,1]]
m3=[]
for i in range(3):
    m_satir=[]
    for j in range(3):
        # m1[i][j]+m2[i][j]
        m_satir.append(m1[i][j]+m2[i][j])
    m3.append(m_satir)
print(m3)
