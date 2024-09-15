from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

computer = roles[randint(0,2)]

player = False

while player == False:
    player = input("Bear, Ninja, or Cowboy? > ")

    if computer ==  player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else:
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else:
            print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", computer, "defeats", player)
        else:
            print("You win!", player, "eats", computer) 

    play_again = input("Would you like to play again? (yes/no) > ")

    if play_again == "yes":
        player = False
        computer = roles [randint(0,2)]
    else:
        print("Thanks for playing!")
        break