import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Open the Sitka and death valley csv files
open_sitka = open("sitka_weather_2018_simple.csv", "r")
open_death_valley = open("death_valley_2018_simple.csv", "r")

# Read the sitka and death valley csv files and identifies the delimiter as comma
csv_sitka = csv.reader(open_sitka, delimiter=",")
csv_death_valley = csv.reader(open_death_valley, delimiter=",")

# Reads the first row of the sitka and death valley files
header_sitka = next(csv_sitka)
header_death_valley = next(csv_death_valley)

# Get the indexes for the dates, station name, high and low temperatures for sitka and death valley.
# Sitka
for index, column_header in enumerate(header_sitka):
    if column_header == "TMAX":
        sitka_high_index = index
    if column_header == "TMIN":
        sitka_low_index = index
    if column_header == "DATE":
        sitka_date_index = index
    if column_header == "NAME":
        sitka_station_index = index

# Death Valley
for index, column_header in enumerate(header_death_valley):
    if column_header == "TMAX":
        death_valley_high_index = index
    if column_header == "TMIN":
        death_valley_low_index = index
    if column_header == "DATE":
        death_valley_date_index = index
    if column_header == "NAME":
        death_valley_station_index = index

# Get list of Sitka high temperature, low temperature and dates values from file
sitka_highs = []
sitka_lows = []
sitka_dates = []

for row in csv_sitka:
    try:
        high_temp = int(row[sitka_high_index])
        low_temp = int(row[sitka_low_index])
        converted_date = datetime.strptime(row[sitka_date_index], "%Y-%m-%d")
        sitka_station = row[sitka_station_index]  # Gets the station name
    except ValueError:
        print(f"There is a missing data for {converted_date}")
        print("This date is not included on the Sitka chart.")
    else:
        sitka_highs.append(high_temp)
        sitka_lows.append(low_temp)
        sitka_dates.append(converted_date)

# Get list of Death Valley high temperature, low temperature and dates values from file
death_valley_highs = []
death_valley_lows = []
death_valley_dates = []

for row in csv_death_valley:
    try:
        high_temp = int(row[death_valley_high_index])
        low_temp = int(row[death_valley_low_index])
        converted_date = datetime.strptime(row[death_valley_date_index], "%Y-%m-%d")
        death_valley_station = row[death_valley_station_index]  # Gets the station name
    except ValueError:
        print(f"There is a missing data for {converted_date}")
        print("This date is not included on the Death Valley chart.")
    else:
        death_valley_highs.append(high_temp)
        death_valley_lows.append(low_temp)
        death_valley_dates.append(converted_date)


# Plot two charts using subplots()

fig, chart = plt.subplots(2)
# Sitka
fig1 = chart[0]
fig1.plot(sitka_dates, sitka_highs, c="red")
fig1.plot(sitka_dates, sitka_lows, c="blue")

# Death Valley
fig2 = chart[1]
fig2.plot(death_valley_dates, death_valley_highs, c="red")
fig2.plot(death_valley_dates, death_valley_lows, c="blue")

# Format the date axis
fig.autofmt_xdate()
fig.suptitle(
    f"Temperature comparison between {sitka_station} and {death_valley_station}"
)
fig1.set_title(sitka_station)
fig2.set_title(death_valley_station)

# Display the charts
plt.show()

# plt.title("Daily High and Low Temperature - 2018", fontsize=16)
# plt.xlabel("Dates", fontsize=10)
# plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
# plt.ylabel("Temperature (F)", fontsize=12)
# plt.tick_params(axis="both", labelsize=12)

# plt.show()


# plt.show()
