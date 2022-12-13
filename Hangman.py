# The Hangman Game Program

# --------- FUNCTION DEFINITIONS -------------------

def displayStatus(chances):
    # to show the hangman figure w/ the
    #   correct parts showing
    if (chances == 0):
        print("--------")
        print("|      |")
        print("|     \\O/")
        print("|      |")
        print("|     / \\")
        print("| ")
        print("==========")
    elif (chances == 1):
        print("--------")
        print("|      |")
        print("|     \\O/")
        print("|      |")
        print("|     / ")
        print("| ")
        print("==========")
    elif (chances == 2):
        print("--------")
        print("|      |")
        print("|     \\O/")
        print("|      |")
        print("|     ")
        print("| ")
        print("==========")
    elif (chances == 3):
        print("--------")
        print("|      |")
        print("|     \\O/")
        print("|      ")
        print("|      ")
        print("| ")
        print("==========")
    elif (chances == 4):
        print("--------")
        print("|      |")
        print("|     \\O")
        print("|      ")
        print("|      ")
        print("| ")
        print("==========")
    elif (chances == 5):
        print("--------")
        print("|      |")
        print("|      O")
        print("|      ")
        print("|      ")
        print("| ")
        print("==========")
    elif (chances == 6):
        print("--------")
        print("|      |")
        print("|       ")
        print("|      ")
        print("|      ")
        print("| ")
        print("==========")


# --------- MAIN PROGRAM ---------------------------
def main():
    answer = "fantastic"
    answerLen = len(answer)

    visible = [None] * answerLen
    for i in range(0, answerLen, 1):
        visible[i] = "-"

    life = 6
    numFound = 0

    while (True):
        print("-------", life, "chances left")
        displayStatus(life)

        print(visible)

        guess = input("Guess a letter:")

        found = False  # guess NO
        for i in range(0, answerLen, 1):
            if (answer[i] == guess):
                found = True
                numFound = numFound + 1
                visible[i] = guess

        # -Was the letter in the word??
        # YES: At least 1 yes
        # NO: ALL are no's
        if (not found):
            life = life - 1
            if (life == 0):
                print("You're dead")
                displayStatus(life)
                break
        else:
            # check for win condition
            if (len(answer) == numFound):
                print("You win!")
                break
