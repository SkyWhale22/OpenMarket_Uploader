from Items.Base import ItemBase

class ItemList:

	####################################################################################################
	#                                        Member Variables                                          #
	####################################################################################################

	####################################################################################################
	#                                        Member Functions                                          #
	####################################################################################################
	m_head = None
	m_tail = None

	def __init__(self):
		self.m_head = None
		self.m_tail = None

	def AddNode(self, node):
		if(self.m_head == None):
			self.m_head = node
			self.m_tail = node

		ItemBase(self.m_tail).m_next = node
		ItemBase(node).m_prev = self.m_tail

		self.m_tail = node

	def GetHeadNode(self):
		return self.m_head

	def GetTailNode(self):
		return self.m_tail

	def FindNodeAt(self, index, node):
		count = 0

		if(ItemBase(self.m_head) == None):
			return

		if(index == count):
			return node

		return self.FindNodeAt(index-1, ItemBase(self.m_tail).m_next)

	# def PopAt(self, index):
	# 	node = self.FindNodeAt(index, self.m_head)
	#
	#
	# 	if(node.m_next != None):
	# 		node.m_next.m_prev = node.m_prev
	#
	# 		if(node.m_prev !=)
	# 		node.m_prev = node.m_next
	# 	else:
	#
	# 	if(node.m_prev != None):
	# 		node.m_prev = None
	#
	# 	node.m_prev.m_next = None
	#
	# 	return node

	def Pop(self):
		tail = self.GetTailNode()

		tail.m_prev = None
		tail.m_prev.m_next = None

		return tail
