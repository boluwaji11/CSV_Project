import matplotlib.pyplot as plt
import csv
from datetime import datetime
from datetime import timedelta


def main():

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
            print(
                f"There is a missing data for {converted_date + timedelta(days=1)}."
            )  # Display missing date
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
            death_valley_station = row[
                death_valley_station_index
            ]  # Gets the station name
        except ValueError:
            print(
                f"There is a missing data for {converted_date + timedelta(days=1)}."
            )  # Display missing date
            print("This date is not included on the Death Valley chart.")
        else:
            death_valley_highs.append(high_temp)
            death_valley_lows.append(low_temp)
            death_valley_dates.append(converted_date)

    # Plotting two charts using subplots()
    fig, chart = plt.subplots(2)

    # Sitka
    fig1 = chart[0]
    fig1.plot(sitka_dates, sitka_highs, c="red")
    fig1.plot(sitka_dates, sitka_lows, c="blue")

    # Death Valley
    fig2 = chart[1]
    fig2.plot(death_valley_dates, death_valley_highs, c="red")
    fig2.plot(death_valley_dates, death_valley_lows, c="blue")

    # Format the chart
    fig.autofmt_xdate()
    fig.suptitle(
        f"Temperature comparison between {sitka_station} and {death_valley_station} in 2018",
        fontsize=12,
    )

    # Chart titles
    fig1.set_title(sitka_station, fontsize=11)
    fig2.set_title(death_valley_station, fontsize=11)

    # Fill Between the charts
    fig1.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.1)
    fig2.fill_between(
        death_valley_dates,
        death_valley_highs,
        death_valley_lows,
        facecolor="blue",
        alpha=0.1,
    )

    # Common Y and X-Axis Labels
    fig.text(
        0.05,
        0.5,
        "Temperature (F)",
        va="center",
        ha="center",
        rotation="vertical",
        fontsize=11,
    )

    fig.text(0.5, 0.05, "Date", va="center", ha="center", fontsize=11)

    # Display the charts
    plt.show()

    # Save a PNG file of the chart
    fig.savefig("Temperature_sitka_death_valley_2018.png", dpi=300)


# Call the main function
main()