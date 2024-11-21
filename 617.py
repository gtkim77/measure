import gpib
import time
import re
import numpy as np

def generate_v(v_left, v_right, interval, mod):
    num = int((v_right - v_left) / interval) + 1
    v_list0 = [float("{:.3e}".format(v_left + i * interval)) if abs(v_left + i * interval) >= 0.0495 else 0 for i in range(num)]
    v_list0.index(0)
    if abs(mod) == 1:  # from left to right
        voltages = v_list0
    elif abs(mod) == 2:  # turn-around
        ind_zero = v_list0.index(0.0)
        if ind_zero < 0:
            voltages = v_list0 + list(reversed(v_list0))
        else:
            voltages = v_list0[ind_zero:] + list(reversed(v_list0)) + v_list0[:ind_zero] + [0.0]
    if mod < 0:
        voltages = list(reversed(v_list0)) 
    return voltages


con = gpib.dev(0,25)

v_info = input("Input the voltage range. left, right, step in series: ")
v_left, v_right, interval = [float(x) for x in v_info.split(' ') if x != '']
mode = int(input("Input the measurement mode (1: one-direction, 2: one-sweep): "))
ok = input("Will you measure now? (y/n) ")

gpib.write(con,'C0\n')
if ok == 'y':
    V = generate_v(v_left, v_right, interval, mode)
    I = []
    for voltage in V:
        cmd = "V{:.3e}O1X\n".format(voltage)
        gpib.write(con, cmd)
        time.sleep(0.1)
        result = gpib.read(con, 1024)
        current = float(re.findall(r"[+\-]?[^\w]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)", str(result))[0])
        I.append(current)
        output = 'Voltage: %.3eV Current: %.3e (A)' % (voltage, current)
        print(output)
        time.sleep(0.1)

print()
print(np.polyfit(I, V, 1))
