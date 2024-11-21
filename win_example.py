import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12.8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3, 2]
         }

df2 = pd.DataFrame(data2, columns=['Year', 'Unemployment_Rate'])

def donothing():
    pass
    
root = tk.Tk()
root.title("Gas Environment Simulator")
root.minsize(480, 480)
root.resizable(0, 0)


figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

main_menu = tk.Menu(root)
gases_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Gas Selection", menu=gases_menu)
sensors_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Sensor Selection", menu=sensors_menu)
concentrations_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Concentrations", menu=concentrations_menu)
help_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Help", menu=help_menu)

# Sub menu: gases_menu
gases_menu.add_command(label="VOC", command=donothing)
gases_menu.add_command(label="Hydrogen Carbon", command=donothing)
gases_menu.add_command(label="Toxic Gases", command=donothing)
gases_menu.add_command(label="Otheres", command=donothing)

# Sub menu: sensors_menu
sensors_menu.add_command(label="Resistive", command=donothing)
sensors_menu.add_command(label="Electrochemical", command=donothing)
sensors_menu.add_command(label="PID", command=donothing)

# Sub menu: concentrations_menu
concentrations_menu.add_command(label="Highest", command=donothing)
concentrations_menu.add_command(label="Lowest", command=donothing)
concentrations_menu.add_command(label="Randomize", command=donothing)
concentrations_menu.add_command(label="Custom", command=donothing)

# Sub menu: help_menu
help_menu.add_command(label="Index", command=donothing)
help_menu.add_command(label="About…", command=donothing)
help_menu.add_command(label="Exit", command=root.quit)

root.config(menu = main_menu)
root.mainloop()
