import numpy as np
import csv
import matplotlib.pyplot as plt


# read from input data file
with open('data/avocado.csv') as file:
    data = list(csv.reader(file, delimiter=','))

print('There are %d total data points' % (len(data)-1))

# create np array without column titles
data = np.array(data[1:])

# find the average price of avocados and total amount sold throughout all the years
years = data[:, 12]
distinct_years = set(years)
avg_prices = data[:, 2].astype(float)
total_bags = data[:, 8].astype(float)
overall_avg_price = np.mean(avg_prices)
overall_total_bags = np.sum(total_bags)
print('The average price of avocados from %s to %s is $%.2f' % (min(distinct_years), max(distinct_years), overall_avg_price))
print('The total number of bags of avocados sold in this period is %d' % overall_total_bags)


"""
---------------------------------------------------------------------------
To find out how the average price of avocados has changed since 2015,
find out how the average price per year compare to each other
---------------------------------------------------------------------------
"""


def price_per_year(data):
    # initialize dictionary that map years to prices
    years_to_prices = {}
    for year in distinct_years:
        years_to_prices[year] = []

    for row in data:
        year = row[12]
        price = row[2].astype(float)
        years_to_prices[year].append(price)

    y_values = []
    print('Year\tAverage Price')
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


"""
---------------------------------------------------------------------------
To find out the most popular kind of avocado (based on plu code) per year,
find the max average total of each avocado type for each year

Column titles that we care about: '4046', '4225', '4770'
---------------------------------------------------------------------------
"""


def most_popular_per_year(data):
    codes = ['4046', '4225', '4770']
    plu_lists_by_year, year_to_type_amount = {}, {}

    # initialize dictionary plu_lists_by_year with a list of lists (all values per type of avocado per year)
    for year in distinct_years:
        year_to_type_amount[year] = ()
        plu_lists_by_year[year] = [[], [], []]

    for row in data:
        year = row[12]
        plu_4046 = row[4].astype(float)
        plu_4225 = row[5].astype(float)
        plu_4770 = row[6].astype(float)
        plu_lists_by_year[year][0].append(plu_4046)
        plu_lists_by_year[year][1].append(plu_4225)
        plu_lists_by_year[year][2].append(plu_4770)

    # determine which type has the highest total; write to file the plu_code and value of the highest total per year
    for year in plu_lists_by_year.keys():
        max_total = 0.0
        for index, plu_values in enumerate(plu_lists_by_year[year]):
            total = np.sum(np.array(plu_values))
            if total > max_total:
                max_total = total
                year_to_type_amount[year] = (codes[index], total)

    print(sorted(year_to_type_amount.items()))
    with open('results/most_popular_type_per_year','w+') as out_file:
        out_file.write('Year |\tPLU  |\tTotal Sold\n')
        out_file.write('--------------------------\n')
        for year, type_tuple in sorted(year_to_type_amount.items()):
            output_string = '%s |\t%s |\t%d\n' % (year, type_tuple[0], type_tuple[1])
            out_file.write(output_string)


price_per_year(data)
most_popular_per_year(data)
