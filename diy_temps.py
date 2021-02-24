import csv
from datetime import datetime




fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

plt.show()