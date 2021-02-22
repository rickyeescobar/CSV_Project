#1) change the file to include all the data for the year of 2018
#2) fill in later

import csv
from datetime import datetime


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ',')

header_row = next(csv_file)

#The enumerate() function returns both the index of each item and the value of each 
#item as you loop through a list.

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:",column_header)

highs = []
dates = []
lows = []

#as an example
#mydate ='2018-07-01'
#converted_date = datetime.strptime(mydate,'%Y-%m-%d')
#print(converted_date)


#we call this method strptime() using the string containing the date we want to work with as its first argument. the second argument tells 
#python...


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)
    


#print(highs)
#print(dates)


#plot highs on chart

import matplotlib.pyplot as plt


fig=plt.figure()

plt.plot(dates, highs, c="red",)
plt.plot(dates, lows, c="blue")


fig.autofmt_xdate()

#we pass fill_between() the list dates for the x values and the low y-value series 
#and lows. the facecolor argument determines the color of the shadd region; we give it a 
#low alpha value of 0.1 so the filled region connnects the two data series without distracting from the
#info that they represent

plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both",labelsize=12)


plt.show()

#matplotlib's pyplot API has a convenience function called subplots() which acts as a 
#utility wriapper and helps in createing common layouts of subplots, including the 
#enclising figure object, in a single call.

fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

plt.show()
