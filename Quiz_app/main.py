from quiz import Quiz
from question import Question

def load_questions(quiz):
    q1 = Question("who is the president of india?", {"A": "Dropadi Murmu", "B": "Devendra Fadanvis", "c": "Eknath Shinde", "D": "Narendra Modi"}, "D" )

    q2 = Question("who is the father of Ai?", {"A": "John McCarthy", "B": "devin flaw", "C": "newton eisac", "D": "Bill Gates"}, "A")

    quiz.add_question(q1)
    quiz.add_question(q2)

def main():
    quiz = Quiz()
    load_questions(quiz)

    while True:
        print("\n==== Quiz Menu ====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                quiz.start()
            case "2":
                print("Exiting Quiz. Goodbye.")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()

    