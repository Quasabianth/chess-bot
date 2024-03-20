class Figure:
    def __init__(self, color: str, pos_x: int, pos_y: int):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y


class Pawn(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Pawn"

    def move(self) -> list[tuple[int, int, int, int]]:
        moves = list()
        assert self.pos_y != 1
        assert self.pos_y != 8
        if self.color == 'w':
            moves += (self.pos_x, self.pos_y, self.pos_x, self.pos_y + 1)
            if self.pos_y == 2:
                moves += (self.pos_x, self.pos_y, self.pos_x, self.pos_y + 2)
            if 1 <= self.pos_x <= 7:
                moves += (self.pos_x, self.pos_y, self.pos_x + 1, self.pos_y + 1)
            if 2 <= self.pos_x <= 7:
                moves += (self.pos_x, self.pos_y, self.pos_x - 1, self.pos_y + 1)
        elif self.color == 'b':
            moves += (self.pos_x, self.pos_y, self.pos_x, self.pos_y - 1)
            if self.pos_y == 7:
                moves += (self.pos_x, self.pos_y, self.pos_x, self.pos_y - 2)
            if 1 <= self.pos_x <= 7:
                moves += (self.pos_x, self.pos_y, self.pos_x + 1, self.pos_y - 1)
            if 2 <= self.pos_x <= 7:
                moves += (self.pos_x, self.pos_y, self.pos_x - 1, self.pos_y - 1)
        return moves


class King(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "King"

    def move(self) -> list[tuple[int, int, int, int]]:
        moves = [(self.pos_x, self.pos_y, self.pos_x + dx, self.pos_y + dy)
                 for dx in [-1, 0, 1]
                 if 1 <= self.pos_x + dx <= 8
                 for dy in [-1, 0, 1]
                 if 1 <= self.pos_y + dy <= 8]
        return moves


class Knight(Figure):
    def __init__(self, color: str, pos_x: int, pos_y: int):
        Figure.__init__(self, color, pos_x, pos_y)
        self.identifier = "Knight"

    def move(self) -> list[tuple[int, int, int, int]]:
        xy: list[tuple[int, int]] = [(2, 1), [1, 2], (2, -1), (1, -2), (-2, -1), (-1, -2), (-1, 2), (-2, 1)]
        moves = [(self.pos_x, self.pos_y, self.pos_x + dx, self.pos_y + dy)
                 for dx, dy in xy
                 if 1 <= self.pos_x + dx <= 8
                 if 1 <= self.pos_y + dy <= 8]
        return moves


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
