__author__ = 'drzewko'

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def create_number(number):
    num_to_str = str(number)
    string_number=""
    for x in num_to_str:
        if is_int(x):
            string_number=string_number+str(x)
    return string_number

def sum(number):
    sum = 0
    for x in number:
        sum = sum+int(x)
    return sum

def find_number(number):
    for x in range(3):
        value = x+number
        if value%3==0:
            return x

print (find_number(sum(create_number("1?5"))))
