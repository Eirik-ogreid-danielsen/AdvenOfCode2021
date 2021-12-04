import math 

def input_handler(input):
        with open(input, 'r') as file:
            data = file.readlines()
            
        return data

def bin_to_dec(binary):
    decimal = 0
    for num in enumerate(binary):
        #print(num[0])
        #print(num[1])
        if int(num[1]) == 1:
            decimal += math.pow(2,len(binary)-1-num[0])
            
    return int(decimal)

def bin_counter(data):
    counters = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in data:
        print(line.strip('\n'))
        for num in enumerate(line.strip('\n')):
            if int(num[1]) ==1:
                counters[num[0]] +=1
            else:
                pass
    return counters 

def find_binaries_engine(counters):
    binaries = {
        "gamma": '',
        "epsilon":''
    }
    for num in counters:
        print(num)
        if int(num) > 500:
            binaries['epsilon']+='1'
            binaries['gamma']+='0'
        else:
            binaries['epsilon']+='0'
            binaries['gamma']+='1'
    return binaries        

def list_to_dec(listDiagnostics):
    decimals = []
    for diagnostic in listDiagnostics:   
        binary = diagnostic.strip('\n')
        
        decimal = int(bin_to_dec(binary)) 
        print(decimal)
        decimals.append(decimal)
    return decimals

def generate_filter(size):
    bitFilter = []
    for i in range(size):
        bitSelector = int(math.pow(2,size-1-i))
        bitFilter.append(bitSelector)
    return bitFilter

def old_find_decimal_life_suport(counters,decimals):
    bitFilter = generate_filter(len(counters))
    print(bitFilter)
    oxygenList = []
    scrubberList = []
    bitnr=len(bitFilter)
    while len(oxygenList) !=1 and len(scrubberList) !=1:
        for i in range(len(bitFilter)):
            for decimal in decimals:
                tempOxygenList = []
                tempScruberList = []
                if counters[i]>=500:
                    print(f'there is :{len(oxygenList)} decimals in oxygenList')
                    filtered = decimal & bitFilter[i]
                    print(f'Cheking to see if {filtered} is equal to {bitFilter[i]}, this is checking bit:{i}')
                    if decimal & bitFilter[i] ==bitFilter[i] and len(oxygenList) != 1 :
                        #filtered = decimal & bitFilter[i]
                        print(f' {decimal} is part of oxygen, the filtered bit has a decimal value of {filtered}')
                        tempOxygenList.append(decimal)
                        #print(tempOxygenList)
                else:
                    print(f'there is :{len(scrubberList)} decimals in scrubberList')
                    filtered = decimal & bitFilter[i]
                    print(f'Cheking to see if {filtered} is  not equal to {bitFilter[i]}, this is checking bit:{i}')
                    if decimal & bitFilter[i] !=bitFilter[i] and len(scrubberList) != 1:
                        #filtered = decimal & bitFilter[i]
                        print(f' {decimal} is part of scrubber, the filtered bit has a decimal value of {filtered}')
                        tempScruberList.append(decimal)
                        #print(tempScruberList)
                if len(oxygenList) != 1 :
                    oxygenList = tempOxygenList
                    print(oxygenList)
                    
                if len(scrubberList) != 1:
                    scrubberList = tempScruberList
                    print(scrubberList)
                
    decimalDict = {
        "oxygen": oxygenList[0],
        "scrubber":scrubberList[0],
    } 
    print(decimalDict)
    return decimalDict

