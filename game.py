print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. '
                'Which way do you go? '
                'Type "left" or "right" ').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the leak. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across ').lower()
    if choice2 == "wait":
        choice3 = input('You arrive unharmed at the island unharmed. ' 
                        'You approach a house with three doors, one blue, one red, and one yellow. '
                        'Which door do you choose? Type "blue" "red" or "yellow" ').lower()
        if choice3 == "red":
            print("You're on fire. Game over.")
        elif choice3 == "yellow":
            print("You've been shot. Game over.")
        elif choice3 == "blue":
            print("You win the game! Congrats!!!")
        else:
            print("Come on. Type a color correctly next time. You lose")
    else:
        print("You've drowned. RIP. Game over")
else:
    print("Game over. You were attacked by pack of bears.")
