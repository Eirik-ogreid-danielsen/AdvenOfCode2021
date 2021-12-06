def input_handler(input):
        with open(input, 'r') as file:
            data = file.readline()
            print(data)
        return data

def get_start_fishies(data):
    fishies = []
    chars = data.split(',')
    for char in chars:
        fishies.append(int(char))
    return fishies


def initialize_population(spawnCycle,fishies):
    spawnList = []
    counts=[0]*spawnCycle
    for fishie in fishies:
        counts[fishie]+=1
    for i in range(len(counts)):
        if counts[i] != 0:
            spawnSet= {
                'day' : i,
                'amount': counts[i]
             }
            spawnList.append(spawnSet)
    return spawnList

    
def find_spawn_index(population):
    index = 0
    for i in range(len(population)):
        if population[i]['day'] == 8:
            index = i
    return index


def spawn_fishies(population,amount):
    spawnSet = {
        'day' : 8,
        'amount': amount
    }
    population.append(spawnSet)

def age_population(population,time): 
    spawn = False
    amount = 0
    spawning = []
    
    for day in range(time):
       # print(f'Day: {day} Population: {population}')
        print(f'Day: {day}')
        for spawnSet in enumerate(population):
            spawnSet[1]['day'] -=1
            if spawnSet[1]['day'] == -1:
                spawn = True
                amount += spawnSet[1]['amount']
                spawning.append(spawnSet[0])
        if spawn:
            print(f'Spawning: {amount} fishies')
            spawn_fishies(population,amount)
            spawn = False
            amount = 0
            for i in spawning:
                population[i]['day']=6
            spawning = []
               
                
        
        


def count_fishies(population):
    amount  = 0
    for spawnSet in population:
       amount += spawnSet['amount']
    return amount


if __name__ == "__main__":
    exampleData = [3,4,3,1,2]
    population = initialize_population(8,exampleData)
    print(population)
    time = 18


    age_population(population,time)
    print(population)
    amount=count_fishies(population)
    print(amount)
    population = initialize_population(8,exampleData)
    time = 80
    age_population(population,time)
    print(population)
    amount=count_fishies(population)
    print(amount)
    data = input_handler('input.txt')
    fishies = get_start_fishies(data)
    population = initialize_population(8,fishies)
    age_population(population,time)
    amount=count_fishies(population)
    print(amount)
    part2time = 256
    part2population = initialize_population(8,fishies)
    age_population(part2population,part2time)
    part2amount=count_fishies(part2population)
    print(part2amount)


    