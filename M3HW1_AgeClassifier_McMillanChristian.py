


def main():

    # Age class.
    Infant =  1.0
    Child = 12
    Teenager = 19
    Adult = 20

    #Input age.
    age = float(input('Enter age: '))

    #Output age class.
    if age <= Infant:
        print('You are a infant')
    else:
        if age <= Child:
            print('You are a child')
        else:
            if age <= Teenager:
                print('You are a teenager')
            else:
                if age >= Adult:
                    print('You are an adult')
                    
        
main()

