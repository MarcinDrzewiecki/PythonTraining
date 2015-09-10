from mimetypes import init

__author__ = 'drzewiec'
from operator import add,mul,sub

class Number(object):
    def __init__(self,number):
        self.number = number

    def evaluate(self):
        return self.number

#print Number(3).evaluate()

class BinaryOperator(object):
    def __init__(self,left,right,function):
        self.function = function
        self.right = right
        self.left = left

    def evaluate(self):
        return self.function(self.left.evaluate(),self.right.evaluate())


class Addition(BinaryOperator):
    def __init__(self,a,b):
        super(Addition,self).__init__(a,b,add)

class Multiplication(BinaryOperator):
    def __init__(self,a,b):
        super(Multiplication,self).__init__(a,b,mul)

#print Addition(Number(2),Multiplication(Number(3),Number(7))).evaluate()

class Sheet(object):
    def __init__(self):
        self.sheet={}

    def fill_in(self,address,expression):
        self.sheet[address]=expression

    def get_value(self,address):
        return self.sheet.get(address,Number(0)).evaluate()


class CellAddress(object):
    def __init__(self,address,sheet):
        self.sheet = sheet
        self.address = address

    def evaluate(self):
        return self.sheet.get_value(self.address)

class SumFunction(object):
    def __init__(self,range,sheet):
        self.sheet = sheet
        self.range = range

    def evaluate(self):
        [f,t]=self.range.split(":")
        frow = int(f[1:])
        trow = int(t[1:])
        col = f[0]
        sum = 0
        for row in xrange(frow,trow+1):
            sum+=self.sheet.get_value((col,row))
        return sum

s = Sheet()


# s.fill_in(("A",1),Number(2))
# s.fill_in(("A",2),Number(8))
#
# s.fill_in(("A",3),Addition(CellAddress(("A",1),s),CellAddress(("A",2),s)))
# s.fill_in(("A",4),SumFunction("A1:A3",s))
# print s.get_value(("A",4))

s.fill_in(("A",1),CellAddress(("A",2),s))
s.fill_in(("A",2),CellAddress(("A",1),s))
print s.get_value(("A",1))