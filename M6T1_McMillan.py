#CTI-110
#M6T1 - Kilometers to miles conversion
#Christian McMillan
#11/30
#This program will take a kilometer input and output the value in miles

# km to mi

mi_km = 0.6214

def main():
# kilometer input

    km = float(input('Enter a distance in km:'))
    show_mi(km)
    
def show_mi(km):
# conversion 
    
    mi = km * mi_km
    
# display miles

    print(km, 'kilometers equals', mi, 'miles')
        
main()
