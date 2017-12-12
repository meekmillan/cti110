#CTI-110
#M2HW2 Tip Tax Total
#McMillan Christian
#9/19

food_cost = float(input('Enter food cost: '))
tip = .18
sales_tax = .07


total = (food_cost * tip) + (food_cost * sales_tax) + food_cost

print('The total cost is $', format(total, ',.2f'))
      

