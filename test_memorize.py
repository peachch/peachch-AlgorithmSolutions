from functools import wraps


def memorize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


class Test():
    @memorize
    def fibonacci(self,n):
        if n < 2: return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def diao(self,n):
        nn = n-1
        return self.fibonacci(nn)

test = Test()
print(test.diao(11))
sa = test.diao(12)
print(sa)
#print(memorize(test.fibonacci(10)))