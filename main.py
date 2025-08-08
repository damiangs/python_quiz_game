# welcome to user to the game


def main():
    print("Welcome to the Quiz me!")
    print("It is a multiple-choice game. You have to choose the correct answer!")

    while True:
        user_readiness = input("Are you ready to play? y/n: ")
        user_readiness.strip().lower()

        if user_readiness == "n":
            print("Come back whenever you want!")
            break

        elif user_readiness == "y":
            print("Let's get started!")
            game_start()
            break
        else:
            print("Enter a valid option(y/n)")


def game_start():
    score = 0
    score_message = f"Your score: {score}"
    print(score_message)

    questions = [
        {
            "question": "What is the capital of Japan?",
            "options": ["a) Puebla", "b) Tokio", "c) Angola", "d) Austria"],
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["a) Nilo", "b) Amazonas", "c) Yangtsé", "d) Misisipi"],
        },
        {
            "question": "In what year did World War II begin?",
            "options": ["a) 2025", "b) 1945", "c) 1994", "d) 1939"],
        },
        {
            "question": "Which is the largest planet in the solar system?",
            "options": ["a) Earth", "b) Jupiter", "c) Mars", "d) Coruscant"],
        },
        {
            "question": "Which continent is the largest in terms of surface area?",
            "options": ["a) Atlantis", "b) America", "c) Asia", "d) Africa"],
        },
    ]

    print(questions[1]["question"])


if __name__ == "__main__":
    main()
