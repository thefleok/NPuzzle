# Leo Jergovic
# Matthew Redmond
# AP Computer Science, C Block
# puzzle.py solves NPuzzle (NOTE: character "*" rep. by 0 in representation")

import re
import copy
import sys

# File Loading
# Arguments: file
# Returns: List of Lists (embedded list)

def LoadFromFile(testfile):
	# following portion of code reads file
	contents = open(testfile)
	Fl = contents.readlines()
	mainList = []
	sideLength = 0
	counter = 0 # index incrementation
	# following for loop determines integers/* to be appended
	for x in Fl:
		if counter == 0: # first line is always sideLength
			sideLength = int(x)
		else:
			y = list(x) # convert to list to change * to 0
			for chr in y:
				if chr == "*":
					y[y.index("*")] = "0"
			z = "".join(y)
			temp = re.findall(r'\d+', z) 
			res = list(map(int, temp))
			mainList.append(res)
		counter = counter + 1 # increments for index
	return testLoadedFile(mainList, sideLength)

# Arguments: mainList (of lists), sideLength of the Npuzzle square
# Returns: List of lists if meets requirements of file

def testLoadedFile(mainList, sideLength): # method checks input file for errors
	for a in mainList: # are all lines same length?
		if len(a) != len(mainList[0]):
			print("not valid file")
			sys.exit()
	count = 0
	ordering = sorted(flatten(mainList)) # orders list to check while loop
	while count < len(ordering) - 1: # sorted numbs chronological/unique?
		if ordering[count + 1] - 1 != ordering[count]:
			print("not valid file")
			sys.exit()
		count = count + 1
	if sideLength != len(mainList): # side length vertically correct?
		print("not valid file")
		sys.exit()
	if sideLength != len(mainList[0]): # side length horizontally correct?
		print("not valid file")
		sys.exit()
	return mainList

# general functions (used throughout program)
# Arguments: list of lists
# returns: single list (code from class early October)

def flatten(nestedList): # flatten function (used throughout program)
	flatList = []
	def flattenFunc(sublist): # method appends list elements to flatlist
		for element in sublist:
			if isinstance(element, list):
				flattenFunc(element)
			else:
				flatList.append(element)
	flattenFunc(nestedList) # call on main list
	return flatList

# Arguments: list of lists (state)
# Returns: nothing, prints state in original format

def deBugPrint(state):
	for x in state: # iterates through all loops
		for y in x:
			print(y, end = "\t")
		print("")
	print ("___")

# Neighbor determination
# Arguments: state (list of lists)
# Returns: tile moved up into hole int, and new state

def moveUp(state): # checks if neighbor is possible above
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state) # makes copy of state to change/check
	if a > 0: # if below first row, is possibble
		(newState[a])[b] = (state[a - 1])[b]
		(newState[a - 1])[b] = 0
		return [state[a - 1][b], newState]
	else:
		return None

# Arguments: state (list of lists)
# Returns: tile moved down into hole int, and new state

def moveDown (state): # checks if neighbor down is possible 
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if a < len(state) - 1: # if above last row, is possible
		(newState[a])[b] = (state[a+1])[b]
		(newState[a + 1])[b] = 0
		return [state[a + 1][b], newState]
	else:
		return None

# Arguments: state (list of lists)
# Returns: tile moved left into hole int, and new state

def moveLeft (state): # checks if neighbor leftward is possible
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if b > 0: # can move left if not leftmost
		(newState[a])[b] = (state[a])[b - 1]
		(newState[a])[b - 1] = 0
		return [state[a][b-1], newState]
	else:
		return None

# Arguments: state (list of lists)
# Returns: tile moved up into hole int, and new state

def moveRight (state): # checks if right neighbor is possible
	for x in state:
		if 0 in x:
			a = state.index(x)
			b = x.index(0)
	newState = copy.deepcopy(state)
	if b < len(state[0]) - 1: # can move right if not at rightmost
		(newState[a])[b] = (state[a])[b + 1]
		(newState[a])[b + 1] = 0
		return [state[a][b + 1], newState]
	else:
		return None

# Arguments: state (list of lists)
# Returns: list of up to 4 possible neighbor states (up, left, down, right)

