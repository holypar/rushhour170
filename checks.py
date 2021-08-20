
#Returns a list of lists from the current input
def listOfLists(start):
    myList = []
    for symbol in start:
        myList.append(list(symbol))
    return myList #WORKS AS INTENDED

#Checks if goal state is reached, and that can be told by seeing if the car XX has reached the end of the 3rd row
def isgoal(start):
    if (start[2][4] == 'X' and start[2][5]== 'X'):
        return True
    return False   #WORKS AS INTENDED


#inputs: collectedPaths is all paths that have been fully explored, we compare the current state to collectedPaths 
#to see if there are any elements out of position
#if there are, the counter goes up.
def elementsOutofPosition(collectedPaths,start):
    elementsOutofPosition = 0
    for a in range(6):
        for b in range(6):
            if start[a][b] != collectedPaths[0][a][b]:
                elementsOutofPosition += 1 
    return elementsOutofPosition                        #maybe this one is off?

#simply checks if there is a cycle 
# first input is all previous states, and second input is current state
#returns False if the newly generated state existed before, true elsewise
#mainly used in generatenew function 
def hasCycle(myQ,start):
    if start in myQ:
        return False
    return True    #works as intended

        