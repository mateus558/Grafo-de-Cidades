class State:
	
	def __init__(self, x = 0.0, y = 0.0, id = " "):
		self.id = id
		self.pos = [x, y]
	
	def getPos(self):
		return self.pos
	
	def getId(self):
		return self.id
	
	def setPos(self,x, y):
		self.pos = [x, y]
	
	def setId(self, id):
		self.id = id
	
	def __repr__(self):
		return str(self.pos) + str(" ") + str(self.id)
	
	def __str__(self):
		return str(self.pos) + str(self.id)
	
	def __hash__(self):
		return hash((self.pos[0], self.pos[1]))
	
	def __eq__(self, other):
		return (self.pos[0], self.pos[1]) == (other.pos[0], other.pos[1])
	
	def __ne__(self, other):
		return not(self == other)

