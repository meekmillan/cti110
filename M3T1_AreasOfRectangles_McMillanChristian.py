# CTI-110
# M3T1 Areas Of Rectangles
# Christian McMillan
# 9/26
# This program will calculate the area of a rectangle.

#Rectangle alpha dimensions
length_a =int(input('input alpha length: '))
width_a =int(input('input alpha width: '))

#Rectangle bravo dimensions
length_b =int(input('input bravo length: '))
width_b =int(input('input bravo width: '))

#Calculate dimensions
alpha_area = length_a * width_a
bravo_area = length_b * width_b

#Display results
if alpha_area > bravo_area:
    print('Rectangle alpha has the greatest area.')
elif alpha_area < bravo_area:
    print('Rectangle bravo has the greatest area.')
else:
    print('Both have the same area')
