"""
Wykorzystując algorytm Euklidesa napisz
funkcję wyznaczającą Największy Wspólny Dzielnik (NWD)
wprowadzonych przez użytkownika liczb.
Zwizualizuj w konsoli rekurencyjny sposób
działania programu.
"""


def Algorytm_Euklidesa(liczba1, liczba2):
    if liczba1 and liczba2 > 0:
        Liczba1.append(liczba1)
        Liczba2.append(liczba2)
        if liczba1 > liczba2:
            mnoznik = int(liczba1 / liczba2)
            reszta = liczba1 % liczba2
            print(f"{liczba1} = {liczba2} * {mnoznik} + {reszta}")
            Reszta.append(reszta)
            # print(Liczba1)
            # print(Liczba2)
            # print(Reszta)
            if reszta != 0:
                Algorytm_Euklidesa(liczba2, reszta)
            else:
                try:
                    print(f"NWD liczb {Liczba1[0], Liczba2[0]} to: {Reszta[-2]}")
                except IndexError:
                    if liczba1 > liczba2:
                        print(f"NWD liczb {liczba1, liczba2} to: {liczba2}")
                    elif liczba1 < liczba2:
                        print(f"NWD liczb {liczba1, liczba2} to: {liczba2}")
        elif liczba1 < liczba2:
            Algorytm_Euklidesa(liczba2, liczba1)
        else:
            print(f"NWD liczb {liczba1, liczba2} to: {liczba1}")
    else:
        print("Nieprawdiłowe dane wejściowe! Podaj liczby naturalne dodatnie!")


print("""Podaj dwie liczby naturalne dodatnie, w celu policzenia NWD, z wykorzystaniem Algorytmu Euklidesa.
Przyjęto, w tym programie, że liczby naturalne zaczynają się od 1!""")
while True:
    try:
        Reszta = []
        Liczba1 = []
        Liczba2 = []

        liczba1 = int(input("Podaj pierwszą liczbę: "))
        liczba2 = int(input("Podaj drugą liczbę: "))

        Algorytm_Euklidesa(liczba1, liczba2)
    except ValueError:
        print("Nieprawdiłowe dane wejściowe! Podaj liczby naturalne dodatnie!")
