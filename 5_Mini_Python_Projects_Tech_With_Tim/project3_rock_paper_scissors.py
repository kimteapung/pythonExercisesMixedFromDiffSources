"""
This is done watching the video 5 Mini Python Projects - For Beginners on https://www.youtube.com/watch?v=DLn3jOsNRVE
I watched the videos and after that did the project not looking the actual codes.

42:53 | Project #3 - Rock, Paper, scissor
"""
import random


def start_game(game_list):
    """
    Start the game
    Variables:
    @count_the_play: int - how many you played the game
    :param game_list: list -  r = rock, s = scissor, p = paper, q = quit
    :return:
    """
    count_the_play = 0
    while True:
        computer_pick = game_list[random.randint(0, 2)]
        user_pick = str(input("Pick you side r = rock, s = scissor, p = paper, q = quit: ")).lower()
        if user_pick in game_list:
            if user_pick != "q":
                count_the_play += 1
                # r > s, s > p, p > r
                if user_pick != computer_pick:
                    # user WIN cases
                    if user_pick == "r" and computer_pick == "s" or user_pick == "s" and computer_pick == "p" or \
                            user_pick == "p" and computer_pick == "r":
                        print(f"\nYou played the game to win {count_the_play} time(s)")
                        print(f"You: {user_pick} | Comp: {computer_pick}\nYou WIN!")
                        # reset the counter
                        count_the_play = 0
                        print("\n")
                    else:
                        print(f"You: {user_pick} | Comp: {computer_pick}\nYou LOSE!")
                else:
                    print(f"You: {user_pick} | Comp: {computer_pick}\nDRAW!")
            else:
                print("\nYou quit the game.")
                quit()
        else:
            print("Please write one of these initial: r = rock, s = scissor, p = paper, q = quit\n")


def main():
    """
    Main body

    Variables:
    @game_list: list - r = rock, s = scissor, p = paper, q = quit
    :return:
    """
    game_list = ["r", "s", "p", "q"]
    start_game(game_list)


main()
