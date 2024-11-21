# https://github.com/ericmuckley/IMES/blob/master/imes_libs/eis.py

import pyvisa
import time

rm = pyvisa.ResourceManager()
con = rm.open_resource('GPIB0::6::INSTR')

# reset device and use default configuration
con.write('*RST\n')  # Reset
time.sleep(1)
con.write('*SRE16\n') # Sets the service request enble register to the 16 bit
time.sleep(1)
con.write('OS 0\n') # Set the separator as comma  (if 1, terminator)
time.sleep(1)
con.write('RH 1\n')  # Set the heading as 'on'  (if 0, off)

# configure data output
con.write('OP 1,0\n')  # Set the RS423 off
con.write('OP 2,1\n')  # Set the GPIB, all 
con.write('OP 3,0\n')  # Set File, off
con.write('RH 0\n')   # Set Heading off (if 1, on)

print('F (Hz), Z (Ohm), Phase (deg)')
vac, vdc = 0.5, 0.0
for freq in [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6]:
    # configure generator output
    con.write('GT0\n')
    con.write('FR ' + str(freq) + '\n')
    con.write('VA ' + str(vac) + '\n')
    con.write('VB ' + str(vdc) + '\n')

    # turn off sweep
    con.write('SW 0\n')

    # acquire single measurement
    con.write('SI\n')
    time.sleep(1)

#    output = con.read_bytes(50).decode('ascii')
    output = con.read_raw().decode('ascii')
    output = output.split(',')
    output = [float(out) for out in output[:3]]
    print(output)

