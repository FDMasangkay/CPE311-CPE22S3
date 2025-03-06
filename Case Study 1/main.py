class GoldenTime():
    def __init__(self): # A pre-existing available time is already here
        self.illness = {
            'heart attack' : 3600,
            'stroke' : 21600,
            'trauma' : 3600,
            'asthma attack' : 3600,
            'severe dehydration' : 7200,
            'septic shock' : 3600,
            'dengue hemorrhagic fever' : 86400,
            'severe allergic reaction' : 3600,
            'third-degree burns' : 3600,
            'tetanus' : 7200,
            'severe pneumonia' : 3600,
            'severe malaria' : 43200
            }

    # Simply shows the current data inside the dictionary.
    def show_golden_time(self):
        print(f'\ncurrently stored golden times (name : seconds) : \n{self.illness}')

    # This can be used to insert a new Illness with its corresponding time on
    # the dictionary, don't mind this if you are not the user since you will
    # actually need to edit the dictionary directly if you want to save it for
    # later use...
    def add_golden_time(self):
        while True:
            try:
                ill  = str(input('\nPlease input the name of the illness : '))
                time = int(input('Please input the Golden Time in SECONDS of the illness : '))
                break
            except ValueError:
                print('PLease insert the time in whole integers!')
        ill = ill.lower()
        self.illness[ill] = time
        print(f'updated [{ill} : {time}] to the dictionary.')
        self.show_golden_time()

    # simply calculates whether some common possible illnesses in the philippines is
    # survivable with the given distance both in the minimum and maximum speed limit
    # compared to its golden hour expressed in seconds.
    def golden_survival(self, min_distance):
        min_speed    = round((min_distance / 16.67), 4) # m/s
        max_speed    = round((min_distance / 27.78), 4) # m/s
        print(f'\n{min_speed} seconds is the amount of time it will take going on the minimum speed limit')
        print(f'{max_speed} seconds is the amount of time it will take going on the maximum speed limit\n')
        for i in self.illness:
            print(f'\nTesting {i}\n')
            min_survival = True
            max_survival = True
            if self.illness[i] < min_speed:
                print(f'{i} FAILED the minimum speed')
                min_survival = False
            else: print(f'{i} PASSED the minimum speed')
            if self.illness[i] < max_speed:
                print(f'{i} FAILED the max_speed')
                max_survival = False
            else: print(f'{i} PASSED the minimum speed')
            if min_survival == True and max_survival == True: print(f'{i} passed both test!')

        if min_survival == True and max_survival == True: print('\nall common illnesses are survivable!')
        else: print('\nthere were some illnesses that failed either or both minimum and maximum speed.')

SimulatedRoads = { # Distances of each node from their adjacent nodes.
    'A' : [('B', 100), ('C', 150), ('D', 800)],
    'B' : [('A', 100), ('C', 250), ('E', 350)],
    'C' : [('A', 150), ('B', 250), ('HOSPITAL', 300)],
    'D' : [('A', 800), ('HOSPITAL', 1000)],
    'E' : [('B', 350), ('HOSPITAL', 30)],
    'HOSPITAL' : [('E', 30), ('C', 300), ('D', 1000)]
}


# dijkstra algorithm will be used here, for now the program will manually input
# the minimum distance...
def GoldenSort(roads, start, end, golden_time):
    pass

if __name__ == '__main__':
    program = GoldenTime()
    while True:
        x = input('\n1 = add illness\n2 = show current illnesses\n3 = simulate golden time\n0 = end program\nX = ')
        if x == '1':
            program.add_golden_time()
        elif x == '2':
            program.show_golden_time()
        elif x == '3':
            temp = 450 # this is a sample minimum distance output...
            print(f'shortest distance : {temp}')
            program.golden_survival(temp)
        elif x == '0':
            break
        else: print('invadid input!')
    print('Program Terminated, goodbye!')