# welcome to user to the game


def main():
    print("Welcome to the Quiz me!")
    print("It is a multiple-choice game. You hace to choose the correct answer!")
    user_readiness = input("Are you ready to play? y/n: ")
    if user_readiness.strip().lower() == "y":
        print("Let's get started!")
    elif user_readiness.strip().lower() == "n":
        print("Come back whenever you want!")
    else:
        print("Enter a valid option")


if __name__ == "__main__":
    main()


