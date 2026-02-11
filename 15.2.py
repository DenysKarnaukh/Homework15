class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        return Fraction(
            self.a * other.b + other.a * self.b,
            self.b * other.b


    def __sub__(self, other):
        return Fraction(
            self.a * other.b - other.a * self.b,
            self.b * other.b


    def __eq__(self, other):
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"