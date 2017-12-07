class State:
	
	def __init__(self, x = 0.0, y = 0.0, id = " ", priority = 0.0):
		self.id = id
		self.pos = [x, y]
		self.visited = False
		self.father = None
		self.costSoFar = 0.0
		self.depth = 0
		self.operator = []
		self.priority = priority
			
	def getPos(self):
		return self.pos
	
	def getId(self):
		return self.id
	
	def setPos(self,x, y):
		self.pos = [x, y]
	
	def setId(self, id):
		self.id = id
	
	def setPriority(self, priority):
		self.priority = priority
	
	def getPriority(self):
		return self.priority
	
	def setVisited(self, visited):
		self.visited = visited
	
	def setFather(self, state):
		self.father = state
	
	def setDepth(self, depth):
		self.depth = depth
	
	def getDepth(self):
		return self.depth
	
	def getFather(self):
		return self.father
	
	def increaseCostSoFar(self, cost):
		self.costSoFar = self.costSoFar + cost
	
	def getCostSoFar(self):
		return self.costSoFar
	
	def setCostSoFar(self, val):
		self.costSoFar = val
	
	def getCost(self):
		return self.costSoFar	 
	
	def isVisited(self):
		return self.visited

	def getOperator(self):
		if(len(self.operator)-1 >=0):
			return self.operator[len(self.operator)-1] #return the top
		else:
			return 0
	
	def setOperator(self, operator):
		if(operator not in self.operator):
			self.operator.append(operator)
		else:
			operator2 = operator
			while (operator2 not in self.operator):
				operator2 = operator2 + 1
			self.operator.append(operator2)
			
	def __cmp__(self, other):
		return (self.priority, other.priority)
	
	def __repr__(self):
		return str(self.pos) + str(" ") + str(self.id)
	
	def __str__(self):
		return str(self.pos) + str(self.id)
	
	def __hash__(self):
		return hash((self.pos[0], self.pos[1]))
	
	def __eq__(self, other):
		return (self.pos[0], self.pos[1]) == (other.pos[0], other.pos[1])
	
	def __lt__(self, other):
		return (self.priority < other.priority);
	
	def __ne__(self, other):
		return not(self == other)

