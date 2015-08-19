__author__ = 'drzewiec'


interval = int(raw_input("Prime number scanner will detect and add to each other all prime numbers from 2 to: "))

prime_numbers = []


def prime_number(number):
    for x in range(2, number):
        if number % x == 0:
            break
    else:
        return number

for x in range(2, interval+1):
    prime_numbers.append(prime_number(x))

prime_numbers=filter(None,prime_numbers)
print(prime_numbers)
print(sum(prime_numbers))