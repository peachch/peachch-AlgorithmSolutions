

input = [3,3,5,6]

def invalidtri(input):
    lenth = len(input)
    input.sort()
    ans = 0
    for i in range(lenth):
        for j in range(i+1,lenth):
            left,right,k = j+1, lenth-1,j
            while left <= right:
                mid = (left+right)//2
                if input[mid] < input[i] + input[j]:
                    k = mid
                    left = mid+1
                else:
                    right = mid-1
            ans += k-j
    print(ans)

invalidtri(input)