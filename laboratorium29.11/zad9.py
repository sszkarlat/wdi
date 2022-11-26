"""
Wykorzystując funkcje, proszę napisać program,
który pobiera przykładowy tekst zapisany w pliku.
A następnie zwraca wartość określającą liczbę zdań w danym tekście.
"""
import re


def otwieranie_pliku(plik):
    with open(plik) as f:
        return f.read().split(" ")


def liczenie_zdan_w_tekscie():
    tekst = " ".join(otwieranie_pliku("przykladowy_tekst.txt"))
    liczbaZdan = len(re.findall(r'\.', tekst))
    return liczbaZdan


print(liczenie_zdan_w_tekscie())
