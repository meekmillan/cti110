#CTI-110
#M3HW2 - Software sales
#Christian McMillan
#10/6
#This program will show the given discount based on volume of items purchesed.

#Input amount purchased
item_amount = int(input('Enter amount purchased: '))

#Item cost
item_cost = 99

#Discount legend
if item_amount < 10:
    discount = 0;
elif item_amount < 20:
    discount = 0.10
elif item_amount < 50:
    discount = 0.20
elif item_amount < 100:
    discount = 0.30
else:
    discount = 0.40

#Total calculator    
sub_total = item_amount * item_cost
discount_amount = discount * sub_total
total = sub_total - discount_amount

def main():
 
    #Output discount
    if item_amount < 10:
        print('After no discount')
    else:
        if item_amount < 20:
            print ('After discount of 10%')
        else:
            if item_amount < 50:
                print ('After discount of 20%')
            else:
                if item_amount < 100:
                    print('After discount of 30%')
                else:
                        print('After discount of 40%')

main()

#Output totals
print('Total discount is: $' + format( discount_amount, ",.2f"))
print('Total price after discount is: $', format( total, ",.2f"))


#Profit???
