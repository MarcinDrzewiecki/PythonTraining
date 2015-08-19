__author__ = 'drzewiec'


interval= int(raw_input("Determine interval for Fizz Buzz game: "))


def is_dividable_by_3(number):
    if number%3==0:
        return True
    return False


def is_dividable_by_5(number):
    if number%5==0:
        return True
    return False

fizz_buzz = []

for x in range(1, interval):
    if is_dividable_by_3(x) and is_dividable_by_5(x):
        fizz_buzz.append("Fizz Buzz")
    elif is_dividable_by_3(x):
        fizz_buzz.append("Fizz")
    elif is_dividable_by_5(x):
        fizz_buzz.append("Buzz")
    else:
        fizz_buzz.append(x)

print(fizz_buzz)