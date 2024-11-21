# https://pyvisa.readthedocs.io/en/latest/introduction/rvalues.html

import pyvisa
import time
import re

rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::4::INSTR')

#F1 : Control I, F2: I-V
#RA1 : Auto Range
#I3 : Integration time Long
#T1 : I Trigger Internal
#E : Trigger
inst.write('F1A5B1RA1I3T1L2M3\n')
inst.write('PA-1.0;PB0.0\n')
inst.write('W1\n')

num = 1
val = inst.read_bytes(23 * num).decode('ascii')

I = float(re.findall("NI[+-].{9}", val)[0].replace('NI',''))
V = float(re.findall("A[+-].{5}", val)[0].replace('A',''))

print(val)
print(I)
print(V)

time.sleep(0)
inst.write('A6B2\n')
inst.write('PA0.0;PB0.0\n')
inst.write('W7\n')
