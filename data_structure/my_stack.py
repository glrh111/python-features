class My_stack(object):
	def __init__(self):
		super(My_stack, self).__init__()
		self.lst = []

	def __repr__(self):
		return '<%s (%r)>' % (self.__class__, self.__dict__)

	def top(self):
		return len(self.lst)

	def is_empty(self):
		return not bool(self.top())

	def push(self, x):
		self.lst.append(x)

	def pop(self):
		if self.is_empty():
			raise
		else:
			rv = self.lst[self.top()-1]
			del self.lst[self.top()-1]
			return rv
