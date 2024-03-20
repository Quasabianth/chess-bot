import Figure
import Point


class Points:
    def __init__(self, points: list[list[Point.Point]], order: str):
        self.points = points
        self.order = order

    def get_white(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'w':
                        figures.append(cand.figure)
        return figures

    def get_black(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'b':
                        figures.append(cand.figure)
        return figures

    def get_figures(self) -> dict[str, list[Figure.Figure]]:
        return {'w': Points.get_white(self)} | {'b': Points.get_black(self)}

    def move(self):
        pass
