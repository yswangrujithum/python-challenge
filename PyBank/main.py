import os
import csv

csvPath = os.path.join("..","Resources","budget_data.csv")
data_output = os.path.join("output_budget_data.txt")

print("Financial Analysis")
print("-------------------------------------------")

def month_reader():

    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ",")
        csv_header = next(csvfile)
        month = sum(1 for row in csvfile)
    return month
    
month_reader()

def total_count():

    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        csv_header = next(csvfile)
        sum_profit_lost = sum(int(row[1]) for row in csvreader)
    return sum_profit_lost

total_count()

def revenue_data():
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        csv_header = next(csvfile)
        total_revenue = []
        change_revenue = []

        for row in csvreader:
            total_revenue.append(int(row[1]))
        
        for i in range(1,len(total_revenue)):
            change_revenue.append(total_revenue[i] - total_revenue[i-1])
            avg_revenue = sum(change_revenue)/len(change_revenue)
        return avg_revenue
        
revenue_data()

def greatest_increase():
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        csv_header = next(csvfile)
        total_revenue = []
        change_revenue = []
        date = []

        for row in csvreader:
            total_revenue.append(int(row[1]))
            date.append(row[0])
        for i in range(1,len(total_revenue)):
            change_revenue.append(total_revenue[i] - total_revenue[i-1])
            max_increase = max(change_revenue)
            num_max_increase = change_revenue.index(max_increase)
            max_date = str(date[num_max_increase])
        return max_date, max_increase

greatest_increase()

def greatest_decrease():
    with open(csvPath,newline="") as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ",")
        csv_header = next(csvfile)
        total_revenue = []
        change_revenue = []
        date = []

        for row in csvreader:
            total_revenue.append(int(row[1]))
            date.append(row[0])
        for i in range(1,len(total_revenue)):
            change_revenue.append(total_revenue[i] - total_revenue[i-1])
            max_decrease = min(change_revenue)
            num_max_decrease = change_revenue.index(max_decrease)
            min_date = str(date[num_max_decrease])
        return min_date, max_decrease
greatest_decrease()

print('Total Months: ', month_reader())
print('Total: $', total_count())
print('Average Change: ', revenue_data())
print('Greatest Increase in Profits: ', greatest_increase())
print('Greatest Decrease in Profits: ', greatest_decrease())

data_output = open('output_budget_data.txt','w')
data_output.write('Financial Analysis\n')
data_output.write('--------------------------------\n')
data_output.writelines(f'Total Months:  {month_reader()}\n')
data_output.writelines(f'Total: $ {total_count()}\n')
data_output.writelines(f'Average Change: $ {revenue_data()}\n')
data_output.writelines(f'Greatest Increase in Profits: {greatest_increase()}\n')
data_output.writelines(f'Greatest Decrease in Profits: {greatest_decrease()}\n')

