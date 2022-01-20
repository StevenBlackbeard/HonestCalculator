number_1 = float(input())
number_2 = float(input())
operator_in = input()
operator_ok = ["+", "-", "*", "pow"]
operator_warning = ["/", "mod", "div"]

if operator_in in operator_warning:
    if number_2 == 0:
        print("Division by 0!")
    else:
        if operator_in == "/":
            print(number_1 / number_2)
        elif operator_in == "mod":
            print(number_1 % number_2)
        else:
            print(number_1 // number_2)
else:
    if operator_in == "+":
        print(number_1 + number_2)
    elif operator_in == "-":
        print(number_1 - number_2)
    elif operator_in == "*":
        print(number_1 * number_2)
    else:
        print(number_1 ** number_2)
