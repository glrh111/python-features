#! /usr/bin/python
# -*- coding: utf-8 -*-

# 最简单的迭代器
print 'simplest iteration'
list1 = [x * x for x in range(20) if x % 2 == 0]
it = iter(list1)
try:
    while True:
        val = it.next()
        print val
except StopIteration:
    pass

# 带有索引的表循环
print 'for with index:'
for idx, ele in enumerate(list1):
    print '%d => %d' % (idx, ele)

# 生成器表达器Generator expression与列表解析List Comprehension
# Generate expression : (x*x for x in range(10)) 返回迭代器
# List Comprehension  : [x*x for x in range(100)] 返回list
# 两个小技巧：
# 对元素的动作太复杂 => 抽象成为函数
# 筛选条件太复杂     => 修改成为嵌套的，更清晰
# (x for x in lst if x.dosth()>0) =>
# (x for x in (y.dosth for y in lst) if x>0)

# an efficient tools: itertools
