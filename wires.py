__author__ = 'drzewiec'



# wire = Wire()
# wire.togglePower()
#
# wire2=Wire()
#
# gate = AndGate(wire,wire2)
# gate.isPowered


def reverse_by_center(s):
    if len(s)%2==0:
        return s[len(s)/2:]+s[0:len(s)/2]
    else:
        return s[(len(s)/2)+1:]+s[len(s)/2]+s[0:len(s)/2]


print reverse_by_center("test")
print reverse_by_center("tesciki")