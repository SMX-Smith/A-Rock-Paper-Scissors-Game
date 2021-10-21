# Will Smith
# Rock, paper scissors game
# 10/12/21
import random
WIDTH = 15


def play():
    win_count = 0
    loss_count = 0
    tie_count = 0
    while True:
        print("Press 'q' to quit")
        user_inp = input("\nRock, Paper, or Scissors?\n(R, P, or S): ")
        user_inp = user_inp.upper()
        computer_inp = random.choice(["R", "P", "S"])
        if user_inp == "Q":
            quit_game(win_count, loss_count, tie_count)
        print("Opponent chose: " + computer_inp + "\n")
        if computer_inp == user_inp:
            print("It\'s a tie!\n")
            tie_count += 1
        elif win(user_inp, computer_inp):
            print("You won!\n")
            win_count += 1
        else:
            print("You lost\n")
            loss_count += 1


# takes player and opponent input and determines winner
def win(player, opponent):
    if (player == "R" and opponent == "S") or (player == "P" and opponent == "R") or (
            player == "S" and opponent == "P"):
        return True


# prints out player's stats for the game
def quit_game(wins, losses, ties):
    print("\nGoodbye!\n\n\n")
    print("Your stats".center(WIDTH))
    print(WIDTH * '-')
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))
    exit()


if __name__ == '__main__':
    play()
