V1 = [9.0, 5.0]
Vout = 1.0
R2 = 1e3
R1max = ((V1[0]*R2)/Vout) - R2
R1min = ((V1[1]*R2)/Vout) - R2
print(R1min)
print(R1max)
