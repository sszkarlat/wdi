"""
Liczby zespolone są reprezentowane przez krotkę (Re, Im).
Gdzie: Re – część rzeczywista liczby, Im -$ część urojona liczby.
Proszę napisać funkcje realizujące podstawowe operacje
na liczbach zespolonych, m.in. dodawanie, odejmowanie, mnożenie,
dzielenie, potęgowanie, wypisywanie i wczytywanie.
Używając tych funkcji proszę napisać funkcję rozwiązującą
równanie kwadratowe o współczynnikach zespolonych.
"""


def wczytywanie(liczbaZespolona1):
    LiczbaZespolona1 = tuple((liczbaZespolona1.real, liczbaZespolona1.imag))
    return LiczbaZespolona1


def wypisywanie(LiczbaZespolona1):
    LiczbaZespolona1 = complex(LiczbaZespolona1[0], LiczbaZespolona1[1])
    return LiczbaZespolona1


def dodawanie(LiczbaZespolona1, LiczbaZespolona2):
    wynik = complex(LiczbaZespolona1[0], LiczbaZespolona1[1]) + complex(LiczbaZespolona2[0], LiczbaZespolona2[1])
    return wczytywanie(wynik)


def odejmowanie(LiczbaZespolona1, LiczbaZespolona2):
    wynik = complex(LiczbaZespolona1[0], LiczbaZespolona1[1]) - complex(LiczbaZespolona2[0], LiczbaZespolona2[1])
    return wczytywanie(wynik)


def mnozenie(LiczbaZespolona1, LiczbaZespolona2):
    wynik = complex(LiczbaZespolona1[0], LiczbaZespolona1[1]) * complex(LiczbaZespolona2[0], LiczbaZespolona2[1])
    return wczytywanie(wynik)


def dzielenie(LiczbaZespolona1, LiczbaZespolona2):
    wynik = complex(LiczbaZespolona1[0], LiczbaZespolona1[1]) / complex(LiczbaZespolona2[0], LiczbaZespolona2[1])
    return wczytywanie(wynik)


def potegowanie(LiczbaZespolona1, n):
    wynik = pow(complex(LiczbaZespolona1[0], LiczbaZespolona1[1]), n)
    return wczytywanie(wynik)


def rownanie_kwadratowe(a, b, c):
    delta = odejmowanie(potegowanie(b, 2),
                        mnozenie(wczytywanie(complex("4")), mnozenie(a, c)))
    print(f"Delta tego rówania kwadratowego: {wypisywanie(delta)}")

    if delta != 0:
        x1 = dzielenie(odejmowanie(mnozenie(wczytywanie(complex("-1")), b), potegowanie(delta, 0.5)),
                       mnozenie(wczytywanie(complex("2")), a))
        x2 = dzielenie(dodawanie(mnozenie(wczytywanie(complex("-1")), b), potegowanie(delta, 0.5)),
                       mnozenie(wczytywanie(complex("2")), a))
        print(
            f"Miejsca zerowe rówania kwadratowego: {wypisywanie(a)}x^2 + {wypisywanie(b)}x + {wypisywanie(c)} to: {wypisywanie(x1)} oraz {wypisywanie(x2)}")
    else:
        x0 = dzielenie(mnozenie(wczytywanie(complex(-1)), b), mnozenie(wczytywanie(complex("2")), a))
        print(
            f"Miejsce zerowe rówania kwadratowego: {wypisywanie(a)}x^2 + {wypisywanie(b)}x + {wypisywanie(c)} to: {wypisywanie(x0)}")


liczbyZespolone = []
while True:
    try:
        a = wczytywanie(complex(input("Podaj pierwszą liczbę: ")))
        b = wczytywanie(complex(input("Podaj drugą liczbę: ")))
        c = wczytywanie(complex(input("Podaj trzecia liczbę: ")))

        print(f"a: {wypisywanie(a)}")
        print(f"b: {wypisywanie(b)}")
        print(f"c: {wypisywanie(c)}")

        rownanie_kwadratowe(a, b, c)
    except ValueError:
        print("Nieprawidłowe dane wejściowe!")
