# -*- coding: utf-8 -*-
import dis, itertools

##### F1 : Decorators. Wrap a function. memoize highly recursive functions.
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

##### F2 : for ... else ... syntax
# 没有break的话，else在loop后执行；若有，不执行
def test_for_else():
    for i in range(10):
        if i == 0:
            break

    else: 
        print 'I\'m %s, not 0' % i


##### F3 : dict.get('key', default); dict['key'] may raise an error

##### F4 : Get the python regex parse tree
##### pattern = re.compile(r'[abcde]', re.DEBUG)

##### F5 : Sending values into generator functions
def g():
    a = 5
    while True:
        f = (yield a)
        if f is not None:
            a = f

# >>> g = g()
# >>> g.next()
# 5
# >>> g.next()
# 5
# >>> g.send(7)
# 7
# >>> g.next()
# 7

##### F6 : Disassemble python. import dis
def test_dis(num):
    return (str(num) + str(num))  


##### F7 : import itertools
# 列表元素的 permutations
# print list(itertools.permutations([1,2,3,4]))
# print len(set(list(itertools.permutations('aacd'))))

##### F8 : order a dict by it's value
# import operator
# x = { ... }
# sorted_x = sorted(x.items(), operator.itemgetter(1))  or 0


##### F9 : Merge two dics
# x = {'a':1, 'b':2}
# y = {'b':3, 'c':4}
# z = x.copy()
# z.update(y)


##### F10 : lst.extend(iter) And lst.append(element)
# x = [1, 2, 3]
# x.append([4, 5]) -> x == [1, 2, 3, [4, 5]]
# x.extend('str') -> x == [1, 2, 3, 's', 't', 'r']

##### F11 : test is substr in str
# if substr in strr:

##### F12 : super() in class; __repr__ And __str__; 
class F12_A(object):
    def __init__(self):
        print 'in F12_A'

class F12_B(F12_A):
    def __init__(self):
        super(F12_B, self).__init__()

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__dict__)

    # use obj instance call it. a.foo(x)
    def foo(self, x):
        pass
    # use obj instance || class instance call it. F12_B.class_foo(x)
    @classmethod
    def class_foo(cls, x):
        pass

    # Staticmethods are used to group functions which have some logical connection with a class to the class.
    @staticmethod
    def static_foo(x):
        pass

# x = F12_B()

##### F13 : Decorator chain
# normal decorator
def print_args(f):
    def wrapper(*args, **kwargs):
        print 'Arguments:', args, kwargs
        return f(*args, **kwargs)
    return wrapper

@print_args
def confirm(a, b):
    return  '%s - %s' % (a, b)

# chain decorator
def makebold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped
def makeitalic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@makebold
@makeitalic
def makehtml():
    return 'hello, world!'



##### F14 : Dotted Property : Descriptor
# My own @property
# http://users.rcn.com/python/download/Descriptor.htm
class Property(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, obj, type):
        if obj is None:
            return self
        return self.fget(obj)

class MyClass(object):
    @Property
    def foo(self):
        return 'foo!'


##### F15 : iter() can take a callable argument
# iter(callable, until_value)
def seek_next_line(f):
    for c in iter(lambda: f.read(1), '\n'):
        pass        



##### F16 : dict for missing item
class MyDict(dict):
    def __missing__(self, key):
        self[key] = rv = []
        return rv

# m = MyDict()
# m['foo'].append(1)
# m['foo'].append(2)
# print m
# --> { 'foo' : [1, 2] }



##### F17 : Context managers and 'with' Statement
# with statement calls the special __enter__ and __exit__
# methods on the file object. Exception are also passed to 
# __exit__.
# Guarantee that the file is closed when execution falls out of
# scope of the with suite

# with open('foo.txt', 'a') as f:
#     f.write('Hello, World!')



##### F18 : Named formatting
# print '%(foo)s <-> %(bar)i' % {'foo':1, 'bar':2}
# # locals() is also a dict
# f18_a = 1
# f18_b = 2
# print '%(__name__)s <-> %(f18_a)i <-> %(f18_b)i' % locals()



##### F19 : create new types
NewType = type('NewType', (object, ), {'x':'hello'})

# =====

class NewTypeNew(object):
    x = 'hello'




##### F20 : Conditional Assignment : avid use it
y = 5
x = 3 if (y==1) else 2
x = 3 if (y==1) else 2 if (y==-1) else 0 
# or any other expressions
print (int if (isinstance(x, str)) else str)(x)
# x = (class1 if (y==1) else class2)(a1, a2)



##### F21 : print not \n
# print a,

if __name__ == '__main__':
    print x