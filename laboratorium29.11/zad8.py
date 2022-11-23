"""
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n
wypełnioną liczbami naturalnymi.
Dla danej tablicy należy napisać funkcję, która będzie odpowiadała na pytanie,
czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z
cyfr będących liczbami pierwszymi.
Wymiar tablicy powinien być definiowany przez użytkownika.
"""
import random


def cyfry_liczby(n):
    cyfryLiczby = []
    if n < 0:
        n = -n
        dl_liczby = len(str(n))
    else:
        dl_liczby = len(str(n))
    for pozycja in range(1, dl_liczby + 1):
        cyfra = n % 10
        n = n // 10
        cyfryLiczby.append(cyfra)

    return cyfryLiczby


def pierwsze_czynniki_liczby(funkcja, *arg):
    listaCyfrPierwszych = [2, 3, 5, 7]
    pierwszeCzynniki = []
    for element in funkcja(*arg):
        if element in listaCyfrPierwszych:
            pierwszeCzynniki.append("True")
    if len(pierwszeCzynniki) == len(funkcja(*arg)):
        return True


def generowanie_tablicy_dwuwymiarowej(n):
    tablicaDwuwymiarowa = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
    return tablicaDwuwymiarowa


def czy_kazdy_wiersz_zawiera_liczbe_z_wylacznie_cyframi_pierwszymi(tablicaDwuwymiarowa):
    licznik = 0
    for wiersz in tablicaDwuwymiarowa:
        for liczba in wiersz:
            if pierwsze_czynniki_liczby(cyfry_liczby, liczba):
                licznik += 1
                print(f"pierwsza napotkana liczba w wierszu {tablicaDwuwymiarowa.index(wiersz)}: {liczba}")
                break
        if licznik == tablicaDwuwymiarowa.index(wiersz):
            break
    if licznik == len(tablicaDwuwymiarowa):
        return True, licznik
    else:
        return False, licznik


while True:
    tablicaDwuwymiarowa = generowanie_tablicy_dwuwymiarowej(int(input("Podaj wielkość tablicy: ")))
    print(tablicaDwuwymiarowa)

    print(f"""Informacje o tablicy dwuwymiarowej:
    1. Czy istnieje, w każdym wierszu tablicy, liczba, której cyfry są pierwsze.
    2. Ilość wierszy (liczone do momentu wystąpienia wiersza, w którym nie ma liczby, składającej się z samych cyfr pierwszych).
    {czy_kazdy_wiersz_zawiera_liczbe_z_wylacznie_cyframi_pierwszymi(tablicaDwuwymiarowa)}""")
