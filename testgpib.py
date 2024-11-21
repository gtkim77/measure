import pyvisa
rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::7::INSTR')
print(inst.query("*IDN?"))
