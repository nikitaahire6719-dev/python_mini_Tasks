from question import Question
from score import Score

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = Score()

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for question in self.questions:
            question.display()
            answer = input("Enter your answer: ").upper()

            if question.is_correct(answer):
                print("correct!")
                self.score.increase()
            else:
                print("Wrong!")

        self.score.show()