from collections import Iterable, Iterator

def fib_g():
	a = 0
	b = 1
	while True:
		yield b
		a, b = b, a + b

print isinstance([], Iterable)

# for idx, value in enumerate(fib_g()):
# 	print '%x = %x' % (idx, value)
# 	if idx > 10000: break

# for idx, value in enumerate((x**2 for x in range(108))):
# 	print '%x = %x' % (idx, value)
# 
# 根据最大公约数和最小公倍数，求符合这个条件的数字
a=5
b=100

# 最小公倍数
def gcd(beta, alpha):
    if alpha == 0:
        return beta
    else:
        return gcd(alpha, beta%alpha)

# 两个数是否互质        
def is_husu(beta, alpha):
    if gcd(beta, alpha) == 1:
        return True
    return False
    
# 求数组中和最小的tueple  
def min_turple(lst):
    idx = 0
    sumer = sum(lst[0])
    for i, value in enumerate(lst):
        if sum(lst[i]) < sumer:
            idx = i
            sumer = sum(lst[i])
    return lst[idx]
    
lst=[]
for i in range(2, b/a+1):
    for j in range(1, i+1):
        if is_husu(i, j) and i*j==b/a:
            lst.append((i, j))

zuixiaode =  min_turple(lst)
print str(zuixiaode[0]*a) + ' ' + str(zuixiaode[1]*a)

# http://www.pythontip.com/coding/code_oj_case/42
import math
def is_prime(n):
    if n <= 3:
        return True
    for i in range(2, int(math.sqrt(n))+2):
        if n%i==0:
            return False
    return True
        
n = 10

def test(n):
    count = 0
    for i in range(1, n/2+1, 2):
        if is_prime(i) and is_prime(n-i) and i != n/2:
            count += 1
            print '%4d - %4d' % (i, n-i)
    return count
    
print test(n)

# 因子平凡和
import math
def yinzi(n):
    if n == 1:
        return [1]
    lst = [1]
    for i in range(2, n+1):
        if n % i == 0:
            lst.append(i)
    return lst
    
def acc(n):
    return sum([reduce((lambda x, y:x+y**2), yinzi(n)) for n in range(1, n+1)])
    
print acc(N)
