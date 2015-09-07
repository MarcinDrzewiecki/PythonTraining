__author__ = 'drzewiec'
from operator import add,mul,sub

class Number(object):
    def __init__(self,number):
        self.number = number

    def evaluate(self):
        return self.number




n = Number(10)
print n.evaluate()

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

print Addition(Number(2),Multiplication(Number(3),Number(7))).evaluate()