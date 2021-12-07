import math


def input_handler(input):
        with open(input, 'r') as file:
            data = file.readline()
            
        return data

def initialize_crabs(data):
    crabs = []
    positionCounter = []
    stringCrabs = data.split(',')
    for stringCrab in stringCrabs:
        crab = int(stringCrab)
        
        if crab in crabs:
            for position in enumerate(positionCounter):
                
                if position[1][0] == crab:
                    positionCounter[position[0]][1] += 1
        else:
            position = [crab,1]
            positionCounter.append(position)
        crabs.append(crab)
    return crabs, positionCounter


def calculate_fuel_costs(positionCounts, target):
    fuelCost = 0
    for position in positionCounts:
        fuelCost+= abs(position[0]-target)*position[1]
    return fuelCost

def find_smallest_fuel_cost(positionCounts):
    fuelCosts = []
    smallest = None
    for positionCount in positionCounts:
        fuelCost = calculate_fuel_costs(positionCounts,positionCount[0])
        fuelCosts.append(fuelCost)
        if smallest == None or fuelCost < smallest[1]:
            smallest = [positionCount, fuelCost]
    return smallest


def calculate_fuel_costs2(positionCounts, target):
    fuelCost = 0
    for position in positionCounts:
        distance = abs(position[0]-target)
        positionCost= 0
        #print(f'Distance: {distance}')
        for i in range(distance):

            stepCost = i +1
            #print(f'Step: {stepCost}')
            positionCost += stepCost
            #print(f'positionCost:{positionCost}')
        fuelCost+= positionCost*position[1]
        #print(f'Cost to get to: {target} from: {position} is: {positionCost}')
    return fuelCost

def find_smallest_fuel_cost2(positionCounts):
    fuelCosts = []
    smallest = None
    for positionCount in positionCounts:
        fuelCost = calculate_fuel_costs2(positionCounts,positionCount[0])
        fuelCosts.append(fuelCost)
        #print(f'Fuel cost for position: {positionCount} is: {fuelCost}')
        if smallest == None or fuelCost < smallest[1]:
            smallest = [positionCount, fuelCost]
    
    return smallest

def tune_smallest_cost(positionCounts,target):
    smallest  = None
    direction  = -1
    for i in range(target-1,target+2,2):
        fuelCost = calculate_fuel_costs2(positionCounts,i)
        if smallest == None or fuelCost < smallest[1]:
            smallest = [i, fuelCost]
            if smallest == None:
                pass
            else:
                direction += 1
                running = True
    while running:
        for i in range(smallest[0],smallest[0]+direction+1):
            fuelCost = calculate_fuel_costs(positionCounts,i)
            if smallest == None or fuelCost < smallest[1]:
                smallest = [i, fuelCost]
            else:
                running = False
    return smallest
            





if __name__ == "__main__":
    testString='16,1,2,0,4,2,7,1,2,14'
    testCrabs, testPositions = initialize_crabs(testString)
    data = input_handler('input.txt')
    crabs, crabPositions = initialize_crabs(data)
    #print(crabs)
    #print(crabPositions)
    testPositions.sort()
    print(testCrabs)
    print(testPositions)
    testAnswer = calculate_fuel_costs(testPositions,5)
    print(testAnswer)
    smallest = find_smallest_fuel_cost(testPositions)
    print(f'The smallest fuel cost is: {smallest[1]} for target position: {smallest[0]}')

    answer = find_smallest_fuel_cost(crabPositions)
    print(f'The smallest fuel cost is: {answer[1]} for target position: {answer[0]}')
    print('Part 2:')
    answer2 = find_smallest_fuel_cost2(crabPositions)
    print(f'The smallest fuel cost is: {answer2[1]} for target position: {answer2[0]}')
    testAnswer = calculate_fuel_costs2(crabPositions,5)
    print(testAnswer)
    answer3 = tune_smallest_cost(crabPositions,answer2[0][0])
    print(f'The smallest fuel cost is: {answer3[1]} for target position: {answer3[0]}')
    answer4 = calculate_fuel_costs2(crabPositions,answer3[0])
    print(answer4)
    
    #position4Cost = calculate_fuel_costs2(testCrabs,5)
    #print(f'Cost to reach position 4: {position4Cost}')
    #position2Cost = calculate_fuel_costs2(testCrabs,10)
   #print(f'Cost to reach position 2: {position2Cost}')