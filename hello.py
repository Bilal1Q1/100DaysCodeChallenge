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
operator = input('\n+\n-\n*\n\\\n\nChoose operation: ')
second_number = int(input('Enter Second Numnber: '))
result = Calculator(first_num, operator, second_number)
print(result)
