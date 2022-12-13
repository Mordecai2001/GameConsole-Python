# Game Console Program
# -------------------------IMPORTS----------------------------
import Hangman
import Connect4
import Sudoku
import Blackjack

# --------------------------MAIN------------------------------


def main():
    print("----------------------MENU----------------------")
    print("These are the game you can play on this console:")
    print("1.Hangman")
    print("2.Connect4")
    print("3.Sudoku")
    print("4.Blackjack")
    print("------------------------------------------------")
    choice = input("Enter your choice:")
    choice = int(choice)
    if choice == 1:
        print("--------------------HANGMAN---------------------")
        Hangman.main()
    elif choice == 2:
        print("-------------------CONNECT4---------------------")
        Connect4.main()
    elif choice == 3:
        print("--------------------SUDOKU----------------------")
        Sudoku.main()
    elif choice == 4:
        print("-------------------BLACKJACK--------------------")
        Blackjack.main()
    else:
        # choice validation
        while (choice != 1) or (choice != 2) or (choice != 3) or (choice != 4):
            choice = input("Enter your choice:")
        if choice == 1:
            Hangman.main()
        elif choice == 2:
            Connect4.main()
        elif choice == 3:
            Sudoku.main()
        elif choice == 4:
            Blackjack.main()


main()
