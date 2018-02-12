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

	def remove(self,data):
		if self.head is None:
			return
		self.size = self.size -1
		currentNode = self.head
		previousNode = None
		print("to remove {}".format(data))
		while (currentNode is not None) and (currentNode.data != data):
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			#print("***",currentNode.data, previousNode.data)
			if currentNode is None:
				print("cannot delete {}".format(data))
			else:
				previousNode.next = currentNode.nextNode

	def sizeoflist(self):
		return self.size

	def insertEnd(self,data):
		newNode = Node(data)
		self.size += 1
		actualNode = self.head
		if self.head is None:
			self.head = newNode
			return
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode
		#newNode.nextNode = None

	def traverseList(self):
		actualNode = self.head
		while actualNode is not None:
			print("%d " %actualNode.data)
			actualNode = actualNode.nextNode



linkedlist = LinkedList()
linkedlist.insertEnd(12)		
linkedlist.insertEnd(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)
linkedlist.traverseList()
print(linkedlist.sizeoflist())

linkedlist.remove(12)
linkedlist.remove(12)
linkedlist.remove(1)
linkedlist.remove(31)
linkedlist.traverseList()
print(linkedlist.sizeoflist())