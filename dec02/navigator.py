def input_handler(input):
        with open(input, 'r') as file:
            instructions = file.readlines()
            
        return instructions

class Submarine:
    depth = 0
    latitude = 0
    aim = 0

    def navigator(self, instructions):
        for instruction in instructions:
            words = instruction.split()
            #print(f'move {words[0]} for {words[1]}')
            self.interpreter(words)

    def defunct_interpreter(self, words):
        if words[0]== 'up':
            value = -int(words[1])
            print(f'up for {value}')
            self.move_depth(value)
        elif words[0] == 'down':
            value = int(words[1])
            print(f'down for {value}')
            self.move_depth(value)
        elif words[0] == 'forward':
            value = int(words[1])
            print(f'forward for {value}')
            self.move_latitude(value)
        elif words[0] == 'backward':
            print(f'backward for {value}')
            value = -int(words[1])
            self.move_latitude(value)

    def interpreter(self, words):
        if words[0]== 'up':
            value = int(words[1])
            #print(f'up for {value}')
            self.aim -= value
        elif words[0] == 'down':
            value = int(words[1])
            #print(f'down for {value}')
            self.aim += value
        elif words[0] == 'forward':
            value = int(words[1])
            print(f'forward for {value}')
            self.move(value)     


    def move_depth(self, value):
        self.depth += value
        print(f'new depth: {self.depth}')

    def move_latitude(self, value):
        self.latitude += value
        print(f'new latitude: {self.latitude}')

    def move(self,value):
        self.latitude += value
        self.depth +=  value*self.aim
        


if __name__ == "__main__":
    SeaElf = Submarine()
    instructions = input_handler('input.txt')
    SeaElf.navigator(instructions)
    answer = SeaElf.depth * SeaElf.latitude
    print(answer)