__author__ = 'drzewko'


def poly(*args):
    def helper(x):
        return sum(a * x ** i for i, a in enumerate(reversed(args)))

    return helper


x2 = poly(3, 1, 0)

print x2(4)
