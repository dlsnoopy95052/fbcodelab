class Node(object):
	def __init__(self,data):
		self.data = data
		self.nextNode = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def insertStart(self,data):
		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode


	def size(self):
		return self.size

