import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from scipy.stats import scoreatpercentile
import csv
import matplotlib.pyplot as plt
""

# read from input data file
with open('data/avocado.csv') as file:
    data = list(csv.reader(file, delimiter=','))

print('%d total data points' % len(data))
# create np array without column titles
data = np.array(data[1:])
years = data[:, 12]
avg_prices = data[:, 2].astype(float)
total_bags = data[:, 8].astype(float)
distinct_years = set(years)
print(distinct_years)
print(avg_prices)
print(total_bags)

overall_avg_price = np.mean(avg_prices)
overall_total_bags = np.sum(total_bags)
print('The average price of avocados from 2015 to 2018 is $%.2f' % overall_avg_price)
print('The total number of bags of avocados sold from 2015 to 2018 is %d' % overall_total_bags)

years_to_prices = {}
for year in distinct_years:
    years_to_prices[year] = []

"""
To find out how the average price of avocados has changed since 2015,
find out how the average price per year compare to each other
"""
for row in data:
    year = row[12]
    price = row[2].astype(float)
    # print(price)
    # np.append(years_to_prices[year], np.array(price))
    years_to_prices[year].append(price)

plot_values, x_values, y_values = [], [], []
for year in sorted(years_to_prices.keys()):
    years_to_prices[year] = np.array(years_to_prices[year])
    average_price_per_year = np.mean(years_to_prices[year])
    print(year, average_price_per_year)
    y_values.append(average_price_per_year)


plt.plot(sorted(distinct_years), y_values)
plt.title("Average price of avocados per year")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()






