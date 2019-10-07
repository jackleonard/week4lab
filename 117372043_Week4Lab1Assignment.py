'''

JACK LEONARD - 117372043
Week 4 Lab 1
Graded Assignment Submission

'''

char_pressed = None

while char_pressed != 'q':
  # this will continue to loop until the participant clicks 'q' key
    char_pressed = input("Please enter a character: 'a', 'b', 'c' or 'd' to reveal your winnings. Type 'q' to quit: ")
    if char_pressed == 'a':
      p1.setWinnings((0,100))
      print("character a has been pressed")
    elif char_pressed == 'b':
      print("character b has been pressed")
    elif char_pressed == 'c':
      print("character c has been pressed")
    elif char_pressed == 'd':
      print("character d has been pressed")




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

    def getFullName(self):
        return "%s %s" % ( self.firstName, self.lastName)

    def setFullName(self, new_full_name):
        firstName, lastName = new_full_name.split(" ")
        self.firstName = firstName
        self.lastName = lastName


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

