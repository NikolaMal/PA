
	
	
class TreeNode:
	def __init__(self, value, freq):
		self.value = value
		self.freq = freq
		self.parent = None
		self.left = None
		self.right = None
	def getValue(self):
		return self.value
	def getFreq(self):
		return self.freq
	def getParent(self):
		return self.parent
	def getLeft(self):
		return self.left
	def getRight(self):
		return self.right
	def setParent(self, parent):
		self.parent = parent
	def setLeft(self, left):
		self.left = left
	def setRight(self, right):
		self.right = right
		
def GetHistogram(list):
	output = []
	temp_list = []
	for i in list:
		if i not in temp_list:
			temp_list.append(i)
		
	for i in temp_list:
		temp = TreeNode(i, list.count(i))
		output.append(temp)
	return output
	
def GetMinFreqElement(list):
	min = list[0]
	for i in range(1, len(list)):
		if min.getFreq() > list[i].getFreq():
			min = list[i]
	list.remove(min)
	return min
	
def MakeNewElem( left, right):
	new_value = left.getValue() + right.getValue()
	new_freq = left.getFreq() + right.getFreq()
	
	new_elem = TreeNode(new_value, new_freq)
	new_elem.setLeft(left)
	new_elem.setRight(right)
	left.setParent(new_elem)
	right.setParent(new_elem)
	return new_elem

def PutElem(list, elem):
	list.append(elem)

def RemoveElem(list, elem):
	list.remove(elem)
	
def GetEncodedValue(node, root):
	result = ""
	
	while node != root[0]:
		if node.getParent().getLeft() == node:
			result += '0'
		elif node.getParent().getRight() == node:
			result += '1'
	
		node = node.getParent()
	return result[::-1]


	
input = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']

output = GetHistogram(input)
second_output = output[:]


for i in output:
	print(i.getValue(), ' ', i.getFreq())
	

print()

while len(output) > 1:
	a = GetMinFreqElement(output)
	b = GetMinFreqElement(output)
	c = MakeNewElem(a, b)
	PutElem(output, c)
	

#print(output[0].getValue(), ' ', output[0].getFreq())
for i in second_output:
	print(i.getValue(), ' ', GetEncodedValue(i, output))