# https://github.com/ericmuckley/IMES/blob/master/imes_libs/eis.py

import gpib
import time
import numpy as np

con = gpib.dev(0,6)

# reset device and use default configuration
gpib.write(con, '*RST\n')  # Reset
time.sleep(1)
gpib.write(con, '*SRE16\n') # Sets the service request enble register to the 16 bit
time.sleep(1)
gpib.write(con, 'OS 0\n') # Set the separator as comma  (if 1, terminator)
time.sleep(1)
gpib.write(con, 'RH 1\n')  # Set the heading as 'on'  (if 0, off)

# configure data output
gpib.write(con, 'OP 1,0\n')  # Set the RS423 off
gpib.write(con, 'OP 2,1\n')  # Set the GPIB, all 
gpib.write(con, 'OP 3,0\n')  # Set File, off
gpib.write(con, 'RH 0\n')   # Set Heading off (if 1, on)

print('F (Hz), Z (Ohm), Phase (deg)')
vac, vdc = 0.5, 0.0
for freq in [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6]:
    # configure generator output
    gpib.write(con, 'GT0\n')
    gpib.write(con, 'FR ' + str(freq) + '\n')
    gpib.write(con, 'VA ' + str(vac) + '\n')
    gpib.write(con, 'VB ' + str(vdc) + '\n')

    # turn off sweep
    gpib.write(con, 'SW 0\n')

    # acquire single measurement
    gpib.write(con, 'SI\n')
    time.sleep(1)

    output = gpib.read(con,50).decode('ascii')
    output = output.split(',')
    frequency = float(output[0])
    amplitude = float(output[1])
    phase_angle = float(output[2])
    output = [frequency, amplitude, phase_angle]
    print(output)
    print(amplitude * np.cos(np.radians(phase_angle)))
    print(amplitude * np.sin(np.radians(phase_angle)))
    print()
