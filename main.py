from sys import platform
import os
from Solver import *
from BreadthFirst import *

'''solve = BreadthFirst(State(0, 0), State(3, 4))
solve.read("graph.inst")
print(solve.solve().getPath()) '''

def wait():
    input("\nPress enter to continue...")

def clear():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "darwin":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')
	return 

def selectMethod(solver):
	print("1 - Breadth First Search")
	o = int(input("> "))
	if o == 1:
		solver = BreadthFirst()
	return solver

def printStatistics(solution):
		

	return

def main():
	solver = None
	solution = None
	fileName = ""
	
	clear()	
	
	while True:
		print("1 - Load an instance")
		print("2 - Select a method to use")
		print("3 - Come with the litle problem bb")
		print("4 - Statistics")
		print("5 - Exit")
		
		o = int(input('> '))
		
		clear()
		
		if o == 1:
			fileName = input("Instance file: ")
		elif o == 2:
			solver = selectMethod(solver)	
		elif o == 3:
			solver.read(fileName)
			solution = solver.solve()
			print("Little Problem solved...")
		elif o == 4:
			printStatistics(solution)
		elif o == 5:
			break
		
		wait()
		clear()
	
	return
	
main()
	
