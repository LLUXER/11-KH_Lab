num_a = int(input("Enter first num: "))
num_b = int(input("Enter second num: "))

operator = input("enter operator: + - *(to multiply) /(divide) ")

if operator == '+':
    print(num_a + num_b)
if operator == '-':
    print(num_a - num_b)
if operator == '*':
    print(num_a * num_b)
if operator == '/':
    print(num_a / num_b)