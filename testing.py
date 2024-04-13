import Points
import Point
import Figure


points = [[Point.Point(x, y, None) for x in range(0, 8)] for y in range(0, 8)]

with open('input.txt') as input_file:
    inp = input_file.readline().rstrip()
    if inp == "last_move":
        inp = input_file.readline().rstrip()
        name, color, fro, to = map(str, inp.split())
        pos_x, pos_y = int(fro[0]), int(fro[1])
        position = Points.Points(points, 'w', (name, int(fro[0]), int(fro[0]), int(to[0]), int(to[0])))
        inp = input_file.readline().rstrip()
    while inp:
        name, color, pos = map(str, inp.split())
        pos_x, pos_y = int(pos[0]), int(pos[1])
        assert 0 <= pos_x <= 7
        assert 0 <= pos_y <= 7
        if name == "Pawn":
            points[pos_x][pos_y].figure = Figure.Pawn(color, pos_x, pos_y)
        elif name == "King":
            points[pos_x][pos_y].figure = Figure.King(color, pos_x, pos_y)
        elif name == "Knight":
            points[pos_x][pos_y].figure = Figure.Knight(color, pos_x, pos_y)
        elif name == "Bishop":
            points[pos_x][pos_y].figure = Figure.Bishop(color, pos_x, pos_y)
        elif name == "Rook":
            points[pos_x][pos_y].figure = Figure.Rook(color, pos_x, pos_y)
        elif name == "Queen":
            points[pos_x][pos_y].figure = Figure.Queen(color, pos_x, pos_y)
        else:
            raise NotImplemented
        inp = input_file.readline().rstrip()
moves = position.move_white()
print(moves)
