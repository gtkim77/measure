import gpib
import time
import re

con = gpib.dev(0,4)

# F1 : Control I, A4: Stepwise Sweep, B1: VB DC, L2: VA I limit 1mA, M3, VB I limit: 10mA
# PS-10: Start V -10V, PT10: Stop V 10, PE1: Step V 1, N: Parameter terminator
# PH2 : Hold Time 2 s, PD.5: Step delay time .5 sec, PB-10: VB -10, PS  

gpib.write(con, 'F1A4B1L2M3\n')
gpib.write(con, 'PS-1;PT1,PE0.1;NPH2;PD.5,PB-10\n')
gpib.write(con, 'W1\n')

num = 70
val = gpib.read(con,23 * num).decode('ascii')

#I = float(re.findall("NI[+-].{9}", val)[0].replace('NI',''))
#V = float(re.findall("A[+-].{5}", val)[0].replace('A',''))

print(val)
#print(I)
#print(V)
gpib.write(con, 'W7\n')
