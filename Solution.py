from State import *

class Solution:
	def __init__(self, path = [], cost = 0.0, time_elapsed = 0.0):
		self.time_elapsed = time_elapsed
		self.cost = cost
		self.path = path
      
	def insertState(self, s):
		self.path.append(s)

	def getPath(self):
		return self.path
		
	def getTimeElapsed(self):
		return self.time_elapsed
		
		
		
		
		
		
		
		
		
