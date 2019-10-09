'''

JACK LEONARD - 117372043
Week 4 Lab 1
Graded Assignment Submission

'''




##### Part A #######


class Participant:
    # class variables
    howManyParticipants = 0

    def __init__(self, firstName, lastName):
        # AI | First Name
        self.firstName = firstName

        # AII | Last Name
        self.lastName = lastName

        # AIII | Variable that counts how many instances of class created
        Participant.howManyParticipants += 1
        #AIV Participants Number
        self.participantsNumber = Participant.howManyParticipants

        # AV Private Variable for Winnings
        self.__winnings = 2000

        # AVI dictionary containing chars user presses as keys followed by the amount of times the participants has pressed the chars as items. This dict should be private

        self.__charsPressed = {"a":0, "b":0, "c":0, "d":0,} #TODO: Figure out how to keep track of individiual keys pressed

    def __str__(self):
        return "Object Info - Participant Name: %s %s , Participant Number:  %d" % (self.firstName, self.lastName, self.participantsNumber)

    #Getters & Setters
    def getFullName(self):
        return "%s %s" % ( self.firstName, self.lastName)

    def setFullName(self, new_full_name):
        firstName, lastName = new_full_name.split(" ")
        self.firstName = firstName
        self.lastName = lastName
    #F
    def getWinnings(self): #TODO not invoked in char press yet
        return self.__winnings

    #G
    def setWinnings(self, winnings_loses): #TODO not invoked in char press yet
        #Takes a tutle as input (amount_won,amount_lost)
        # From this the function should calculate how much money the participant has left over once the winning amount and losing amount has been applied to the participant’s overall winnings.
        winnings = self.__winnings
        return ((winnings - winnings_loses[1])+winnings_loses[0])


    #H - This function returns the character presses made by the participant as a list of tuples (i.e. not a dictionary).
    def getKeyPressInfo(self): #TODO not invoked in char press yet
        dictlist = []
        charsPressed = self.__charsPressed
        for key, value in charsPressed.items():
            temp = [key,value]
            dictlist.append(temp)
        return dictlist

    #I - Count how many tims a participant has clicked chars ('a', 'b', 'c', 'd',)
    def recordKeysPressed(self, char_pressed): #TODO not invoked in char press yet
        charDict = self.__charsPressed
        if char_pressed == "a" or char_pressed == "b" or char_pressed == "c" or char_pressed == "d":
            charDict[char_pressed] =+ 1
            #debug
            print(charDict)
        else: #this is actually superflous, I could just use the first statement but I'm leaving it here in case I need a special operation for disalowed keys
            print("Invalid Character")

        #This function is intended to count how many times a participant has clicked the characters a, b, c or d.

    #J - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.
    def getMaxKeyPress(self):
        highestvalue = 0
        highestValueList = []
        dictlist = self.__charsPressed
        # find highest values
        for item in dictlist.items():
            key = item[0]
            value = item[1]
            print(key, value)
            if value > highestvalue:
                highestvalue = value
                print(f"Highest Value: {highestvalue}")
        # find the chars with highest value
                for k, v in dictlist.items():
                    if v == highestvalue:
                        highestValueList.append((k, v))
                        print(highestValueList)
        return highestValueList

        # K - This function returns a list of tuples that hold the character(s) with the highest amount of key presses.
    def getMinKeyPress(self): #todo: check this !!
        minvalue = 0
        minvalueList = []
        dictlist2 = self.__charsPressed
        # find highest values
        for item in dictlist2.items():
            key = item[0]
            value = item[1]
            print(key, value)
            if value < minvalue:
                minvalue = value
                print(f"Min Value: {minvalue}")
                # find the chars with highest value
                for k, v in dictlist2.items():
                    if v == minvalue:
                        minvalueList.append((k, v))
                        print("Min Value List")
                        print(minvalueList)
            return minvalueList




















p1 = Participant("Jane", "Doe")
p1.setWinnings((100,50))

char_pressed = None
while char_pressed != 'q':
# this will continue to loop until the participant clicks 'q' key
    char_pressed = input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    # This is pretty ugly code, I code wrap some of this in a function and just recall
    if char_pressed == 'a':
        #class functions
        p1.getWinnings()
        p1.setWinnings((0,0))
        p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        g = p1.getKeyPressInfo()
        print(g)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
        #debug
        print(f"character a has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'b':
        #class functions
        p1.getWinnings()
        p1.setWinnings((0,0))
        p1.getKeyPressInfo()
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
        #debug
        print(f"character a has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'c':
        #class functions
        p1.getWinnings()
        p1.setWinnings((100,50))
        p1.getKeyPressInfo()
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
        #debug
        print(f"character a has been pressed. Winnings: {p1.getWinnings()}")
    elif char_pressed == 'd':
        # class functions
        p1.getWinnings()
        p1.setWinnings((0,0))
        p1.getKeyPressInfo()
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
        # debug
        print(f"character a has been pressed. Winnings: {p1.getWinnings()}")
    else:
        #class functions
        p1.getKeyPressInfo()
        g = p1.getKeyPressInfo()
        p1.recordKeysPressed(char_pressed)
        p1.getMaxKeyPress()
        p1.getMinKeyPress()
        #debug
        print("Invalid character pressed. Please enter a character: 'a', 'b', 'c' or 'd' ")





####### Testing & Debugging Code #######
# now stored in testing-qa.py :)

####### Testing & Debugging Code #######

# Creating instance of class
p1 = Participant("Jane", "Doe")
p2 = Participant("John", "Doe")

print(p1.getFullName(), p1.participantsNumber)
print(p2.getFullName(), p2.participantsNumber)
print(p1)
print(p2)

## Testing Getters & Setters

p1.setFullName("Janette Doe")
print(p1)
print(p1.setWinnings((100,50))) #works !!

print(p1.getKeyPressInfo()) # works !!

