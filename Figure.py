class Figure:
    def __init__(self, color: str, pos_x: int, pos_y: int):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y


class Pawn(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Pawn"


class King(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "King"


class Knight(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Knight"


class Bishop(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Bishop"


class Rook(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Rook"


class Queen(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Queen"
