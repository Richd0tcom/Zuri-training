import random as rd


def play(computer_action, user_action):

    if user_action == computer_action:
        print("Its a tie!") 
        user_action = input("pick an option between 'R', 'P' or 'S': ")
        play(computer_action, user_action)

    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")



options = ["R","P","S"]
opt= {"R":"Rock","P":"Paper","S":"Scissors"}

player = input("pick an option between 'R', 'P' or 'S': ")

computer = rd.choice(options)

# while ( not valid_option):
#     if not player in options:
#         player = input("pick an option between 'R', 'P' or 'S': ")
#         continue;
#     else:
while not player in options:
    player = input("ERROR: invalid option\n pick an option between 'R', 'P' or 'S': ")

print(f"Player({opt[player]}):CPU({opt[computer]})")
play(computer, player)






