#Look at test_point.py first!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**.5
    def magnitude(self):
        return self.x + self.y
    def __repr__(self):
        return f"({self.x}, {self.y})"
