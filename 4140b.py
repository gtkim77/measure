import gpib
import time
import re

con = gpib.dev(0,4)

#F1 : Control I, F2: I-V
#RA1 : Auto Range
#I3 : Integration time Long
#T1 : I Trigger Internal
#E : Trigger
#gpib.write(con, 'F1A5B1RA1I3T1L2M3\n')
#gpib.write(con, 'PA-1.0;PB0.0\n')

gpib.write(con, 'F2A4B1RA1I1L2M3\n')
gpib.write(con, 'PS0;PT1.0,PE.1NPH1;PV1,PB-1\n')
gpib.write(con, 'W1\n')

num = 22
#val = gpib.read(con,23 * num).decode('ascii')

Vs = []
Is = []

while True:
    val = gpib.read(con,23 * 1).decode('ascii')
    V = float(re.findall("A[+-].{5}", val)[0].replace('A',''))
    Vs.append(V)
    if val[1:2] == 'N':
        print('len: %d, symbol: %1s, result: %s' % (len(val),val[1:2], val))
        I = float(re.findall("NI[+-].{9}", val)[0].replace('NI',''))
        Is.append(I)
    if val[1:2] == 'L':
        I = float(re.findall("LI[+-].{9}", val)[0].replace('LI',''))
        Is.append(I)
        print('len: %d, symbol: %1s, result: %s' % (len(val),val[1:2], val))
        break

print(Vs)
print(Is)

#I = float(re.findall("NI[+-].{9}", val)[0].replace('NI',''))
#V = float(re.findall("A[+-].{5}", val)[0].replace('A',''))

#print(val)
#print(I)
#print(V)

#time.sleep(0)
#gpib.write(con, 'A6B2\n')
#gpib.write(con, 'PA0.0;PB0.0\n')
#gpib.write(con, 'W7\n')
