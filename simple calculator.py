operation = input('''
type the required maths operation:
+ for addition
- for substraction
* for multiplication
/ for division
''')

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

if operation == '+':
    print ('{} + {} = '. format(n1, n2))
    print (n1 + n2)

elif operation == '-':
    print ('{} - {} = '. format(n1 , n2))
    print (n1 - n2)

elif operation == '*':
    print ('{} * {} = '.format (n1, n2))
    print (n1 * n2)

elif operation == '/':
    print ('{} /{} = '. format(n1, n2))
    print (n1 / n2)

else :
    print (" The operation etered is invalid. Restart the programme.")
