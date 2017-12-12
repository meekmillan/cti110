#CTI-110
#M6T2 - feet to inches conversion
#Christian McMillan
#11/30
#This program will convert feet to inches

# km to mi

ft_inch = 12

def main():
# feet input

    ft = float(input('Enter a distance in feet:'))
    show_inch(ft)
    
def show_inch(ft):
# conversion 
    
    inch = ft * ft_inch
    
# display inches

    print(ft, 'feet equals', inch, 'inches')
    
main()
