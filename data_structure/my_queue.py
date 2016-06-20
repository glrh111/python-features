class My_queue(object):
	def __init__(self):
		super(My_queue, self).__init__()
		self.lst = []

	def __repr__(self):
		return '<%s (%r)>' % (self.__class__, self.__dict__)

	def head(self):
		'''
		return head.idx + 1
		'''
		return len(self.lst)

	def tail(self):
		'''
		return tail.idx
		'''
		return 0

	def is_empty(self):
		return not bool(self.head())

	def enqueue(self, x):
		'''
		enter queue
		'''
		self.lst.insert(self.tail(), x)

	def dequeue(self):
		'''
		de queue
		'''
		if self.is_empty():
			raise
		rv = self.lst[self.head()-1]
		del self.lst[self.head()-1]
		return rv