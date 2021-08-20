import copy
from checks import*
#Finds all horizontal cars the game by getting the start and end indexes of each car.
#returns all horizontal car indexes by returning each's front and end indexes.
def findHoriCars(start):
    carIndexes = []
    for i in range(6):
        j = 0
        while j < 5:
            if start[i][j]!='-' and start[i][j+1] == start[i][j]:
                head = [i,j]  
                if j+2<=5:
                    if start[i][j+2] == start[i][j]:  #checks the whole playing field this way
                        endOfCar = [i,j+2]  
                        j+=3
                    else:
                        endOfCar = [i,j+1]
                        j+=2
                else:
                    endOfCar = [i,j+1]
                    j+=2
                carIndexes.append([head,endOfCar])  #returns a list of lists containing each hori cars 
                #front and end of car indexes
            else:
                j+=1
    return carIndexes

#Finds all vertical cars in the game by getting the start and end indexes of each car.
#returns all vertical car indexes by returning each's front and end indexes.
def findVertCars(start):
    carIndexes = []
    for j in range(6):
        i = 0
        while i < 5:
            if start[i][j]!='-' and start[i+1][j] == start[i][j]:
                head = [i,j]
                if i+2<= 5:
                    if start[i+2][j] == start[i][j]:
                        endOfCar = [i+2,j]
                        i+=3
                    else:
                        endOfCar = [i+1,j]
                        i+=2
                else:
                    endOfCar = [i+1,j]
                    i+=2
                carIndexes.append([head,endOfCar])
            else:
                i+=1
    return carIndexes        

#MOVEMENT AREA--------------------------------
        
# This function generates a new state when one vertical car moves 1 unit up
def verticalCarMoveUp(start,head,endOfCar):
    slot = start[head[0]][head[1]]
    newState = copy.deepcopy(start)
    newState[head[0]-1][head[1]] = slot
    newState[endOfCar[0]][endOfCar[1]]= '-'
    return newState

# This function generates a new state when one vertical car moves 1 unit down
def verticalCarMoveDown(start,head,endOfCar):
    slot = start[head[0]][head[1]]
    newState = copy.deepcopy(start)
    newState[endOfCar[0]+1][endOfCar[1]]= slot
    newState[head[0]][head[1]]= '-'
    return newState

# This function generates a new state when one horizontal car moves 1 unit left 
def horiLeft(start,head,endOfCar):
    slot = start[head[0]][head[1]]
    newState = copy.deepcopy(start)
    newState[head[0]][head[1]-1] = slot
    newState[endOfCar[0]][endOfCar[1]]= '-'
    return newState

# This function generates a new state when one horizontal car moves 1 unit right
def horiRight(start,head,endOfCar):
    slot = start[head[0]][head[1]]
    newState = copy.deepcopy(start)
    newState[endOfCar[0]][endOfCar[1]+1]= slot
    newState[head[0]][head[1]]= '-'
    return newState


# generates all possibles states from the current state
def generateNew(start,g,myqueue):
    result = []
    allHorizontalCars = findHoriCars(start)
    allVerticalCars = findVertCars(start)
    for a in range(len(allHorizontalCars)):
        front = allHorizontalCars[a][0]
        endOfCar = allHorizontalCars[a][1]
        if front[1]>0 and start[front[0]][front[1]-1] == '-':
            temp = horiLeft(start,front,endOfCar)
            if hasCycle(myqueue,temp):
                result.append(temp)
        if endOfCar[1]<5 and start[endOfCar[0]][endOfCar[1]+1] == '-':
            temp = horiRight(start,front,endOfCar)
            if hasCycle(myqueue,temp):
                result.append(temp)
    for b in range(len(allVerticalCars)):
        front = allVerticalCars[b][0]
        endOfCar = allVerticalCars[b][1]
        if front[0]>0 and start[front[0]-1][front[1]] == '-':
            temp = verticalCarMoveUp(start,front,endOfCar)
            if hasCycle(myqueue,temp):
                result.append(temp)
        if endOfCar[0]<5 and start[endOfCar[0]+1][endOfCar[1]] == '-':
            temp = verticalCarMoveDown(start,front,endOfCar)
            if hasCycle(myqueue,temp):
                result.append(temp)
    return result
