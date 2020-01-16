class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.base()

    def base(self):
        for i in list(range(2, max(self.numerator, self.denominator)))[::-1]:
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator = self.numerator // i
                self.denominator = self.denominator // i

    def add(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def subtract(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def show(self):
        print(f"{self.numerator}/{self.denominator}")


if __name__ == "__main__":
    x = Fraction(3, 4)
    x.add(Fraction(5, 8)).show()
    x.subtract(Fraction(5, 8)).show()
    x.multiply(Fraction(4, 3)).show()
    x.divide(Fraction(5, 8)).show()
