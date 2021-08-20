from checks import*
from movement import*
#calculates f(n) value
#checks
#inputs: first: currentState, second: current g(n) value
def blockingHeuristic(start,gn):
    if isgoal(start) == True:
        return 0
    endOfCar = 0    #if car is state is x x (blank)  since there is x and blank next to each other
                    #that means that the second x is the end of the car if looking left to right
    count = 1
    for i in range(len(start[2])):
        if start[2][i] == 'X' and start[2][i+1] != 'X':
            endOfCar = i
            break
    for j in range(endOfCar+1,6): #checks how many blocking cars from end of the xx car to end of board row.
        if start[2][j] != '-': 
            count += 1
    fn = count + gn
    return fn   #returns f(n) value



#My heruristic adds another complexity to the original blocking heuristic by checking if a
#blocking car is blocked as well.
#if the blocking car is blocked add 2 to the f(n)
#if the blocking car is not blocked add 1 to the f(n)
#inputs: start = current state, g(n)
def myHeuristic(start,gn):
    if isgoal(start) == True:
        return 0
    endOfCar = 0
    for i in range(len(start[2])):
        if start[2][i] == 'X' and start[2][i+1] != 'X':
            endOfCar = i
            break
    vertCars = findVertCars(start)
    count = 0
    for j in range(endOfCar+1,6):
        if start[2][j] != '-':
            if start[0][j] == start[2][j]:
                if start[3][j] != '-':
                    count += 2
                else:
                    count += 1
            if start[4][j] == start[2][j]:
                if start[5][j] != '-':
                    count +=2
                else:
                    count += 0
            if start[1][j] == start[2][j]:
                if start[0][j] != '-' and start[3][j] != '-':
                    count += 2
                else:
                    count += 1
            if start[3][j] == start[2][j]:
                if start[1][j] != '-' and start[4][j] != '-':
                    count += 2
                else:
                    count += 1
            if start[1][j] == start[2][j] and start[3][j] == start[2][j]:
                if start[0][j] != '-' and start[4][j] != '-':
                    count += 2
                else:
                    count += 1
        fn = count + gn
    return fn