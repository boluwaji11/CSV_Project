import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(
    open_file, delimiter=","
)  # Reads the csv file and identifies the delimiter as comma

header_row = next(csv_file)  # Skips the first row

# The enumerate() function returns both the index of each item and the value of each
# item as you loop through a list.

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

# print(highs)

# Plot highs on a chart

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily High Temperature, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()