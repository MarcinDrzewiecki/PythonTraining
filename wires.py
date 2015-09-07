__author__ = 'drzewiec'



wire = Wire()
wire.togglePower()

wire2=Wire()

gate = AndGate(wire,wire2)
gate.isPowered