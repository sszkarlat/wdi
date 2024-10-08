# zadanie2
name = "Szymon"
age = 19
print(name)
print(age)

# zadanie3
number1 = 2
number2 = -5
number3 = -5.55
word1 = "Ala"
word2 = "pilka"

# zadanie4
imie = "Szymon"
nazwisko = "Szkarłat"
wiek = 19
ulubiona_potrawa = "spaghetti"
ulubione_zwierze = "pies"
wynik_dzielenia = 5 / 7
print(imie)
print(nazwisko)
print(wiek)
print(ulubiona_potrawa)
print(ulubione_zwierze)
print(wynik_dzielenia.__round__(1))
print(wynik_dzielenia.__round__(3))
print(wynik_dzielenia.__round__(5))
print(wynik_dzielenia.__round__(10))
print(imie, nazwisko, wiek, ulubiona_potrawa, ulubione_zwierze, wynik_dzielenia.__round__(1),
      wynik_dzielenia.__round__(3), wynik_dzielenia.__round__(5), wynik_dzielenia.__round__(10))
print("Szymon")
print("Szkarłat")
print(19)
print("spaghetti")
print("pies")
print((5 / 7).__round__(1))
print((5 / 7).__round__(3))
print((5 / 7).__round__(5))
print((5 / 7).__round__(10))
print("Szymon", "Szkarłat", 19, "spaghetti", "pies", (5 / 7).__round__(1), (5 / 7).__round__(3), (5 / 7).__round__(5),
      (5 / 7).__round__(10))

# zadanie5
number = int(input("Podaj liczbę: "))
print("Wprowadzona przez Ciebie liczba to", number)


# zadanie6
def dodawanie(number1, number2):
    return number1 + number2


def odejmowanie(number1, number2):
    return number1 - number2


def mnozenie(number1, number2):
    return number1 * number2


def dzielenie(number1, number2):
    return number1 / number2


def potegowanie(number1, number2):
    return number1 ** 2, number2 ** 2


def pierwiastkowanie(number1, number2):
    return number1 ** 0.5, number2 ** 0.5


"""
Najpierw prosimy użytkownika o podanie liczb
Są one typu float, tak aby była możliwość zapisania liczb zmiennoprzecinkowych
Liczby zmiennoprzecinkowe to liczby nie całkowite (liczby całkowite - typ int)
"""

pierwszaLiczba = float(input("Podaj pierwszą liczbę: "))
drugaLiczba = float(input("Podaj drugą liczbę: "))
if pierwszaLiczba < 0 and drugaLiczba < 0:
    print("Obie liczby są ujemne")  # Jeśli użytkownik poda dwie liczby ujemne otrzyma komunikat
    exit()
elif pierwszaLiczba < 0:
    modulPierwszejLiczby = abs(pierwszaLiczba)  # Sposób uzyskania wartości bezwzględnej z pierwszej podanej liczby
    print("Wynik dodawania:", dodawanie(modulPierwszejLiczby, drugaLiczba))
    print("Wynik odejmowania:", odejmowanie(modulPierwszejLiczby, drugaLiczba))
    print("Wynik mnożenia:", mnozenie(modulPierwszejLiczby, drugaLiczba))
    if mnozenie(modulPierwszejLiczby, drugaLiczba) == 10:
        print("Yay!")  # Jeżeli wynik mnożenia jest równy 10 to użytkownik otrzyma komunikat "Yay!"
    print("Wynik dzielenia:", dzielenie(modulPierwszejLiczby, drugaLiczba))
    print("Kwadrat obu liczb:", potegowanie(modulPierwszejLiczby, drugaLiczba))
    print("Pierwiastek obu liczb:", pierwiastkowanie(modulPierwszejLiczby, drugaLiczba))
elif drugaLiczba < 0:
    modulDrugaLiczba = abs(drugaLiczba)  # Sposób uzyskania wartości bezwzględnej z drugiej podanej liczby
    print("Wynik dodawania:", dodawanie(pierwszaLiczba, modulDrugaLiczba))
    print("Wynik odejmowania:", odejmowanie(pierwszaLiczba, modulDrugaLiczba))
    print("Wynik mnożenia:", mnozenie(pierwszaLiczba, modulDrugaLiczba))
    if mnozenie(pierwszaLiczba, modulDrugaLiczba) == 10:
        print("Yay!")  # Jeżeli wynik mnożenia jest równy 10 to użytkownik otrzyma komunikat "Yay!"
    print("Wynik dzielenia:", dzielenie(pierwszaLiczba, modulDrugaLiczba))
    print("Kwadrat obu liczb:", potegowanie(pierwszaLiczba, modulDrugaLiczba))
    print("Pierwiastek obu liczb:", pierwiastkowanie(pierwszaLiczba, modulDrugaLiczba))
