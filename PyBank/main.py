import os 
import csv
from statistics import mean

# import csv file and creating lists to store data
csvpath= os.path.join("Resources","budget_data.csv")
months = []
profitloss = []

# formatting csv to seperate and store the two columns into corresponding empty list from above
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profitloss.append(int(row[1]))

#  variable that will store the interation of profit/loss column to find net change
netchange = []

for i in range(1,len(profitloss)):
    netchange.append(profitloss[i]-profitloss[i-1])
        

# sum of total months in data set
monthtotal = len(months)

# sum of the profit margin
totalprofitmargin = sum(profitloss)

# average of the sum of the net change 
averageprofitchange = mean(netchange)

# most profit made in a month
maxprofitgain = max(netchange)

# most profit loss in a month 
maxprofitloss = min(netchange)

# month that had the most profit gain   
maxmonthgain = months[netchange.index(maxprofitgain) + 1]

# month that had the most profit loss
maxmonthloss = months[netchange.index(maxprofitloss) + 1]

# Summary output
print(f"""
Finacial Analysis
------------------------
Total Months: {monthtotal}
Total: ${totalprofitmargin}
Average Change: ${round(averageprofitchange, ndigits= 2)}
Greatest Increase in Profits: {maxmonthgain} (${maxprofitgain})
Greatest Decrease in Profits: {maxmonthloss} (${maxprofitloss})"""
)



