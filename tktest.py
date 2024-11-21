import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :10.0')
    os.environ.__setitem__('DISPLAY', ':10.0')

root = tkinter.Tk()
root.mainloop()
