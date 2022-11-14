"""
Zadanie 5.
Proszę napisać program, który wypełnia listę tysiącem losowych liczb z dowolnego
wskazanego zakresu przez użytkownika i sprawdzający, czy w tym zakresie jest liczba
zawierająca wyłącznie cyfry nieparzyste. W celu generowania liczb można wykorzystać funkcję random.randint().
Należy wypisać wszystkie takie znalezione liczby w kolejności malejącej i obsłużyć wyjątek,
w którym użytkownik podaje na wejściu liczby, które są równe.
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


# Jest to rozwiązanie szybsze od tego poniżej. Ponieważ tutaj tylko sprawdzamy czy element jest w
# listaLiczbNieparzystych
def nieparzyste_czynniki_liczby(function, *arg):
    listaLiczbNieparzystych = [1, 3, 5, 7, 9]
    nieparzysteCzynniki = []
    for element in function(*arg):
        if element in listaLiczbNieparzystych:
            nieparzysteCzynniki.append("True")
    if len(nieparzysteCzynniki) == len(function(*arg)):
        return True


# Jest to rozwiązanie wolniejsze 
# def nieparzyste_czynniki_liczby(function, *arg):
#     nieparzysteCzynniki = []
#     for element in function(*arg):
#         if element % 2 != 0:
#             nieparzysteCzynniki.append("True")
#     if len(nieparzysteCzynniki) == len(function(*arg)):
#         return True


def losowanie_liczb(poczatekZakresu, koniecZakresu):
    wylosowaneLiczby = []
    for liczba in range(0, 1000):
        if poczatekZakresu < koniecZakresu:
            wylosowaneLiczby.append(random.randint(poczatekZakresu, koniecZakresu))
        elif poczatekZakresu > koniecZakresu:
            wylosowaneLiczby.append(random.randint(koniecZakresu, poczatekZakresu))
        else:
            while poczatekZakresu == koniecZakresu:
                print("Początek i koniec zakresu to ta sama liczba, a więc nie jest to dopowiedni zakres do losowania!")
                poczatekZakresu = int(input("Podaj początek zakresu: "))
                koniecZakresu = int(input("Podaj koniec zakresu: "))
    return wylosowaneLiczby


def liczby_z_nieparzystymi_cyframi():
    liczbyNieparzyste = []
    for liczba in losowanie_liczb(poczatekZakresu, koniecZakresu):
        if nieparzyste_czynniki_liczby(cyfry_liczby, liczba):
            liczbyNieparzyste.append(liczba)
    return sorted(liczbyNieparzyste, reverse=True)


while True:
    poczatekZakresu = int(input("Podaj początek zakresu: "))
    koniecZakresu = int(input("Podaj koniec zakresu: "))

    print(liczby_z_nieparzystymi_cyframi())
