import copy
class State:
    global goalState
    goalState=[[1,2,3],[8,'B',4],[7,6,5]]

   #Constructor for state
    def __init__(self, state, move = '', cost = 0, depth = 0):
        self.state = state
        self.move = move
        self.cost = cost
        self.depth = depth
    
    def getState(self):
        return self.state

    #function to find index of blank space
    def findBlank(self):
        a = self.state
        for i in range(0,3):
            for j in range(0,3):
                if self.state[i][j] == 'B':
                    return [i,j] #if blank space is found, a list containing the indices is returned
        return False #if blank space isnt found, it returns False

    #Function to test if blank space can move right
    def canMoveRight(self):
        """if blank is in last position of inner lists, then it can't move right & function returns false"""
        if self.findBlank() == [0,2] or self.findBlank() == [1,2] or self.findBlank() == [2,2]: 
            return False
        else:
            return True
            

    #Function to test if blank space can move left
    def canMoveLeft(self):
        #if blank space is in first position of inner lists, then it can't move left & returns false
        if self.findBlank() == [0,0] or self.findBlank() == [1,0] or self.findBlank() == [2,0]:
            return False
        else:
            return True

    #Function to test if blank space can move up
    def canMoveUp(self):
        #if blank space is in the first inner list, then it can't move up & returns false
        if self.findBlank() == [0,0] or self.findBlank() == [0,1] or self.findBlank() == [0,2]:
            return False
        else:
            return True

    #Function to test if blank space can move down
    def canMoveDown(self):
        """if blank space is in last inner list, then it can't move down & returns false"""
        if self.findBlank() == [2,0] or self.findBlank() == [2,1] or self.findBlank() == [2,2]:
            return False
        else:
            return True

    #Function to move blank space right
    def moveRight(self):
        #create a new state to update 
        copyOf = copy.deepcopy(self.state)
        newState = State(copyOf,'right',self.cost + 1,self.depth + 1)
        position =  newState.findBlank() #find blank spot 
        x1,y1 = position[0],position[1] #indices of blank space
        newState.state[x1][y1] =  newState.state[x1][y1+1] #set value of blank space to the value of the right
        newState.state[x1][y1+1] = 'B' #set next tile over to blank space
        return newState #return state to add to a list of possible successors of parent

    #Function to move empty space right
    def moveLeft(self):
        #create a new state to update 
        copyOf = copy.deepcopy(self.state)
        newState = State(copyOf,'left',self.cost + 1,self.depth + 1)
        position = newState.findBlank()
        x1,y1 = position[0],position[1] #indices of blank space
        newState.state[x1][y1] = newState.state[x1][y1-1] #set value of blank space to the value of the value to the left
        newState.state[x1][y1-1] = 'B' #set next tile over to blank space
        return newState #return state to add to a list of possible successors of parent

    #Function to move empty space up
    def moveUp(self):
        #create a new state to update 
        copyOf = copy.deepcopy(self.state)
        newState = State(copyOf,'up',self.cost + 1,self.depth + 1)
        position =  newState.findBlank()
        x1,y1 = position[0],position[1] #indices of blank space
        newState.state[x1][y1] =  newState.state[x1-1][y1] #set value of blank space to the value of the above tile
        newState.state[x1-1][y1] = 'B' #set value of position above original blank space to the blank space value
        return  newState #return state to add to a list of possible successors of parent

    #Function to move empty space down
    def moveDown(self):
        #create a new state to update 
        copyOf = copy.deepcopy(self.state)
        newState = State(copyOf,'down',self.cost + 1,self.depth + 1)
        position = newState.findBlank()
        x1,y1 = position[0],position[1] #indices of blank space
        newState.state[x1][y1] =newState.state[x1+1][y1] #set valuen of blank space to the value of below position
        newState.state[x1+1][y1] = 'B' #set value of position below original blank space to the blank space value
        return newState

    def generateSuccessors(self):
        """check if move is valid & if it is, add the new state generated to a list of successor states"""
        successors = list()
        if self.canMoveRight():
            s = self.moveRight()
            successors.append(s)
        if self.canMoveLeft():
            s = self.moveLeft()
            successors.append(s)
        if self.canMoveDown():
            s = self.moveDown()
            successors.append(s)
        if self.canMoveUp():
            s = self.moveUp() 
            successors.append(s)
        return successors

    def print(self):
        print ("State: ", self.state, "   move: ",self.move , "     depth: ", self.depth, "      cost: ", self.cost)

    def __str__(self):
        return f'state: {self.state}, move: {self.move}, depth: {self.depth},cost: {self.cost}'

