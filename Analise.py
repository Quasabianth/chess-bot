import Figure
import Point
import Points
import math
import json


class Analise:
    def __init__(self, points: Points):
        self.points = points

    def count_pieces(self) -> int:
        with open("metrix.json", "r") as metrix:
            file_metrix = metrix.read()
        figures: dict[str: int] = json.loads(file_metrix)
        count = 0
        for figure in self.points.get_white():
            count += figures[figure]
        for figure in self.points.get_black():
            count -= figures[figure]
        return count
