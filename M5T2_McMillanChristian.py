#CTI-110
#M3HW2 - Bug Collector
#Christian McMillan
#10/12
#This program will total and display the amount of bugs collected in 7 days

# initialize
bugTotal = 0

# get bugs collected daily
for day in range(1, 8):
    # prompt user
    print ('Enter the number of bugs collected on day', day)

    # input bugs
    bugs = int(input())

    # calculate total
    bugTotal += bugs
    
# display total bugs
    print('You have collected', bugTotal, 'bug(s) by day', day)
print('Totaling', bugTotal, 'bugs this week.')
