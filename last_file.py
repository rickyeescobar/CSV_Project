import csv
from datetime import datetime
import matplotlib.pyplot as plt



##sitka file

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)


for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:",column_header)

highs = []
dates = []
lows = []
station =[]


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    station.append(row[1])
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

### death valley file

open_file1 = open("death_valley_2018_simple.csv", "r")

csv_file1 = csv.reader(open_file1, delimiter= ',')

header_row1 = next(csv_file1)


for index1, column_header1 in enumerate(header_row1):
    print("Index:", index1, "Column Name:",column_header1)

highs1 = []
dates1 = []
lows1 = []
station1 =[]

for row in csv_file1:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date1 = datetime.strptime(row[2],'%Y-%m-%d')
    
    except ValueError:
        print(f'missing data for {converted_date1}')
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(converted_date1)
        station1.append(row[1])


###Subplots

fig, a = plt.subplots(2)


# figure 1

a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")


#a[0].autofmt_xdate
a[0].fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

a[0].set_title(station[1], fontsize=16)
#a[0].xlabel("", fontsize=12)
#a[0].ylabel("Temperature (F)", fontsize=12)
#a[0].tick_params(axis="both",labelsize=12)

# figure 2

a[1].plot(dates1, highs1, c="red",)
a[1].plot(dates1, lows1, c="blue")

#a[1].autofmt_xdate
a[1].fill_between(dates1,highs1,lows1, facecolor='blue', alpha=0.1)

a[1].set_title(station1[1], fontsize=16)
#a[1].xlabel("", fontsize=12)
#a[1].ylabel("Temperature (F)", fontsize=12)
#a[1].tick_params(axis="both",labelsize=12)

plt.show()