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
        self.firstName = firstName
        self.lastName = lastName
        self.howManyParticipants += 1
        self.participantsNumber = self.howManyParticipants  # TODO: Fix this - trying to declare and set variable that is automatically set to participants number

    def __str__(self):
        return "Object Info - Participant Name: %s %d , Participant Number:  %f" % (
        self.firstName, self.lastName, self.participantsNumber)

    def getFullName(self):
        return '{} {}'.format(self.firstName, self.lastName)


p1 = Participant("Jane", "Doe")
print(p1.getFullName())