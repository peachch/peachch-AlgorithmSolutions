def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = 0
    # lat = 0\
    lengt = len(matrix)
    length = len(matrix) - 1
    print(int(lengt/2))
    print((lengt+1)//2)
    for row in range((lengt)//2):
        for lat in range((lengt+1)//2):
            temp = matrix[row][lat]
            matrix[row][lat] = matrix[length - lat][row]
            matrix[length - lat][row] = matrix[length - row][length - lat]
            matrix[length - row][length - lat] = matrix[lat][length - row]
            matrix[lat][length - row] = temp

    return matrix

print(rotate([[5,1,9],[2,4,8],[13,3,6]]))