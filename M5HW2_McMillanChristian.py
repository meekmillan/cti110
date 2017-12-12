#CTI-110
#M5HW2 - Running Total
#Christian McMillan
#10/24
#This program will calculate a running total

# Initialize
total=0
newNum = int (input( "Enter a number?: "))

# Enter loop
while newNum >=0:
    total +=newNum
    newNum = int (input( 'Enter a number?: '))

# Print end of loop total
print("Total: ",total)


