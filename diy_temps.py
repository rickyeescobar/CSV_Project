import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)













fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

plt.show()