def computeNeighbors (state):
	neighbors = []
	if not moveUp(state) == None: # checks if a possible neighbor state
		neighbors.append(moveUp(state))
	if not moveLeft(state) == None:
		neighbors.append(moveLeft(state))
	if not moveDown(state) == None:
		neighbors.append(moveDown(state))
	if not moveRight(state) == None:
		neighbors.append(moveRight(state))
	return neighbors # returns neighbors

# Algorithms
# Arguments: state (list of lists)
# returns: Boolean, true if ordered and * in bottom right

def isGoal(state):
	checkState = copy.deepcopy(state)
	x = flatten(checkState) # flattens for an easier order check
	y = flatten(state)
	x.sort()
	x.pop(0)
	x.append(0) # move 0 to end because of ordering
	if x == y: # compares the altered and unaltered states
		return True
	else:
		return False	

# Arguments: state (list of lists)
# Returns: list of strings for steps to result

def BFS(state):
	frontier = [state]
	discovered = [state]
	parents = {tuple(flatten(state)): []} # dictionary —> list to tuple
	while len(frontier) > 0:
		currentState = frontier.pop(0)
		if isGoal(currentState): # checks if its a goal
			return parents[tuple(flatten(currentState))]
		for neighbor in computeNeighbors(currentState): # expands
			if neighbor[1] not in discovered:
				og = [str(neighbor[0])] # for code shortening
				ad = parents[tuple(flatten(currentState))] + og
				parents [tuple(flatten(neighbor[1]))] = ad
				frontier.append(neighbor[1])
				discovered.append(neighbor[1])
	return None

# Arguments: state (list of lists)
# Returns: list of strings for steps to result

def DFS(state): # very similar code to above, but adds to front of frontier
	frontier = [state]
	discovered = [state]
	parents = {tuple(flatten(state)): []}
	while len(frontier) > 0:
		currentState = frontier.pop(0)
		if isGoal(currentState):
			return parents[tuple(flatten(currentState))]
		for neighbor in computeNeighbors(currentState):
			if neighbor[1] not in discovered:
				og = [str(neighbor[0])]
				ad = parents[tuple(flatten(currentState))] + og
				parents [tuple(flatten(neighbor[1]))] = ad
				frontier.insert(0, neighbor[1])
				discovered.append(neighbor[1])

# Arguments: state (list of lists)
# Returns: list of strings for steps to result

def BBFS (state): # twins code from before, adds to start/end from 2 dicts
	frontier1 = [state]
	side = len(state)
	solved = []
	number = 1
	for x in state:
		substore = []
		for y in state:
			substore.append(number)
			number = number + 1
		solved.append(substore)
	solved [side-1][side-1] = 0
	frontier2 = [solved]
	discovered1 = [state]
	discovered2 = [solved]
	parents1 = {tuple(flatten(state)): []} # two dicts, for start/end
	parents2 = {tuple(flatten(solved)): []}
	while len(frontier1) > 0:
		currentState = frontier1.pop(0)
		currentSolve = frontier2.pop(0)
		if currentState in discovered2: # checks if discovered twice
			og1 = parents2[tuple(flatten(currentState))]
			return parents1[tuple(flatten(currentState))] + og1
		elif currentSolve in discovered1:
			og2 = parents2[tuple(flatten(currentSolve))]
			return parents1[tuple(flatten(currentSolve))] + og2
		for neighbor in computeNeighbors(currentState):
			if neighbor[1] not in discovered1:
				g = [str(neighbor[0])]
				ad = parents1[tuple(flatten(currentState))] + g
				parents1 [tuple(flatten(neighbor[1]))] = ad
				frontier1.append(neighbor[1])
				discovered1.append(neighbor[1])
		for neighbor in computeNeighbors(currentSolve):
			if neighbor[1] not in discovered2:
				og = parents2[tuple(flatten(currentSolve))]
				ad = [str(neighbor[0])] + og
				parents2 [tuple(flatten(neighbor[1]))] = ad
				frontier2.append(neighbor[1])
				discovered2.append(neighbor[1])
	return None
def main():
	printer = LoadFromFile("testfile.txt")
	deBugPrint(printer)
	print(BBFS(printer))
	print(BFS(printer))
	print(DFS(printer))
main()
