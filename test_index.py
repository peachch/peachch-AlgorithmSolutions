numx = [1,2,3,4,2,1,2,3,2,1,3,4,2,1,2,3,1,2,3,4,2,1,2,3,2,1,3,4,2,1,2,3]
print(len(numx))
for index in range(0,len(numx)+1,5):
    sub = numx[index:index+5]
    print(sub)

