# -*- coding: utf-8 -*-

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    first_lst = lst[0]
    try:
        rest_lst = lst[1:]
    except:
        rest_lst = []
    smaller = [x for x in rest_lst if x <= first_lst]
    larger = [y for y in rest_lst if y > first_lst]
    return quick_sort(smaller) + [first_lst] + quick_sort(larger)

print quick_sort(list(range(1, 100))[::-1] + list(range(1, 100)))

print '\n'

print quick_sort(list(range(1, 100)))
