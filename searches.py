from state import State
from collections import deque

class Searches:
    global goalState
    goalState=[[1,2,3],[8,'B',4],[7,6,5]]

    def __init__(self,startState):
        self.startState = State(startState)

    def bfs(self,initial):
        startState = State(initial)
        open = deque() #use deque as a queue with popleft to dequeue
        open.append((startState,startState.state)) #add initial configuration to the openlist
        closed = list() #closed is empty
        count = 1 #to keep count of the iterations
        """while open isnt empty, search"""
        while open: 
            b = open.popleft() #open contains a list of tuples 
            x = b[0]#x is the object of State
            if x.state == goalState: #if state is the goal, add x to closed list and return it
                closed.append(x.state)
                return closed
            else: #or else generate children and add x to closed list
                children = x.generateSuccessors()
                if children:    #if child states generated, add x to closed list
                    closed.append(x.state)
                    for c in children: #loop through list of possible successor states and add unvisited nodes to open list
                        if c.state in open: #do nothing with c if its already in open
                            continue 
                        elif c.state in closed: #do nothing with c if its already in closed
                            continue
                        else:
                            if c.state == goalState:  #if child is goal, add to closed list and return closed
                                closed.append(c.state)
                                return closed
                            else:
                                open.append((c,c.state))  #else add it to open
            count += 1 #increase counter
            if count == 70000: # at 70,000 iterations, stop search
                break
        return closed

    def dfs(self,initial):
        startState = State(initial)
        open = deque() #use deque as a stack by using pop to remove most recently entered state into the stack
        open.append(startState) #add initial configuration to the openlist
        closed = list() #closed is empty
        count = 1 #to keep count of the iterations
        """while open isnt empty, search"""
        while open:
            x = open.pop() #open contains a list of tuples 
            if x.state == goalState:  #if state is the goal, add x to closed list and return it
                closed.append(x.state)
                return closed
            else:
                children = x.generateSuccessors()
                if children:
                    closed.append(x.state)    #if children are generated, add x to closed list
                    for c in children: #loop through children generated and add to respective list
                        if c.state in open: #do nothing with c if its already in open
                            continue 
                        elif c.state in closed: #do nothing with c if its already in closed
                            continue
                        else:
                            if c.state == goalState: #if c is goal state, add it to closed & return closed
                                closed.append(c.state)
                                return closed
                            else:
                                open.append(c)
            count += 1 #increase counter
            if count == 70000: # at 70,000 iterations, stop search
                break
        return closed

    def hammingDistanace(self,state):
        result = 0
        a = list(state)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] != goalState[i][j]:
                    result += 1
        return result

   #method to find the position of the number in the goal state
    def findItem(self,item): #static method to find where the number is in the goal state 
        a = list(goalState)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j]==item:
                    return [i,j]
        return False

    def manhattanDistance(self,state): 
        sum = 0
        a = list(state)
        for i in range(len(a)):
            for j in range(len(a[i])):
                numInCurrentState = a[i][j]
                numInGoalState = self.findItem(numInCurrentState)
                x1,y1 = numInGoalState[0],numInGoalState[1]
                distance = abs(x1-i) + abs(y1-j)
                sum+=distance
        return sum

    def permutationInv(self,startstate):
        tempState = list(startstate.state)
        s = list()
        #flattens the list for processing
        for i in range(len(tempState)):
            for j in range(len(tempState[i])):
                s.append(tempState[i][j])
        #set blank to 0 for processing purposes 
        for i in range(len(s)): #loop to find blank
            if s[i] == 'B':
                s[i] = 0
        count = 0
        for i in s: #is left
            for j in range(i+1,len(s)): #j is values to the right of i 
                if s[i] == 1: #everything should be to the right of 1
                    continue
                elif (s[i] == 2 or s[i] == 3) and s[i] > s[j]: #any value on the right of 2,3 should be larger so if its not, its on the wrong side of i
                    count += 1
                elif s[i] == 8 and s[j] > 0 and s[j] < 4: #if value 1,2,3 is to the right of 8, add 1
                    count += 1
                elif s[i] == 0 and ((s[j] > 0 and s[j] < 4) or s[j] == 8): #tests if values located on the right of i are values are are supposed to be on left
                    count += 1
                elif s[i] == 4 and ((s[j] >= 0 and s[j] < 4) or s[j] == 8):
                    count += 1
                elif s[i] == 7 and ((s[j] >= 0 and s[j] <= 4) or s[j] == 8):
                    count += 1
                elif s[i] == 6 and ((s[j] >= 0 and s[j] <= 4) or s[j] >= 7): 
                    count += 1
                elif s[i] == 5 and i < 8: #5 should have nothing to the right so anyhting to the right would be added
                    count += 1
        return count
   
    #INADMISSIBLE HEURISTIC
    def nilssonsSequence(self,state): # = P(n) + 3*S(n)
        #P(n) is the manhattan distance
        p = self.manhattanDistance(state.state)
        #S(n) is (1 + 2*num_incorrect_pairs)
        goal = [1,2,3,8,'B',4,7,6,5]
        s = list() #for proccessing we need a flat list of the given state 
        tempState = list(state.state)
        for i in range(len(tempState)):
            for j in range(len(tempState[i])):
                s.append(tempState[i][j])
        count = 0 #count of incorrect pairs
        for i in range(len(s)):
            val = s[i]
            for j in range(len(goal)):
                if goal[j] == val and j < (len(goal)-1):
                    shouldBeNext = goal[j+1]
                else:
                    shouldBeNext = 0
            if i < (len(s)-1):
                if not(s[i+1] == shouldBeNext):
                    count +=1
        S = 3*(1 + 2*count) #value of S(n)
        return (p+S)
            
    def bestFirt(self,initial,heuristic):
        startState = State(initial,'',0,0)
        open = list() #implement a priority queue with a list but adding key,value pairs, sorting, and popping the first one
        closed = list()
        #set of if-elif to determine the h value for the passed heuristic 
        if heuristic == 'm': 
            h = self.manhattanDistance(startState.state) 
        elif heuristic == 'h':
            h = self.hammingDistanace(startState.state)
        elif heuristic == 'p':
            h = self.permutationInv(startState)
        elif heuristic == 'n':
            h = self.nilssonsSequence(startState)
        open.append([h,startState])
        count = 1
        """While the queue isnt empty, search"""
        while open:
            open.sort(key=lambda row: row[0])
            b = open.pop(0) #set current state to the state with the lowest h value
            x = b[1] #get method returns a tuple so we set a variable to the index containing the state
            if x.state == goalState:
                closed.append(x.state)
                return closed
            else:
                children = x.generateSuccessors()
                if children:
                    closed.append(x.state)    #if children are generated, add x to closed list
                    for c in children: #loop through children generated and add to respective list
                        if c.state in open: #do nothing with c if its already in open
                            continue
                        elif c.state in closed: #do nothing with c if its already in closed
                            continue
                        else:
                            if c.state == goalState: #if c is goal state, add it to closed & return closed
                                closed.append(c.state)
                                return closed
                            else: #if child isnt goal, calculate h value and add to open
                                #set of if-elif to determine the h value based on the heuristic passed
                                if heuristic == 'm': 
                                    h = self.manhattanDistance(c.getState()) 
                                elif heuristic == 'h':
                                    h = self.hammingDistanace(c.getState())
                                elif heuristic == 'p':
                                    h = self.permutationInv(c)
                                elif heuristic == 'n':
                                    h = self.nilssonsSequence(startState)
                                open.append((h,c,c.state))
            count += 1
            if count == 50000:
                break
        return closed

    def aStar(self,initial,heuristic):
        startState = State(initial,'',0,0)
        open = list() #implement a priority queue with a list but adding key,value pairs, sorting, and popping the first one
        closed = list()
        #set of if-elif to determine the h value for the passed heuristic 
        if heuristic == 'm': 
            h = self.manhattanDistance(startState.state) 
        elif heuristic == 'h':
            h = self.hammingDistanace(startState.state)
        elif heuristic == 'p':
            h = self.permutationInv(startState)
        elif heuristic == 'n':
            h = self.nilssonsSequence(startState)
        f = startState.cost + h #f-value is the key for priority queue
        open.append([f,startState])
        count = 1
        """While the queue isnt empty, search"""
        while open:
            open.sort(key=lambda row: row[0])
            b = open.pop(0) #set current state to the state with the lowest f value
            x = b[1] #get method returns a tuple so we set a variable to the index containing the state
            if x.state == goalState:
                closed.append(x.state)
                return closed
            else:
                children = x.generateSuccessors()
                if children:
                    closed.append(x.state)    #if children are generated, add x to closed list
                    for c in children: #loop through children generated and add to respective list
                        #set of elif to determine the h value based of passed heuristic 
                        if heuristic == 'm': 
                            h = self.manhattanDistance(c.getState()) 
                        elif heuristic == 'h':
                            h = self.hammingDistanace(c.getState())
                        elif heuristic == 'p':
                            h = self.permutationInv(c)
                        elif heuristic == 'n':
                            h = self.nilssonsSequence(startState)
                        f = c.cost + h
                        #if child is goal, add to closed and return
                        if c.state in open: #do nothin with c if its already in open
                            continue 
                        elif c.state in closed:#do nothing with c if its already in closed
                            continue
                        else:
                            if c.state == goalState: #if c is goal state, add it to closed & return closed
                                closed.append(c.state)
                                return closed
                            else: #if child isnt goal, add to open
                                open.append((f,c,c.state))
            count += 1
            if count == 50000:
                break
        return closed
