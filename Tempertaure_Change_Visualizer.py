import numpy as np
import matplotlib.pyplot as plt

item_nos = int(input("How many changes are there to show (Number)? "))

times = []
temps = []

for i in range(item_nos):
    ti = input("What is the time for the change? ")
    te = float(input("What is the temperature(Decimal or integer)? "))

    times.append(ti)
    temps.append(te)

np_times = np.array(times)
np_temps = np.array(temps)

plt.title("Temperature graph")
plt.plot(np_times, np_temps, color = "red")
plt.show()
