from art import logo, numbers_art

print(logo)

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def guard(num):
    try:
        int(num)
        return  True
    except:
        return False


calculated = True
repeat = False
result = 0


while calculated:
    while True:
        try:
            mode = input(
                "Choose an arithmetic operation.\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n")
            int(mode)
            if int(mode) > 0 and int(mode) < 5:
                break
            else:
                print("Incorrect choice. Try again.")
        except:
            print("Incorrect choice. Try again.")

    while True:
        if repeat == True:
            a = result
            b = input("Enter the second number ")
            if "." in b:
                b = float(b)
            elif "," in b:
                b = b.replace(",", ".")
                b = float(b)
            else:
                b = int(b)
        else:
            a = input("Enter the first number ")
            b = input("Enter the second number ")

            if "." in a:
                a = float(a)
            elif "," in a:
                a = a.replace(",", ".")
                a = float(a)
            else:
                a = int(a)

            if "." in b:
                b = float(b)
            elif "," in b:
                b = b.replace(",", ".")
                b = float(b)
            else:
                b = int(b)


        while True:
            if int(mode) == 4 and int(b) == 0:
                print("You can't divide by 0 :(")
                b = input("Enter the second number ")
            else:
                break

        if guard(a) == True and guard(b) == True:

            if int(mode) == 1:
               result = sum(a, b)
               oper = "+"
            elif int(mode) == 2:
                result = diff(a, b)
                oper = "-"
            elif int(mode) == 3:
                result = mult(a, b)
                oper = "*"
            elif int(mode) == 4:
                result = div(a, b)
                oper = "/"

            if type(result) == float:
                checked = int(result * 10)
                checked = str(checked)
                count = 0
                for x in checked:
                    count +=1
                last_num = checked[count-1]
                if int(last_num) == 0:
                    result = int(result)

            print(numbers_art(a, b, oper, result))
            print(f"Result: {round(result, 5)}")
            break
        else:
            print("Need numbers.")

    while True:
        exit_calc = input("Do you want to keep counting? 'y' or 'n' ")
        if exit_calc == 'y':
            break
        elif exit_calc == 'n':
            print("See you later. Bye.")
            calculated = False
            break
        else:
            print("Unknown command")

    if calculated == True:
        while True:
            cont = input("Do you want to continue with last result? 'y' or 'n' ").lower()
            if cont == 'y':
                repeat = True
                break
            elif cont == 'n':
                repeat = False
                break
            else:
                print("Unknown command")


