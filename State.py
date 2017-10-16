class State:
	
	def __init__(self, x = 0.0, y = 0.0, id = " "):
		self.id = y
		self.pos = [x, y]
	def getPos(self):
		return self.pos
	def getId(self):
		return self.id
	def setPos(self,x, y):
		self.pos = [x, y]
	def setId(self, id)
		self.id = id
	def __hash__(self):
		return hash((self.x, self.y))
	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)
	def __ne__(self, other):
		return not(self == other)