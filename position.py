import math as m


class Position:
    def __init__(self, x, y, phi=0.0):
        self.x = x
        self.y = y
        self.phi = phi

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y, self.phi + other.phi)
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Position):
            result = Position(self.x - other.x, self.y - other.y, self.phi)
            result.rotate(-other.phi)
            return result
        raise NotImplementedError

    def __mul__(self, other):
        if type(other) == float:
            return Position(self.x * other, self.y * other, self.phi * other)
        raise NotImplementedError

    def __str__(self):
        return f"({self.x}, {self.y}, {self.phi})"

    def rotate(self, psi):
        self.x, self.y = self.x * m.cos(psi) + self.y * m.sin(psi), -self.x * m.sin(psi) + self.y * m.cos(psi)
        self.phi += psi
