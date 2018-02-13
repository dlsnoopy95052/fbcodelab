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

		if self.head is None:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def remove(self,data):
		if self.head is None:
			return
		#self.size = self.size -1
		currentNode = self.head
		previousNode = None
		#print("to remove {}".format(data))
		while (currentNode.data != data):
			previousNode = currentNode
			currentNode = currentNode.nextNode
			if (currentNode is None):
				print("cannot find {} in the list".format(data))
				return
		#print("currentNode data is ", currentNode.data)
		if previousNode is None:
			#print("case 1")
			self.head = currentNode.nextNode
			self.size -= 1
		else:
			#print("***",currentNode.data, previousNode.data)
			if currentNode is None:
				#print("case 2")
				print("cannot delete {}".format(data))
			else:
				#print("case 3")
				#print("***",previousNode.data,currentNode.data)
				previousNode.nextNode = currentNode.nextNode
				#if (previousNode.next is None):
					#print("previous's next is none??")
				#print("currentnode data is ", previousNode.nextNode)
				#print("&&&",(previousNode.next).data)
				self.size -= 1

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
		if (actualNode is None):
			print("empty list")
			return
		while actualNode is not None:
			print("%d " %actualNode.data)
			actualNode = actualNode.nextNode



linkedlist = LinkedList()
linkedlist.insertStart(12)	
linkedlist.insertStart(122)
linkedlist.insertStart(12)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)
print("traversing starts")
linkedlist.traverseList()
print("traversing is done")
print("total size is {}".format(linkedlist.sizeoflist()))

linkedlist.remove(12)
linkedlist.remove(12)
linkedlist.remove(122)
#linkedlist.remove(31)
print("traversing starts")
linkedlist.traverseList()
print("traversing is done")
print("total size is {}".format(linkedlist.sizeoflist()))