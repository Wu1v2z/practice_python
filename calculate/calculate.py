Num_1 = float(input('Enter first number: '))
Num_2 = float(input('Enter second number: '))
Operation = input('Enter the operation: ')

if Operation == '+' :
    print(Num_1, ' + ', Num_2, ' = ', Num_1 + Num_2)     
elif Operation == '-' :
    print(Num_1, ' - ', Num_2, ' = ', Num_1 - Num_2)     
elif Operation == '*' :
    print(Num_1, ' * ', Num_2, ' = ', Num_1 * Num_2)     
elif Operation == '/' :
    print(Num_1, ' / ', Num_2, ' = ', Num_1 / Num_2)  
elif Operation == 'sqrt':
    chose = input('Chose the number: ')
    if chose == '1':
        print('Sqrt of', Num_1, '=', Num_1 ** 0.5)
    if chose == '2':
        print('Sqrt of', Num_2, '=', Num_2 ** 0.5)
else:
    print('Not realised') 


print('Thanks for your used my calculate')




