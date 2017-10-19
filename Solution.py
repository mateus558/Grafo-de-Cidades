from State import *

class Solution:
	def __init__(self, a = [], cost = 0.0, time_elapsed = 0.0):
		self.time_elapsed = time_elapsed
		self.cost = cost
		self.a = a
      
	def insertState(self, s):
		self.a.append(s)

	def getPath(self):
		return self.a
