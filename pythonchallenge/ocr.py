# -*- coding: utf-8 -*-
import string
import operator
import itertools

# decode the following string
class MyDict(dict):
    def __missing__(self, key):
        self[key] = rv = 0
        return rv

dic = MyDict()

with open('data', 'r') as f:
    for char in iter(lambda: f.read(1), ''):
        dic[char] += 1

# there has some probs
# sorted_dic = sorted(dic.items(), operator.itemgetter(0))

for idx, ele in dic.items():
    print '%s - %s' % (idx, ele)


# function 2
with open('data', 'r') as f:
    text = f.read()

print ''.join(sorted(set(text), (lambda x, y: text.count(x)-text.count(y))))




