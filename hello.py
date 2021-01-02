def Add(n1,n2):
    return n1 + n2
def Subtract(n1,n2):
    return n1 - n2
def Multiply(n1,n2):
    return n1 * n2
def Divide(n1,n2):
    return n1/n2
operations = {
    '+' : Add,
    '-': Subtract,
    '*' : Multiply,
    '/' : Divide
}
num1 = int(input('Enter first Number: '))

for key in operations:
    print(key)
game_over = False
while not game_over:
    operation_symbol = input('Choose the Operation: ')    
    num2 = int(input('Enter second Number: '))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(12,2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
    continu = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to exit: ').lower()
    if continu == 'y':
        num1 = answer
    else:
        game_over = True
