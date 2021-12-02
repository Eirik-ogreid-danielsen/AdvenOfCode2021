def get_sonar_input(input):
    with open(input, 'r') as file:
        sonar = file.readlines()
        return sonar

def depth_increase_rate(sonar):
    lastReading = None
    increases = 0

    for reading in sonar:
        if lastReading == None:
            lastReading = reading
            increases+=1
           # print(f'{reading}: No previous reading')
        
        else:
            if reading > lastReading:
                increases+=1
                lastReading=reading
            #    print(f'{reading}: Depth increasing')
            else:
                lastReading = reading
             #   print(f'{reading}: Depth decreasing')
    return increases


def create_sliding_windows(sonar, size):
    windows = []
    window = 0
    reads =0
    numwindows = int(int(len(sonar)/size)*size)
    print(numwindows)
    for reading in sonar:
            valueReading= int(reading)
            window = valueReading
            reads +=1
            print(len(windows))
            print(reads)
            if len(windows) < numwindows:
                windows.append(window)
            if len(windows)-2>0:
                windows[len(windows)-2] += valueReading
            if len(windows)-3>0:
                windows[len(windows)-3] += valueReading

                
            
           
        
    try:
                print(windows[2000])
    except:
                 print("there is no index at 2000")
    try:
                print(windows[1999])
    except:
                 print("there is no index at 1999")
    try:
                print(windows[1998])
    except:
                 print("there is no index at 1998")
    try:
                print(windows[1997])
    except:
                 print("there is no index at 1997")
            
        
    print(f'Created{len(windows)} windows out of {len(sonar)} readings, sliding window with size of {size}')
    return windows
    
def sliding_window_depth_increase_rate(sonar, size):
    windows = create_sliding_windows(sonar, size)
    increases = depth_increase_rate(windows)
    return increases




    


if __name__ == "__main__":
       sonar = get_sonar_input('input.txt')
       #increases = depth_increase_rate(sonar)
       #print(f'The depth increased a total of {increases} times')
       sliding_increases = sliding_window_depth_increase_rate(sonar, 3)
       print(f'With a sliding window of 3 the depth increased {sliding_increases} times')