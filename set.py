class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


v1 = Vector(2, 3)
v2 = Vector(4, 3)
v3 = v1*v2
print(v3)