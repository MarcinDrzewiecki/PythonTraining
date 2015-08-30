onet__author__ = 'drzewiec'


def fib(number):
    a,b=1,1
    for x in xrange(number):
        a,b = b, a+b
    return a

def l(list):
    return 0 if list==[] else 1+l(list[1:])

print l([1,2,3])

def mymap(function,list):
    if list == []:
        return []
    else:
        return [function(list[0])]+map(function,list[1:])

print(mymap(lambda n:n+2,[1,2,3]))

