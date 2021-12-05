def input_handler(input):
        with open(input, 'r') as file:
            data = file.readlines()
            
        return data

def get_instructions(data):
    instructions = []
    for line in data:
        line.strip('\n')
        tempLine = line.split()
        instruction = [tempLine[0],tempLine[2]]
        instructions.append(instruction)
    return instructions


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.count = 1


def create_cords(instruction):
    instructionCords = []
    for strCords in instruction:
        tempCord = strCords.split(',')
        intCord = [0,0]
        for strNum in enumerate(tempCord):
            intNum = int(strNum[1])
            intCord[strNum[0]]= intNum
        instructionCords.append(intCord)    
    print(instructionCords) 
    return instructionCords


def create_points(intCords):
    points = []
    cords = intCords[0]
    endcords = intCords[1]
    print('CreatingCords')
    running = True
    while running :
        point = Point(cords[0],cords[1])
        points.append(point)
        print(point.x,point.y)
        if cords[0] < endcords[0]:
            cords[0]+=1
        if cords[0] > endcords[0]:
            cords[0]-=1
        if cords[1] < endcords[1]:
            cords[1]+=1
        if cords[1] > endcords[1]:
            cords[1]-=1
        if cords[0] == endcords[0] and cords[1] == endcords[1]:
            running = False
    point = Point(endcords[0],endcords[1])
    print(point.x,point.y)
    points.append(point)
    print('created points')
    return points

def check_if_diagonal(intCords):
    result = True
    start = intCords[0]
    end = intCords[1]
    if start[0] == end[0] or start[1] == end[1]:
        result = False
    return result

def get_pointsList(instructions):
    pointsList= []
    for instruction in instructions:
        cords = create_cords(instruction)
        if check_if_diagonal(cords):
            points = create_points(cords)
            pointsList.append(points)
        else:
            points = create_points(cords)
            pointsList.append(points)
    return pointsList


def find_matching_point(points, target):
    result = [False,None]
   
    for point in enumerate(points):
        if point[1].x == target.x and point[1].y == target.y:
            result[1] = point[0]
            result[0] = True
            
    return result

def count_points(pointslist):
    points = []
    totalpoints = 0
    
    for newPoints in pointslist:
        totalpoints += len(newPoints)
        pointsAdded = 0
        for newPoint in newPoints:
            #print('checking if point')
            result = find_matching_point(points,newPoint)
            if result[0]:
               
                i =  result[1]
                #print(f'point:{newPoint.x}{newPoint.y} is already in the list')
                points[i].count += 1
            else:
                points.append(newPoint)
                pointsAdded += 1
        #print(f'processed: {totalpoints} points')
        #print(f'added: {pointsAdded} to points, points is now:{len(points)} long')
        pointsAdded = 0
    return points

if __name__ == "__main__":
    testData = input_handler('example.txt')
    data = input_handler('input.txt')
    instructions = get_instructions(data)
    pointsList = get_pointsList(instructions)
    points = count_points(pointsList)
    answer = 0
    for point in points:
     if point.count >= 2:
         answer +=1
    print(answer)