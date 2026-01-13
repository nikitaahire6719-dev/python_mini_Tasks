class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print("\n" + self.text)
        for key, value in self.options.items():
            print(f"{key}. {value}")
        
    def is_correct(self, answer):
        return answer == self.correct_option
