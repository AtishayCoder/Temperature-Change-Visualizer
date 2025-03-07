import matplotlib.pyplot as plt

item_nos = int(input("How many changes are there to show (Number)? "))

times = []
temps = []

for i in range(item_nos):
    ti = input("What is the time for the change? ")  # Time as a string (e.g., "10 AM")
    te = float(input("What is the temperature (Decimal or integer)? "))  # Numeric value
    times.append(ti)
    temps.append(te)

plt.title("Temperature Graph")
plt.plot(times, temps, color="red", marker="o", linestyle="-")
plt.xlabel("Time")
plt.ylabel("Temperature (centigrate)")
plt.grid(True)
plt.show()