def find_decimal_life_suport(counters,decimals):
    bitFilter = generate_filter(len(counters))
    print(bitFilter)
    oxygenList = decimals
    scrubberList = decimals
    while len(oxygenList) !=1 and len(scrubberList) !=1:
        for i in range(len(bitFilter)):
            tempOxygenList = []
            tempScruberList = []
            if len(oxygenList) !=1: 
                for num in oxygenList:
                    filtered = num & bitFilter[i]
                    if counters[i] >= 500:
                        if filtered == bitfilter[i]:
                            tempOxygenList.append(num)
                    else: 
                        if filtered != bitfilter[i]:
                            tempOxygenList.append(num)
            else:
                    print("oxygenList is now one: skipping oxygen check")
                    print(f'iam currently checking bit {i}')
                    print(oxygenList)
            if len(scrubberList) !=1 :
                for num in scrubberList:
                    filtered = num & bitFilter[i]
                    if counters[i] < 500:
                        if filtered != bitfilter[i]:
                            tempScruberList.append(num)
                    else:
                        if filtered == bitfilter[i]:         
                            tempScruberList.append(num)
            else:
                print("scrubberList is now one: skipping scrubber check")
                print(f'iam currently checking bit {i}')
                print(scrubberList)
            if len(tempOxygenList) != 0:
                print(tempOxygenList)
                oxygenList = tempOxygenList
            if len(tempScruberList) != 0:
                print(tempScruberList)
                scrubberList = tempScruberList
    decimalDict = {
    "oxygen": oxygenList[0],
    "scrubber":scrubberList[0],
     } 
    print(decimalDict)
    return decimalDict

def find_oxygen(counters,decimals):
    oxygenList = decimals  
    bitFilter = generate_filter(len(counters))
    print(bitFilter)
    #check every bit for conditions until we reach a lone number
    for i in range(len(bitFilter)):
            print(f'checking bit:{i}')
            tempOxygenList = []
            for num in oxygenList:
                filtered = num & bitFilter[i]                   #isolates the correct bit
                if counters[i] >= len(decimals)/2:          #check if there are more high bits
                    print(f'there are more high bits, getting high bits')
                    if filtered == bitFilter[i]:                    #checks if bit is high
                        tempOxygenList.append(num)      #add the num with matching bit to the tempList
                else:                                                      #there are more low bits   
                    print(f'there are more low bits, getting low bits')   
                    if filtered != bitFilter[i]:                     #checks if bit is low     
                        tempOxygenList.append(num)      #add the num with matching bit to the tempList    
            oxygenList = tempOxygenList                  #replaces the list of diagnostics numbers with the new oxygen numbers       
            if i == 0 and len(oxygenList) == counters[0]:
                print('then first oxygen selection is correct')     
            print(oxygenList)
            if len(oxygenList) == 1:
                
                print("breaking")
                print(f'oxygenlist: {oxygenList}')
                break
    oxygen = oxygenList[0]
    print(oxygen)
    return oxygen

def separate_bits_lh(decimals,bitFilter):
    highBits = []
    lowBits = []
    for decimal in decimals:
        if decimal & bitFilter == bitFilter:
            highBits.append(decimal)
        else:
            lowBits.append(decimal)
    bits = [lowBits,highBits]
    return bits

def find_scrubber(counters,decimals):
    scrubberList = decimals  
    bitFilter = generate_filter(len(counters))
    print(bitFilter)
    #check every bit for conditions until we reach a lone number
    for i in range(len(bitFilter)):
            print(f'checking bit:{i}')
            tempScrubberList = []
            for num in scrubberList:
                filtered = num & bitFilter[i]                   #isolates the correct bit
                if counters[i] >= len(decimals)/2:          #check if there are more high bits
                    print(f'there are more high bits, getting low bits')
                    if filtered != bitFilter[i]:                    #checks if bit is low
                        tempScrubberList.append(num)      #add the num with matching bit to the tempList
                else:  
                    print(f'there are more low bits, getting high bits')                                                    #there are more low bits      
                    if filtered == bitFilter[i]:                     #checks if bit is high     
                        tempScrubberList.append(num)      #add the num with matching bit to the tempList    
            scrubberList = tempScrubberList                  #replaces the list of diagnostics numbers with the new oxygen numbers  
            if i == 0 and len(scrubberList) == len(decimals) - counters[0]:
                print('then first scrubber selection is correct')            
            print(scrubberList)
            if len(scrubberList) == 1:
                
                print("breaking")
                print(f'scrubberlist: {scrubberList}')
                break
    scrubber = scrubberList[0]
    print(scrubber)
    return scrubber
