class Score:
    def __init__(self):
        self.points = 0

    def increase(self):
        self.points += 1

    def show(self):
        print(f"\n final score: {self.points}")