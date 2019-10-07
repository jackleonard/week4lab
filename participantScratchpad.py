
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
        return "Object Info - Participant Name: %s %d , Participant Number:  %f" % (
        self.firstName, self.lastName, self.participantsNumber)

    def getFullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

# Testing & Debugging Code

# Creating Participant 1 Class
p1 = Participant("Jane", "Doe")

print(p1.getFullName(), p1.participantsNumber)
