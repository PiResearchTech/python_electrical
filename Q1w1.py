print('Minimum current requirement for an inverter')
fan = 150
pc = 150
LED = 40
voltage = 230
total = fan+pc+LED
minimumI = total / voltage
print('minimum current requirement of interval:', minimumI)
