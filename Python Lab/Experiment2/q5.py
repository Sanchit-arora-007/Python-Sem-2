a = int(input('Enter coefficient of x square: '))
b = int(input('Enter coefficient of x: '))
c = int(input('Enter constant: '))

d = b*b - (4*a*c)

if d >= 0:
    print('Real Roots')
    root1 = (-b + (d**0.5)) / (2*a)
    root2 = (-b - (d**0.5)) / (2*a)
else:
    print('Imaginary Roots')
    root1 = (-b + (d**0.5)) / (2*a)
    root2 = (-b - (d**0.5)) / (2*a)

print('Roots are:', root1, root2)
