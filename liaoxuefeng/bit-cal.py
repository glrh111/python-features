# -*- coding: utf-8 -*-

def tran(hexno):
	def iter(product, no, count):
		if count < 0:
			return product
		return iter(product+[int(no/0x10**count)], no % 0x10**count, count-2)
	return '.'.join(map(str, (iter([], hexno, 6))))

test1 = 0x8002c2f2

print tran(test1)
	