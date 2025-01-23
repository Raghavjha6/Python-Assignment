'''Q. Write a program for a matchstick game being played between the computer and a user. Your 
program should ensure that the computer always wins. Rules for the game are as follows:
• There are 21 matchsticks.
• The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
• After the person picks, the computer does its picking.
• Whoever is forced to pick up the last matchstick loses the game.'''

matchsticks = 21
while matchsticks > 1:
    user_pick = int(input("Pick 1, 2, 3, or 4 matchsticks: "))
    if user_pick not in [1, 2, 3, 4]:
        print("Invalid input. Pick again.")
        continue
    matchsticks -= user_pick
    computer_pick = 5 - user_pick
    print(f"Computer picks {computer_pick} matchsticks.")
    matchsticks -= computer_pick
    print(f"Matchsticks left: {matchsticks}")
if matchsticks == 1:
    print("You are forced to pick the last matchstick. You lose!")
