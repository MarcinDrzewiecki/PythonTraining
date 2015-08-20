__author__ = 'drzewiec'

interval = int(raw_input("Prime number scanner will detect and add to each other all prime numbers from 2 to: "))
how_many_prime_numbers = int(raw_input("How many prime numbers should i add to each other? :  "))

prime_numbers = []
count=0


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for x in range(2,1000000):
    if is_prime(x):
        prime_numbers.append(x)
        count += 1
        if count == how_many_prime_numbers:
            break

for x in range(2, interval + 1):
   if is_prime(x):
      prime_numbers.append(x)

print(prime_numbers)
print(sum(prime_numbers))


