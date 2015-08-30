__author__ = 'drzewiec'




class Node(object):
    def __init__(self,v,l,r):
        self.r = r
        self.v = v
        self.l = l
    def h(self):
        return 1+max(self.l.h(),self.r.h())
    def s(self):
        return node1.v + self.r.s() + self.l.s()

class Nil(object):
    def h(self):
        return 0
    def s(self):
        return 0

node0 = Nil()
print node0.h()

node1 = Node(2,Node(3,Nil(),Node(5,Nil(),Node(1,Nil(),Nil()))),Node(-1,Nil(),Nil()))

print node1.h()
print node1.s()
#policzyc sume wszystkich wartosci