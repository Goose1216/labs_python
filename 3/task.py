
class Quad:

    def __init__(self, h1, h2, h3, h4):
        self.coord = [h1, h2, h3, h4]

    def move(self, x, y):
        coord_changes = (x, y)
        for j in range(2):
            for i in range(len(self.coord)):
                self.coord[i][j] += coord_changes[j]

    def is_intersect(self, other):
        if any(self.point_in_figure(x, y, self.coord) for x, y in other.coord) \
                and any(not (self.point_in_figure(x, y, self.coord)) for x, y in other.coord):
            return True
        if any(other.point_in_figure(x, y, other.coord) for x, y in self.coord) \
                and (any(not (other.point_in_figure(x, y, other.coord)) for x, y in self.coord)):
            return True
        return False

    @staticmethod
    def point_in_figure(xp, yp, coord):
        if (coord[0][0]) <= xp <= (coord[1][0]) and (coord[0][1] <= yp <= coord[2][1]):
            return True
        return False

