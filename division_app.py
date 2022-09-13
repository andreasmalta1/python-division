print("Division App")
while True:
    try:
        num1 = int(input("Num 1: "))
        num2 = int(input("Num 2: "))
        print(str(num1), "/", str(num2), "=", str(num1/num2))
        break
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("Please only input digits")

