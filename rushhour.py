import copy
from queue import PriorityQueue #for implementation of a star
from checks import *
from heuristics import*
totalstates = 0

#Parminder Singh
#Rush Hour, RUN THIS FILE 
#This is my main function that basically runs the whole assignment critera. 
#Takes in which heuristic to use 

#beginner test case
#rushhour(0,["--AABB", "--CDEF", "XXCDEF", "--GGHH", "------", "------"]) not prinitng anything graded on this RETURNS EMPTY LIST

# rushhour(0, ["--B---","--B---","XXB---","--AA--","------","------"]) RUNS

#test case #1 works
#rushhour(0,["---O--", "---O--", "XX-O--", "PQQQ--", "P-----", "P-----"])

#test case #2 NEED 18 works
#rushhour(0,["OOOP--", "--AP--", "XXAP--", "Q-----", "QGGCCD", "Q----D"])

#test case #3  need 15 works
#rushhour(0,["--OPPP", "--O--A", "XXO--A", "-CC--Q", "-----Q", "--RRRQ"])

#test case #4 need 30 works
#rushhour(0,["-ABBO-", "-ACDO-", "XXCDO-", "PJFGG-", "PJFH--", "PIIH--"])

#test case #5  55 moves RETURNS EMPTY LIST
#rushhour(0,["OOO--P", "-----P", "--AXXP", "--ABCC", "D-EBFF", "D-EQQQ"])

def rushhour(heuType,startState):
    global totalstates
    pq = PriorityQueue()
    totalstates = 0
    startList = listOfLists(startState)
    pq.put((0,startList))
    result = state_search(pq,[],0,heuType,[startList])  #this isnt returning anything
    print(result)
    moves = len(result) - 1
    print(result)
    print("Total moves: " + str(moves))
    print("Total states explored:" + str(totalstates))

def dummyfunction(mylist):
    return []

def state_search(pq,path,g,mode,allstates): 
    if pq == []:
        return []
    pqHead = pq.get()
    start = pqHead[1]
    if isgoal(start): #check if it is goal state
        return [start]
    else:
        temp = generateNew(start,g,allstates)
        for i in range(len(temp)): # this for loop put the newly generated states into priority queue
            global totalstates #for final print result on hw
            totalstates += 1 # count states explored
            if mode == 0:
                pq.put((blockingHeuristic(temp[i],g),temp[i]))
            else:
                pq.put((myHeuristic(temp[i],g),temp[i]))
            allstates.append(temp[i])
        path.append(start)
        result = state_search(pq,path,g+1,mode,allstates)
        difference = elementsOutofPosition(result,start)
        if difference == 2:
            result.insert(0,start)
        return result


