# welcome to user to the game


def main():
    print("Welcome to the Quiz me!")
    print("It is a multiple-choice game. You have to choose the correct answer!")

    while True:
        user_readiness = input("Are you ready to play? y/n: ").strip().lower()

        if user_readiness == "n":
            print("Come back whenever you want!")
            break

        elif user_readiness == "y":
            print("Let's get started!")
            game_start()

            # ask the user to play again
            play_again = input("Do you want to play again? y/n: ").strip().lower()
            if play_again == "n":
                print("Thanks for playing! Goodbye!")
                break

            elif play_again != "y":
                print("Invalid input. Exiting the game")
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
            "options": ["a) Puebla", "b) Tokyo", "c) Angola", "d) Austria"],
            "answer": "b",
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["a) Nilo", "b) Amazonas", "c) Yangtsé", "d) Misisipi"],
            "answer": "a",
        },
        {
            "question": "In what year did World War II begin?",
            "options": ["a) 2025", "b) 1945", "c) 1994", "d) 1939"],
            "answer": "d",
        },
        {
            "question": "Which is the largest planet in the solar system?",
            "options": ["a) Earth", "b) Jupiter", "c) Mars", "d) Coruscant"],
            "answer": "b",
        },
        {
            "question": "Which continent is the largest in terms of surface area?",
            "options": ["a) Atlantis", "b) America", "c) Asia", "d) Africa"],
            "answer": "c",
        },
        {
            "question": "Who wrote 'Don Quixote de la Mancha'?",
            "options": ["a) Cervantes", "b) Cortazar", "c) Fuentes", "d) Verne"],
            "answer": "a",
        },
        {
            "question": "What sport is played at the Wimbledon tournament?",
            "options": ["a) Swimming", "b) Basketball", "c) Soccer", "d) Tenis"],
            "answer": "d",
        },
        {
            "question": "Who painted the 'Mona Lisa'?",
            "options": ["a) Picasso", "b) DaVinci", "c) DiCaprio", "d) Dali"],
            "answer": "b",
        },
        {
            "question": "In what year was America discovered?",
            "options": ["a) 1492", "b) 1920", "c) 1945", "d) 1536"],
            "answer": "a",
        },
        {
            "question": "Who was the first man to walk on the moon?",
            "options": ["a) Trump", "b) Armstrong", "c) Musk", "d) Obrador"],
            "answer": "b",
        },
    ]

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer: ").strip().lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'")

    print(f"\nGame over! Your final score: {score}/{len(questions)}")


if __name__ == "__main__":
    main()
