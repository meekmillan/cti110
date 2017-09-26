# CTI-110
# M2T1 - Sales Prediction
# Christian McMillan
# 9/12/17
# This program calculates a precentage based on user input.

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of the total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
