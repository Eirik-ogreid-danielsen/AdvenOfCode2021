def input_handler(input):
        with open(input, 'r') as file:
            data = file.readlines()
            
        return data


def data_formater(data):
    diagnostics =[]
    for line in data:
        temps = line.split('|')
        diagnostic = []
        for temp in temps:
            diagnostic.append(temp.strip('\n').split())
        diagnostics.append(diagnostic)
    return diagnostics


def count_unique_digits(diagnostics):
    count = 0
    for diagnostic in diagnostics:
        for digit in diagnostic[1]:
            if len(digit)==2 or len(digit) == 4 or len(digit) ==7 or len(digit) == 3:
                count += 1
    return count


if __name__ == "__main__":
    data = input_handler('input.txt')
    diagnostics = data_formater(data)
    count = count_unique_digits(diagnostics)
    print(count)
