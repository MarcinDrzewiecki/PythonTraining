__author__ = 'drzewiec'


def even():
    return list(range(0, 101, 2))


def ifCheck(number):
    return number % 2 == 0 and number % 3 != 0


def my_filter(predicate, list):
    array = []
    for x in list:
        if predicate(x):
            array.append(x)
    return array


def function():
    return my_filter(lambda number: number % 2 == 0 and number % 3 != 0, xrange(101))


print function()


def mysquare(number):
    return number ** 2


def square():
    return map(lambda number: number ** 2, xrange(11))


def map2():
    return [number ** 2 for number in xrange(11)]


print map2()

print square()

print (lambda n: n + 3)(3)


def function2():
    return [number for number in xrange(101) if number % 2 == 0 and number % 3 != 0]


print function2()
# map(f,l) === [f(x) for x in l]
# filter(p.l)=== [x for x in l if p(x)]

print [x ** 2 for x in xrange(101) if x % 2 != 0]

# all(p,l)
# any(p.l)

print all([x % 2 == 0 for x in xrange(1, 11)])
print any([x % 2 == 0 for x in xrange(1, 11)])
print all([x%2==0 for x in xrange(1,11)])
print any([x%2==0 for x in xrange(1,11)])


def silnia(n):
    return reduce(lambda x,y: x*y,xrange(1,n+1))

print silnia(3)

def digits_to_int(digits):
    numbers=""
    for x in digits:
        numbers+=str(x)
    numbers = int(numbers)
    return numbers

print digits_to_int([2,3,4])

def digits_to_int2(digits):
    return reduce(lambda x,y:x*10+y,digits,0)

print digits_to_int2([2,3,4])


def wielomian(*args):
    def aux(x):
        return reduce(lambda y,z: y*x +z,args,0)
    return aux

print wielomian(1,0,0)(7)

print "-----"
def test(n):
    return reduce(lambda x,y:x*y, n)
print test([1])