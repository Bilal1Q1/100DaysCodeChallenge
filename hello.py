def Calculator(f_num, operator, s_num):
    if operator == '+':
        return f_num + s_num
    elif operator == '*':
        return f_num * s_num
    elif operator == '-':
        return f_num - s_num
    elif operator == '/':
        return f_num / s_num
    else:
        return 'Wrong Operator'
first_num = int(input('Enter first Number: '))
game_over = False
while not game_over:

    operator = input('\n+\n-\n*\n\\\n\nChoose operation: ')
    second_number = int(input('Enter Second Numnber: '))
    result = Calculator(first_num, operator, second_number)
    print(f"{first_num} {operator} {second_number} = {result}")
    continu = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculatio: ').lower()
    if continu == 'no':
        game_over = True
    else:
        first_num = result
        