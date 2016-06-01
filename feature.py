# -*- coding: utf-8 -*-
class memoize:
    def __init__(self, f):
        self.f = f
        self.dict = {}

    def __call__(self, *args):
        if not args in self.dict:
            self.dict[args] = self.f(*args)
        return self.dict[args]

@memoize
def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fib2(n):
    if n < 2:
        return 1
    return fib2(n-1) + fib2(n-2)

if __name__ == '__main__':
    for i in range(10000):
        print fib2(i)