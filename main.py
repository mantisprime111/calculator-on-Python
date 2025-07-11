def calculator():
    print("Выберите операцию: + - * /")
    operation = input().strip()
    try:
        number1 = float(input("Ведите первое число: "))
        number2 = float(input("Ведите второе число: "))
    except ValueError:
        print("Нужно вводить числа :(")
        return

    if operation == "+":
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("На ноль делить нельзя")
            return
        result = number1 / number2
    else:
        print("Неверная операция")
        return
    print(f"Результат: {result}")
    
    
calculator()