else:
    print("Wynik dodawania:", dodawanie(pierwszaLiczba, drugaLiczba))
    print("Wynik odejmowania:", odejmowanie(pierwszaLiczba, drugaLiczba))
    print("Wynik mnożenia:", mnozenie(pierwszaLiczba, drugaLiczba))
    if mnozenie(pierwszaLiczba, drugaLiczba) == 10:
        print("Yay!")  # Jeżeli wynik mnożenia jest równy 10 to użytkownik otrzyma komunikat "Yay!"
    print("Wynik dzielenia:", dzielenie(pierwszaLiczba, drugaLiczba))
    print("Kwadrat obu liczb:", potegowanie(pierwszaLiczba, drugaLiczba))
    print("Pierwiastek obu liczb:", pierwiastkowanie(pierwszaLiczba, drugaLiczba))

# zadanie7
poczatekZakresu = int(input("Podaj początek zakresu: "))
koniecZakresu = int(input("Podaj koniec zakresu: "))
if koniecZakresu - poczatekZakresu > 20:
    srednia = int((poczatekZakresu + koniecZakresu) / 2)
    print(srednia - 3)
    print(srednia - 2)
    print(srednia - 1)
    print(srednia + 1)
    print(srednia + 2)
    print(srednia + 3)
else:
    for liczba in range(poczatekZakresu, koniecZakresu + 1):
        print(liczba)


# zadanie8
def holiday_bush(number):
    for i in range(number):
        if i == 0:
            print(' ' * (number - i - 1), 'X' * (2 * i + 1))
        else:
            print(' ' * (number - i - 1), '*' * (2 * i + 1))
    print(' ' * (number - 1), 'U')


request = int(input("Podaj jakiej wysokości ma być choinka: "))  # Wprowadzona liczba ma być całkowita, nieujemna
holiday_bush(request)

# zadanie9
from enum import IntEnum

saldo = 1000
PIN = '1111'

Operacje_na_koncie = IntEnum('Operacje_na_koncie', 'Wpłata Wypłata Sprawdzenie_salda Zakończenie')

wybor = int(input("""Co chcesz wykonać na swoim koncie:
1. wpłacić 
2. wypłacić 
3. sprawdzić saldo
4. zakończyć użytkowanie
"""))

while True:
    if wybor == Operacje_na_koncie.Zakończenie:
        break
    PINuzytkownika = input("Podaj PIN: ")
    if PINuzytkownika != PIN:
        print("Niepoprawny PIN!")
    else:
        if wybor == Operacje_na_koncie.Wpłata:
            kwotaDoWplaty = int(input("Podaj kwote jaką chcesz wpłacić na swoje konto: "))
            saldo += kwotaDoWplaty
            print("Twój stan konta po tej transakcji to:", saldo)
        elif wybor == Operacje_na_koncie.Wypłata:
            kwotaWyplacona = int(input("Podaj kwotę jaką chcesz wypłacić: "))
            while kwotaWyplacona > saldo:
                print("Nie możesz wybrać tej kwoty, ponieważ Twój stan konta to:", saldo)
                kwotaWyplacona = int(input("Podaj kwotę jaką chcesz wypłacić: "))
            else:
                saldo -= kwotaWyplacona
                print("Twój stan konta po tej transakcji to:", saldo)
        elif wybor == Operacje_na_koncie.Sprawdzenie_salda:
            print("Twój stan konta to:", saldo)
        wybor = int(input("Co chcesz zrobić w kolejnym kroku?"))

# zadanie10
import random

print("""Kalkulator umożliwia następujące operacje na liczbach, aby je wykonać wybierz:
+ (dodawanie)
- (odejmowanie)
* (mnożenie)
/ (dzielenie)
^ (potęgowanie)
# (pierwiastkowanie)
x (losowanie liczby z zakresu)""")

request = "T"

while True:
    if request == "T":
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        wybor = input()  # Podanie znaku operacji na liczbach
        if wybor == "+":
            suma = liczba1 + liczba2
            print(suma)
        elif wybor == "-":
            roznica = liczba1 - liczba2
            print(roznica)
        elif wybor == "*":
            iloczyn = liczba1 * liczba2
            print(iloczyn)
        elif wybor == "/":
            if liczba2 != 0:
                iloraz = liczba1 / liczba2
                print(iloraz)
            else:
                print("Nie dziel przez zero!")
        elif wybor == "^":
            potegowanie = liczba1 ** liczba2
            print(potegowanie)
        elif wybor == "#":
            if liczba1 > 0 and liczba2 != 0:
                pierwiastkowanie = liczba1 ** (1 / liczba2)
                print(pierwiastkowanie)
            else:
                print("Nieprawidłowe dane wejściowe!")
        elif wybor == "x":
            if liczba1 > liczba2:
                losowanie = random.randint(int(liczba2), int(liczba1))
                print(losowanie)
            else:
                losowanie = random.randint(int(liczba1), int(liczba2))
                print(losowanie)
        else:
            print("Nieprawidłowy znak operacji")
        request = input("Czy chcesz wprowadzić nowe dane?")    
    elif request == "N":
        break
    else:
        exit()
