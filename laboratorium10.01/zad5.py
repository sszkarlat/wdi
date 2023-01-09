import math
import unittest
import pytest


class ComplexNumber:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def print_number(self):
        return complex(self.Re, self.Im)

    def __add__(self, other):
        return ComplexNumber(self.Re + other.Re, self.Im + other.Im)

    def __sub__(self, other):
        return ComplexNumber(self.Re - other.Re, self.Im - other.Im)

    def __mul__(self, other):
        realPart = self.Re * other.Re - self.Im * other.Im
        imagPart = self.Re * other.Im + self.Im * other.Re
        return ComplexNumber(realPart, imagPart)

    def __truediv__(self, other):
        realPart = (self.Re * other.Re + self.Im * other.Im) / (other.Re ** 2 + other.Im ** 2)
        imagPart = (self.Im * other.Re - self.Re * other.Im) / (other.Re ** 2 + other.Im ** 2)
        return ComplexNumber(realPart, imagPart)

    def __pow__(self, n):
        # Oblicz moduł i kąt fi liczby zespolonej
        magnitude = math.sqrt(self.Re ** 2 + self.Im ** 2)
        phase = math.atan2(self.Im, self.Re)

        # Podnosimy moduł do potęgi n, a kąt fi mnożymy przez n
        new_magnitude = magnitude ** n
        new_phase = phase * n

        # Obliczamy nową część rzeczywistą i urojoną liczby zespolonej
        newRealPart = new_magnitude * math.cos(new_phase)  # mnożymy moduł przez cosinus kąta fi
        newImagPart = new_magnitude * math.sin(new_phase)  # mnożymy moduł przez sinus kąta fi

        # Na końcu zwracamy nowo powstałą liczbę zespoloną
        return ComplexNumber(newRealPart.__round__(5), newImagPart.__round__(5))


def quadratic_zeros(a, b, c):
    delta = ComplexNumber.__sub__(
        ComplexNumber.__pow__(b, 2), ComplexNumber.__mul__(
            ComplexNumber.__mul__(a, ComplexNumber(4, 0)), c)
    )
    # print(delta.print_number())

    # Jeśli delta jest równa zero, to istnieje tylko jedno miejsce zerowe.
    if delta.print_number() == complex(0 + 0j):
        x1 = ComplexNumber.__truediv__(ComplexNumber.__mul__(b, ComplexNumber(-1, 0)),
                                       ComplexNumber.__mul__(a, ComplexNumber(2, 0)))
        return x1

    # Jeśli delta jest różna od zera, to istnieją dwa miejsca zerowe.
    elif delta != 0:
        x1 = ComplexNumber.__truediv__(
            ComplexNumber.__add__(ComplexNumber.__mul__(
                b, ComplexNumber(-1, 0)), ComplexNumber.__pow__(delta, 0.5)),
            ComplexNumber.__mul__(a, ComplexNumber(2, 0)))
        x2 = ComplexNumber.__truediv__(
            ComplexNumber.__sub__(ComplexNumber.__mul__(
                b, ComplexNumber(-1, 0)), ComplexNumber.__pow__(delta, 0.5)),
            ComplexNumber.__mul__(a, ComplexNumber(2, 0)))
        return x1, x2


def test_quadratic_zeros1():
    # Test, w którym mamy dwa miejsa zerowe, tylko rzeczywiste liczby
    a = ComplexNumber(1, 0)
    b = ComplexNumber(5, 0)
    c = ComplexNumber(6, 0)

    x1, x2 = quadratic_zeros(a, b, c)
    assert x1.print_number() == complex(-2 + 0j)
    assert x2.print_number() == complex(-3 + 0j)


def test_quadratic_zeros2():
    # Test, w którym mamy dwa miejsa zerowe, tylko liczby zespolone
    a = ComplexNumber(1, 0)
    b = ComplexNumber(2, 0)
    c = ComplexNumber(2, 0)
    x1, x2 = quadratic_zeros(a, b, c)
    assert x1.print_number() == complex(-1 + 1j)
    assert x2.print_number() == complex(-1 - 1j)


def test_quadratic_zeros3():
    # Test dla delty równej 0, kiedy mamy tylko jedno miejsce zerowe
    a = ComplexNumber(1, 0)
    b = ComplexNumber(2, 0)
    c = ComplexNumber(1, 0)
    x1 = quadratic_zeros(a, b, c)
    assert x1.print_number() == complex(-1 + 0j)


class TestQuadraticZeros(unittest.TestCase):
    # Test dla delty równej 0, kiedy mamy tylko jedno miejsce zerowe
    def test_quadratic_zeros1(self):
        a = ComplexNumber(1, 0)
        b = ComplexNumber(2, 0)
        c = ComplexNumber(1, 0)
        self.assertEqual(quadratic_zeros(a, b, c).print_number(), complex(-1 + 0j))

    # Test dla delty różnej od zera, kiedy miejscami zerowymi są liczby rzeczywiste
    def test_quadratic_zeros2(self):
        a = ComplexNumber(1, 0)
        b = ComplexNumber(5, 0)
        c = ComplexNumber(6, 0)
        self.assertEqual(quadratic_zeros(a, b, c)[0].print_number(), complex(-2 + 0j))
        self.assertEqual(quadratic_zeros(a, b, c)[1].print_number(), complex(-3 + 0j))

    # Test dla delty różnej od zera, kiedy miejscami zerowymi są liczby zespolone
    def test_quadratic_zeros3(self):
        a = ComplexNumber(1, 0)
        b = ComplexNumber(2, 0)
        c = ComplexNumber(2, 0)
        self.assertEqual(quadratic_zeros(a, b, c)[0].print_number(), complex(-1 + 1j))
        self.assertEqual(quadratic_zeros(a, b, c)[1].print_number(), complex(-1 - 1j))
