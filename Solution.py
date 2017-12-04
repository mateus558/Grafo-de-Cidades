from State import *

class Solution:
	def __init__(self, path = [], cost = 0.0, expandedNodes = 0, branchFactor = 0.0, numberVisited = 0, time_elapsed = 0.0, iterations = 0.0):
		self.time_elapsed = time_elapsed
		self.cost = cost
		self.path = path
		self.expandedNodes = expandedNodes 
		self.branchFactor = branchFactor
		self.numberVisited = numberVisited
		self.iterations = iterations
      	
	def insertState(self, s):
		self.path.append(s)

	def getPath(self):
		return self.path
	
	def getDepth(self):
		return self.path[-1].getDepth()
	
	def getNumberVisited(self):
		return self.numberVisited
	
	def getBranchFactor(self):
		return self.branchFactor
	
	def getExpandedNodes(self):
		return self.expandedNodes
		
	def getTimeElapsed(self):
		return self.time_elapsed
	
	def getCost(self):
		return self.cost
		
	def getNumberOfIterations(self):
		return self.iterations
		
		
		
		
		
		
		
