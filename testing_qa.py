import importlib
importlib.import_module("117372043_Week4Lab1Assignment.py")

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

