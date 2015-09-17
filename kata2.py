__author__ = 'drzewiec'


def countBits(n):
    return str(bin(n)[2:]).count("1")






print reduce(lambda a,b: a+b if (a==25) else a<b, [25,25,100,50])

def get_score(n):
    if n == 1:
        return 50
    return n*50 + get_score(n-1)



print get_score(10)

def get_score(n):
    return 50*reduce(lambda x,y: (x+y), xrange(n+1))
print get_score(4)


def squareSum(numbers):
    return sum(map(lambda x:x**2,numbers))

print squareSum([2,3,4])