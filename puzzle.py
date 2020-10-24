import re
import copy
def LoadFromFile(testfile):
	contents = open(testfile)
	Fl = contents.readlines()
	mainList = []
	for x in Fl:
		subList = []
		temp = re.findall(r'\d+', x) 
		res = list(map(int, temp))
		mainList.append(res)
	return mainList
def flatten(nested_list):
	flat_list = []

	def flatten_func(sublist):
		for element in sublist:
			if isinstance(element, list):
				flatten_func(element)
			else:
				flat_list.append(element)


	flatten_func(nested_list)
	return flat_list
def deBugPrint(state):
	for x in state:
		for y in x:
			print (y, end = " ")
		print("")
	print ("___")
def moveUp (state):
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if a > 0:
		(newState[a])[b] = (state[a-1])[b]
		(newState[a-1])[b] = 0
		return [state[a-1][b], newState]
	else:
		return None
def moveDown (state):
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if a < len(state) - 1:
		(newState[a])[b] = (state[a+1])[b]
		(newState[a+1])[b] = 0
		return [state[a+1][b], newState]
	else:
		return None
def moveLeft (state):
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if b > 0:
		(newState[a])[b] = (state[a])[b - 1]
		(newState[a])[b - 1] = 0
		return [state[a][b-1], newState]
	else:
		return None
def moveRight (state):
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if b < len(state[0]) - 1:
		(newState[a])[b] = (state[a])[b + 1]
		(newState[a])[b + 1] = 0
		return [state[a][b+1], newState]
	else:
		return None
def computeNeighbors (state):
	neighbors = []
	if not moveUp(state) == None:
		neighbors.append(moveUp(state))
	if not moveDown(state) == None:
		neighbors.append(moveDown(state))
	if not moveRight(state) == None:
		neighbors.append(moveRight(state))
	if not moveLeft(state) == None:
		neighbors.append(moveLeft(state))
	return neighbors
def goal(state):
	checkState = copy.deepcopy(state)
	x = flatten(checkState)
	y = flatten(state)
	x.sort()
	print (x)
	print (y)
	if x == y:
		return True
	else:
		return False
def BFS(state):
	frontier = state
	discovered = {state[0][0]}
	
	
def main():
	printer = LoadFromFile("testfile.txt")
	deBugPrint(printer)
	print (computeNeighbors(printer))
	print (BFS(printer))
	print (goal (printer))
main()
