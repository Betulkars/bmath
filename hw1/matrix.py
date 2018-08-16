# m1=[[1, 0, 0],
#      [0, 1, 0],
#      [0, 0, 1]]
# m2=[[5, 8, 1, 2],
#      [6, 7, 3, 0],
#      [4, 5, 9, 1]]
# m3=[]
# for i in range(len(m1)):
#     pivot=[]
#     for j in range(len(m2[0])):
#         toplam=0
#         for k in range(len(m2)):
#             toplam+=m1[i][k]*m2[k][j]
#         pivot.append(toplam)
#     m3.append(pivot)
# print(m3)

line1=0
column1=0
line2=0
column2=0
matrix1=[]
matrix2=[]

line1=int(input("Lütfen 1.matrisin satır sayısını giriniz:"))
column1=int(input("Lütfen 1.matrisin sütun sayısını giriniz:"))

line2=int(input("Lütfen 2.matrisin satır sayısını giriniz:"))
column2=int(input("Lütfen 2.matrisin sütun sayısını giriniz:"))

if column1 != line2:
    print ("1.matrisin sütun sayısı ile 2.matrisin satır sayısı eşit olamaz!")
for i in range (line1):
    matrix1 += [[" "]*column1]
for i in range(line2):
    matrix2 += [[" "]*column2]
for s in matrix1:
    print(s)
print ("  ")
for t in  matrix2:
    print(t)




