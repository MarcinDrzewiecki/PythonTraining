onet__author__ = 'drzewiec'


def fib(n):
    if n == 0:
        return 0
    elif n <=3:
        return 1
    else:
        a, b = 1, 0
        for x in xrange(n):
            a, b = b, a + b
        return a

print fib(4)

def l(list):
    return 0 if list == [] else 1 + l(list[1:])


print l([1, 2, 3])


def mymap(function, list):
    if list == []:
        return []
    else:
        return [function(list[0])] + map(function, list[1:])


print(mymap(lambda n: n + 2, [1, 2, 3]))
