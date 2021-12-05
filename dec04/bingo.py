

def input_handler(input):
        with open(input, 'r') as file:
            data = file.readlines()
            
        return data

def get_numbers(data):
    numbers = []
    numbersStringList = data[0].split(',')
    for num in numbersStringList:
        numbers.append(int(num))
    print(numbers)
    return numbers

def get_cards(data):
    cardsets = []
    counter = 0
    cardStart = 2
    cardEnd = cardStart +5
    record = False
    card = [[],[],[],[],[]]
    drawnCard = [[],[],[],[],[]]
    for line in enumerate(data):
        if line[0]== cardStart:
            record = True
            cardStart += 6
        elif line[0] ==cardEnd:
            record = False
            cardEnd += 6
            
            counter = 0
        if record : 
            cardLine = []
            inputLine = line[1].strip('\n').split()
            for num in inputLine:
                intNum =int(num)
                cardLine.append(intNum)
            card[counter] = cardLine
            
            drawnCard[counter] = [0,0,0,0,0]
            counter += 1
            if line[0] == cardEnd -1:
                cardset = [card,drawnCard]
                cardsets.append(cardset)
                card = [[],[],[],[],[]]
                drawnCard = [[],[],[],[],[]]

        else:
            pass
    return cardsets

def find_nr(card, num):
    result = [False,None]
    for j in range(len(card)):
        for i in range(len(card[j])):
           # print(f'checking if {card[j][i]} = {num}')
            if card[j][i] == num:
                result = [True,[j,i]]
                print(result)
                break          
    return result

def mark_found(cords, card):
    card[cords[0]][cords[1]] = 1
    print(card)

def check_Bingo(card):
    
    columSums = [0,0,0,0,0]
    result= [False,False,None]
    for j in range(len(card)):
        rowSum = 0
        for i in range(len(card[j])):
            
            rowSum += card[j][i]
            columSums[i] += card[j][i] 
            #print(f'rowsum for  row:{rowSum}')
            #print(f'columSums: {columSums}')
            if rowSum == 5:
                result = [True,True,j]
                print(f'Bingo in row:{j}')
                break
            elif 5 in columSums :
                colum = columSums.index(5)
                result=[True,False,colum]
                print(f'Bingo in colum:{colum}')
                break
    return result

def lets_play_bingo(cardSets,numbers):
    result=[False,None,False,None,None]
    print(f'there are:{len(cardSets)}cards')
    print(cardSets)
    for num in numbers:

        for cardset in enumerate(cardSets):
            print(f'checking if num:{num} is in cardset: {cardset[0]}')
            card = cardset[1][0]
            result = find_nr(card,num)
            if result[0]:
                mark_found(result[1],cardset[1][1])
                bingo = check_Bingo(cardset[1][1])
                if bingo[0]:
                    result = [True,cardset[0],bingo[1],bingo[2],num]
                    print('IT`S A BINGO!')
                    return result
        

    return result  
def get_answer(cardset,winning):
    cardSum =0
    card = cardset[0]
    marks = cardset[1]
    winning = winning
    for j in range(len(card)):
        for i in range(len(card[j])):
            if marks[j][i] == 0:
                cardSum+= card[j][i]
                print(cardSum)
    answer = cardSum*winning

    return answer

def find_worst_card(cardSets,numbers):
    remainingCardSets = cardSets
    while len(remainingCardSets) !=1:
        print(f'there are: {len(remainingCardSets)} cardSets remaining:')
        cardSetsInPlay = remainingCardSets
        winner = lets_play_bingo(cardSetsInPlay,numbers)
        remainingCardSets.remove(remainingCardSets[winner[1]])
    cardSet = remainingCardSets[0]
    print(f'This is the worst possible card!{cardSet}')
    result = lets_play_bingo(remainingCardSets,numbers)
    
    return [cardSet, result]

if __name__ == "__main__":

    data =input_handler('input.txt')
    #data = input_handler('example.txt')
    numbers = get_numbers(data)
    
    get_cards(data)
    cardSets = get_cards(data)
card = cardSets[0][0]
print(len(cardSets[0][0]))
print(card[0])
result = find_nr(card,13)
print(result)
winner = lets_play_bingo(cardSets,numbers)
print(winner)
answer = get_answer(cardSets[winner[1]],winner[4])
print(f'The winning Board is: {winner[1]} and the winning colum or row is: {cardSets[winner[1]]}')
print(f'The puzzle answer is: {answer}')
loserConditions = find_worst_card(cardSets,numbers)
#loser = lets_play_bingo(loserCard,numbers)
loserAnswer = get_answer(loserConditions[0],loserConditions[1][4])
print(f'The puzzle 2 answer is: {loserAnswer}')
#print(cardSets[0][1])
#for num in numbers:
#    print(f'checking if {num} is in card')
#    res = find_nr(card,num)
#    if res[0] == True:
#        print(f'found Number in card, marking location{res[1]}')
#        mark_found(res[1],cardSets[0][1])
#        bingo = check_Bingo(cardSets[0][1])
#        if bingo[0]:
#            break
#print(cardSets[0])
