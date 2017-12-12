# CTI-110
# M3Lab - Debugging
# Christian McMillan
# 9/28
# This program converts number to letter grade.
def main():

    # System uses 10-point grading scale.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59

    #Input number grade.
    score = float(input('Enter grade: '))

    #Output letter grade.
    if score > A_score:
        print('Your grade is: A')
    else:
        if score > B_score:
            print('Your grade is: B')
        else:
            if score > C_score:
                print('Your grade is: C')
            else:    
                if score > D_score:
                    print('Your grade is: D')
                else:    
                    if score >= F_score:
                        print('Your grade is: F')                    
                                  

main() 
main()
main()
main()
main()




