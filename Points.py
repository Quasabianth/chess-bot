import Figure
import Point

# класс поля (клеток)


class Points:
    def __init__(self, points: list[list[Point.Point]], order: str, last_move: tuple[str, int, int, int, int] | None,
                 white_long_castling: bool = True, white_short_castling: bool = True, black_long_castling: bool = True,
                 black_short_castling: bool = True):
        self.points = points
        self.order = order
        self.last_move = last_move
        self.white_long_castling = white_long_castling
        self.white_short_castling = white_short_castling
        self.black_long_castling = black_long_castling
        self.black_short_castling = black_short_castling

    # получить все белые фигуры

    def get_white(self) -> list[Figure.Figure]:
        figures = []
        for i in range(0, 8):
            for j in range(0, 8):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'w':
                        figures.append(cand.figure)
        return figures

     # получить все черные фигуры

    def get_black(self) -> list[Figure.Figure]:
        figures = []
        for i in range(0, 8):
            for j in range(0, 8):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'b':
                        figures.append(cand.figure)
        return figures

    # получить все фигуры

    def get_figures(self) -> list[Figure.Figure]:
        return self.get_white() + self.get_black()

    # получить белого короля

    def get_white_king(self) -> list[Figure.Figure]:
        return [figure for figure in self.get_white()
                if type(figure) is Figure.King]

    # получить черного короля

    def get_black_king(self) -> list[Figure.Figure]:
        return [figure for figure in self.get_black()
                if type(figure) is Figure.King]

    # возможные ходы пешки

    def possible_move_pawn(self, pawn: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        if pawn.color == 'w':
            if self.points[pawn.pos_x][pawn.pos_y + 1].figure is None:
                moves.append(
                    (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y + 1)
                )
                if pawn.pos_y == 1:
                    if self.points[pawn.pos_x][pawn.pos_y + 2].figure is None:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y + 2)
                        )
            if 0 <= pawn.pos_x <= 6:
                if self.points[pawn.pos_x + 1][pawn.pos_y + 1].figure is not None:
                    if self.points[pawn.pos_x + 1][pawn.pos_y + 1].figure.color != pawn.color:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x + 1, pawn.pos_y + 1)
                        )
            if 1 <= pawn.pos_x <= 7:
                if self.points[pawn.pos_x - 1][pawn.pos_y + 1].figure is not None:
                    if self.points[pawn.pos_x - 1][pawn.pos_y + 1].figure.color != pawn.color:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x - 1, pawn.pos_y + 1)
                        )
        elif pawn.color == 'b':
            if self.points[pawn.pos_x][pawn.pos_y - 1].figure is None:
                moves.append(
                    (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y - 1)
                )
                if pawn.pos_y == 6:
                    if self.points[pawn.pos_x][pawn.pos_y - 2].figure is None:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y - 2)
                        )
            if 0 <= pawn.pos_x <= 7:
                if self.points[pawn.pos_x + 1][pawn.pos_y - 1].figure is not None:
                    if self.points[pawn.pos_x + 1][pawn.pos_y - 1].figure.color != pawn.color:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x + 1, pawn.pos_y - 1)
                        )
            if 1 <= pawn.pos_x <= 7:
                if self.points[pawn.pos_x - 1][pawn.pos_y - 1].figure is not None:
                    if self.points[pawn.pos_x - 1][pawn.pos_y - 1].figure.color != pawn.color:
                        moves.append(
                            (pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x - 1, pawn.pos_y - 1)
                        )
        else:
            raise NotImplemented
        return set(moves)

    # возможные ходы короля

    def possible_move_king(self, king: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (0 <= king.pos_x + i <= 7) or not (0 <= king.pos_y + j <= 7):
                    continue
                if i == 0 and j == 0:
                    continue
                if self.points[king.pos_x + i][king.pos_y + j].figure is not None:
                    if self.points[king.pos_x + i][king.pos_y + j].figure.color != king.color:
                        moves.append(
                            (king.identifier, king.pos_x, king.pos_y, king.pos_x + i, king.pos_y + j)
                        )
                else:
                    moves.append(
                        (king.identifier, king.pos_x, king.pos_y, king.pos_x + i, king.pos_y + j)
                    )
        return set(moves)

    # возможные ходы коня

    def possible_move_knight(self, knight: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        xy: list[tuple[int, int]] = [(2, 1), [1, 2], (2, -1), (1, -2), (-2, -1), (-1, -2), (-1, 2), (-2, 1)]
        for i, j in xy:
            if not (0 <= knight.pos_x + i <= 7) or not (0 <= knight.pos_y + j <= 7):
                continue
            if self.points[knight.pos_x + i][knight.pos_y + j].figure is not None:
                if self.points[knight.pos_x + i][knight.pos_y + j].figure.color != knight.color:
                    moves.append(
                        (knight.identifier, knight.pos_x, knight.pos_y, knight.pos_x + i, knight.pos_y + j)
                    )
            else:
                moves.append(
                    (knight.identifier, knight.pos_x, knight.pos_y, knight.pos_x + i, knight.pos_y + j)
                )
        return set(moves)

    # возможные ходы слона

    def possible_move_bishop(self, bishop: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        xy: list[tuple[int, int]] = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        for i, j in xy:
            g = 1
            while 0 <= bishop.pos_x + i * g <= 7 and 0 <= bishop.pos_y + j * g <= 7:
                if self.points[bishop.pos_x + i * g][bishop.pos_y + i * g].figure is not None:
                    if self.points[bishop.pos_x + i * g][bishop.pos_y + i * g].figure.color == bishop.color:
                        moves.append(
                            (bishop.identifier, bishop.pos_x, bishop.pos_y, bishop.pos_x + i * g, bishop.pos_y + i * g)
                        )
                    break
                moves.append(
                    (bishop.identifier, bishop.pos_x, bishop.pos_y, bishop.pos_x + i * g, bishop.pos_y + i * g)
                )
                g += 1
        return set(moves)

    # возможные ходы ладьи

    def possible_move_rook(self, rook: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        xy: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in xy:
            g = 1
            while 0 <= rook.pos_x + i * g <= 7 and 0 <= rook.pos_y + j * g <= 7:
                if self.points[rook.pos_x + i * g][rook.pos_y + i * g].figure is not None:
                    if self.points[rook.pos_x + i * g][rook.pos_y + i * g].figure.color == rook.color:
                        moves.append(
                            (rook.identifier, rook.pos_x, rook.pos_y, rook.pos_x + i * g, rook.pos_y + i * g)
                        )
                    break
                moves.append(
                    (rook.identifier, rook.pos_x, rook.pos_y, rook.pos_x + i * g, rook.pos_y + i * g)
                )
                g += 1
        return set(moves)

    # возможные ходы ферзя

    def possible_move_queen(self, queen: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        xy: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i, j in xy:
            g = 1
            while 0 <= queen.pos_x + i * g <= 7 and 0 <= queen.pos_y + j * g <= 7:
                if self.points[queen.pos_x + i * g][queen.pos_y + i * g].figure is not None:
                    if self.points[queen.pos_x + i * g][queen.pos_y + i * g].figure.color == queen.color:
                        moves.append(
                            (queen.identifier, queen.pos_x, queen.pos_y, queen.pos_x + i * g, queen.pos_y + i * g)
                        )
                    break
                moves.append(
                    (queen.identifier, queen.pos_x, queen.pos_y, queen.pos_x + i * g, queen.pos_y + i * g)
                )
                g += 1
        return set(moves)

    # проверка на шах

    def is_check(self, order: str) -> bool:
        flag = False
        if order == 'w':
            king = self.get_white_king()[0]
            pos_x, pos_y = king.pos_x, king.pos_y
            for cand in self.move_black():
                x, y = cand[3], cand[4]
                if pos_x == x and pos_y == y:
                    flag = True
                    break
        elif order == 'b':
            king = self.get_black_king()[0]
            pos_x, pos_y = king.pos_x, king.pos_y
            for cand in self.move_white():
                x, y = cand[3], cand[4]
                if pos_x == x and pos_y == y:
                    flag = True
                    break
        else:
            raise NotImplemented
        return flag

    # возможные ходы белых без учета шахов
    def move_white(self) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for figure in self.get_white():
            match type(figure):
                case Figure.Pawn:
                    moves += self.possible_move_pawn(figure)
                case Figure.King:
                    moves += self.possible_move_king(figure)
                case Figure.Knight:
                    moves += self.possible_move_knight(figure)
                case Figure.Bishop:
                    moves += self.possible_move_bishop(figure)
                case Figure.Rook:
                    moves += self.possible_move_rook(figure)
                case Figure.Queen:
                    moves += self.possible_move_queen(figure)
                case _:
                    raise NotImplemented
        return set(moves)

    # возможные ходы черных без учета шахов

    def move_black(self) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for figure in self.get_black():
            match type(figure):
                case Figure.Pawn:
                    moves += self.possible_move_pawn(figure)
                case Figure.King:
                    moves += self.possible_move_king(figure)
                case Figure.Knight:
                    moves += self.possible_move_knight(figure)
                case Figure.Bishop:
                    moves += self.possible_move_bishop(figure)
                case Figure.Rook:
                    moves += self.possible_move_rook(figure)
                case Figure.Queen:
                    moves += self.possible_move_queen(figure)
                case _:
                    raise NotImplemented
        return set(moves)

    # функция, которая передвигает фигуры

    def move_piece(self, move: tuple[str, int, int, int, int], color) -> None:
        identifier, from_x, from_y, to_x, to_y = move
        if identifier == "Pawn":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.Pawn(color, to_x, to_y)
        elif identifier == "King":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.King(color, to_x, to_y)
        elif identifier == "Knight":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.Knight(color, to_x, to_y)
        elif identifier == "Bishop":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.Bishop(color, to_x, to_y)
        elif identifier == "Rook":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.Rook(color, to_x, to_y)
        elif identifier == "Queen":
            self.points[from_x][from_y].figure = None
            self.points[to_x][to_y].figure = Figure.Queen(color, to_x, to_y)
        else:
            raise NotImplemented

    # функия возможных ходов с учетом шахов

    def possible_moves_white(self) -> set[tuple[str, int, int, int, int]]:
        possible_moves = list()
        for cand in self.move_white():
            _after_move = Points(self.points.copy(), 'w')
            _after_move.move_piece(cand, 'w')
            if not _after_move.is_check('w'):
                possible_moves.append(cand)
        return set(possible_moves)

    # функия возможных ходов с учетом шахов

    def possible_moves_black(self) -> set[tuple[str, int, int, int, int]]:
        possible_moves = list()
        for cand in self.move_black():
            _after_move = Points(self.points.copy(), 'b')
            _after_move.move_piece(cand, 'b')
            if not _after_move.is_check('b'):
                possible_moves.append(cand)
        return set(possible_moves)

    # функция удаления фигуры
    
    def delete(self, x, y) -> None:
        self.points[x][y].figure = None
