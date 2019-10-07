
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
        self.participantsNumber = Participant.howManyParticipants

        # Private Variable for Winnings
        self.__winnings = 2000

    def __str__(self):
        return "Object Info - Participant Name: %s %d , Participant Number:  %f" % (
        self.firstName, self.lastName, self.participantsNumber)

    def getFullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

# Testing & Debugging Code

# Creating Participant 1 Class
p1 = Participant("Jane", "Doe")

print(p1.getFullName(), p1.participantsNumber)
