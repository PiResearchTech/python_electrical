import math
truepower = 120
Apparent = 170
value = truepower/Apparent
print('result=',math.acos(value), 'in radians')
degrees = math.acos(value) * (180 / 3.14)
print('result=', degrees,'in degrees')