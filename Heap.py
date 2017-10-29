from Item import Item

class Heap:

	def __init__(self, heapType):
		self.array = []
		self.count = 0
		self.heapType = heapType

	"""
	inserts an item in heap
	"""
	def insert(self, item):
		self.count = self.count + 1
		self.array.insert(0, item)
		self.percolateDown(0)

	"""
	computes position of left child of ith element
	"""
	def leftChildPosition(self, i):
		left = 2 * i + 1
		if (left >= self.count):
			return -1
		return left

	"""
	computes position of right child of ith element
	"""
	def rightChildPosition(self, i):
		right = 2 * i + 2
		if (right >= self.count):
			return -1
		return right

	"""
	restructures/heapifies heap starting at position i
	"""
	def percolateDown(self, i):
		l = self.leftChildPosition(i)
		r = self.rightChildPosition(i)
		
		if (l != -1 and self.array[l].priority < self.array[i].priority):
			minimum = l
		else:
			minimum = i

		if (r != -1 and self.array[r].priority < self.array[minimum].priority):
			minimum = r
		
		""" swap i and minimum positions """
		if (minimum != i):
			temp = self.array[i]
			self.array[i] = self.array[minimum]
			self.array[minimum] = temp
			self.percolateDown(minimum)
	
	"""
	deletes and returns the minimum priority element from heap
	"""
	def deleteMin(self):
		if (self.count == 0):
			return -1

		item = self.array[0]
		self.array[0] = self.array[self.count - 1]
		self.count = self.count -1
		""" Heapify """
		self.percolateDown(0)
		return item

	"""
	Updates priority of item with data item to priority
	"""
	def updatePriority(self, item, priority):
		for idx, heapItem in self.array:
			if (heapItem.item == item):
				heapItem.priority = priority
				self.array[idx] = heapItem
				break

	"""
	returns true when heap is empty else false
	"""
	def isEmpty(self):
		return self.count == 0
