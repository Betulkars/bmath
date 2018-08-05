m1=[[1,2],[4,5],[7,8],[1,2],[0,1]]
m2=[[9,8],[6,5],[3,2],[1,2],[0,1]]
m3=[]
for i in range(len(m1)):
    m_satir=[]
    for j in range(len(m2[0])):
        # m1[i][j]+m2[i][j]
        m_satir.append(m1[i][j]+m2[i][j])
    m3.append(m_satir)
print(m3)