def find_scrubber_better(counters,decimals):
    scrubberList = decimals  
    bitFilters = generate_filter(len(counters))
    print(f'checking numbers against filter with size: {len(bitFilters)}')
    for i in range(len(bitFilters)):
        print(f'checking bit nr:{12-0}')
        bits = separate_bits_lh(scrubberList,bitFilters[i])
        print(f' nr high bits:{len(bits[1])}, nr low bits: {len(bits[0])}') 
        if len(bits[1]) >= len(bits[0]):
            print(f'There are more or equal high bits, scrubber takes the low bits')
            scrubberList = bits[0]

        else:
            print(f'There are more low bits, scrubber takes the high bits')
            scrubberList = bits[1]
        print(scrubberList)
        if len(scrubberList) == 1:
                print("breaking")
                print(f'scrubberlist: {scrubberList}')
                break
    return scrubberList[0]

def find_oxygen_better(counters,decimals):
    oxygenList = decimals  
    bitFilters = generate_filter(len(counters))
    print(f'checking numbers against filter with size: {len(bitFilters)}')
    for i in range(len(bitFilters)):
        print(f'checking bit nr:{12-0}')
        bits = separate_bits_lh(oxygenList,bitFilters[i])
        print(f' nr high bits:{len(bits[1])}, nr low bits: {len(bits[0])}') 
        if len(bits[1]) >= len(bits[0]):
            print(f'There are more or equal high bits, oxygen takes the high bits')
            oxygenList = bits[1]
        else:
            print(f'There are more low bits, oxygen takes the low bits')
            oxygenList = bits[0]
        print(oxygenList)
        if len(oxygenList) == 1:
                print("breaking")
                print(f'oxygenlist: {oxygenList}')
                break
    return oxygenList[0]

def test_filter_generator():
    filters = [2048,1024,512,256,128,64,32,16,8,4,2,1 ]
    print(len(filters))
    bitFilters= generate_filter(len(filters))
    print(bitFilters)
    if filters == bitFilters:
        print("success")
def test_filter():
    testdata = [2522,98]
    bitFilter = generate_filter(12)
    for i in range(len(bitfilter)):
        print(f'testing bit {i}:')
        data0 = testdata[0] & bitFilter[i]
        data1 = testdata[1] & bitFilter[i]
        print(f'bit:{i} is:{data0} for test 1 ')
        print(f'bit:{i} is:{data1} for test 2 ')

        

if __name__ == "__main__":
    data=input_handler('input.txt')
    counters=bin_counter(data)
    #print(counters)
    binaries= find_binaries_engine(counters)
    print(binaries)
    gamma = bin_to_dec(binaries['gamma'])
    print(f'gamma:{gamma}')
    epsilon = bin_to_dec(binaries['epsilon'])
    print(f'epsilon:{epsilon}')
    answer = gamma*epsilon
    print(answer)
    decimals = list_to_dec(data)
    bitfilter = generate_filter(len(counters))
    print(bitfilter)
    for i in range(len(counters)):
        print(i)
        print(bitfilter[i])
    #lifeSuport = find_decimal_life_suport(counters, decimals)
    #print(lifeSuport)
    #oxygen = find_oxygen(counters,decimals)
    #scrubber = find_scrubber(counters,decimals)
    #finalAnswer = oxygen*scrubber
    #print(f'Final answet: {finalAnswer}')
    #test_filter_generator()
    #test_filter()
    better_scrubber = find_scrubber_better(counters,decimals)
    better_oxygen = find_oxygen_better(counters,decimals)
    print(better_scrubber)
    print(better_oxygen)
    better_answer = better_scrubber*better_oxygen
    print(better_answer)
  
    
   