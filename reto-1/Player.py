import Option

class Player:
    username = ""
    points = 0
    optionChoose = ""
    winner = False
    options = ""

    def __init__(self, username, points, optionChoose, winner, options):
        self.username = username
        self.points = points
        self.optionChoose = optionChoose
        self.winner = winner
        self.options = Option