lst = list(range(10))

try:
    lst.remove(11)
except:
    print 'no such element'
finally:
    print 'hahhaha'

print lst

for i in range(10):
    lst.insert(0, i+101)

lst.sort()

print lst