def Add(num1, num2):
    return num1 + num2
def Subtract(num1, num2):
    return num1 - num2
def Multiply(num1, num2):
    return num1 * num2
def Divide(num1, num2):
    return num1 / num2
operations = {
    '+' : Add,
    '-': Subtract,
    '*' : Multiply,
    '/' : Divide
}
calculatin_function = operations['+']
print('Add'())
