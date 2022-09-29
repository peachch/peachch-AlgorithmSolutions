
memo = {}
def diff(input):
    global memo
    res = []
    if input in memo:
        return memo[input]
    for i in range(len(input)):
        char = input[i]
        # print(char)

        if char == '-' or char == '+' or char == '*':
            left = list(diff(input[0:i]))
            right = list(diff(input[i+1:]))
            # print(input[0:i])
            # print(right)
            for a in left:
                for b in right:
                    if char == "+":
                        res.append(a+b)
                    elif char == "-":
                        res.append(a-b)
                    elif char == "*":
                        res.append(a*b)
            memo[input] = res
    if not res:
        res.append(int(input))
    return res

print(diff("2*3-4"))