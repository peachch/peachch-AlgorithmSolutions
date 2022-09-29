arr = [1,2,3,4,5]
n = len(arr)
index = 0
while True:
    print(arr[index % n])
    index+=1