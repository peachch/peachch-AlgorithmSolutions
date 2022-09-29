import copy
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

marked1 = [copy.deepcopy([False]*len(board[0]))]*len(board)
a =[1,2]
b = [2,3]
c = (a,b)
print(id(marked1))
marked2 = copy.copy(marked1)
print(id(marked2))
marked3 = ceshi
print(id(marked3))
marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

# for i in marked2:
#     print(id(i))
for i in marked3:
    print(id(i))
#
# for i in marked:
#     print(id(i))


print(marked)
print(marked1)
print(type(marked), type(marked1))
marked2[0][0] = True
marked3[0][0] = True
print(marked2)
print(marked3)


a = {1:"1",2:"2",3:"3"}
b = [a, a]
print(b)
b = copy.copy(b)
a[1]="yi"
print(b)

# 深拷贝、浅拷贝；列表生成式


