import Figure

# класс поля


class Point:
    def __init__(self, pos_x: int, pos_y: int, figure: Figure.Figure | None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.figure = figure
