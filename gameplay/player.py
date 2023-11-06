class Player:
    def __init__(self, score):
        self.score = score

    def add(self, val):
        self.score += val

    def reset_score(self):
        self.score = 0

    def get_score(self):
        return self.score
