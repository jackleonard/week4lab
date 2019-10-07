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
