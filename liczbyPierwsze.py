def is_prime(number):
    if number < 2:
        return False
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True


request = int(input("Podaj liczbę, która chcesz sprawdzić: "))
print(is_prime(request))
