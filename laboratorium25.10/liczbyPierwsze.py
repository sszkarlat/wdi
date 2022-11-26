def is_prime(number):
    if number < 2:
        return False
    else:
        for divisor in range(2, int((number ** 0.5) + 1)):
            if number % divisor == 0:
                return False
        return True


"""Przykłady testowe:
268979
7
811709
925189
1890571
325826571
17592186044415"""

while True:
    request = int(input("Podaj liczbę, która chcesz sprawdzić: "))
    print(is_prime(request))
