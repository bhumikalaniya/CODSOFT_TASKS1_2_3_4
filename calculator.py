print("****____WELCOME TO THE CALCULATER____****")
while True:
    num1 = float(input("ENTER THE FIRST NUMBER:"))
    num2 = float(input("ENTER THE SECOND NUMBER:"))

    print("CHOOSE AN OPERATION")
    print("1. ADD(+)")
    print("2. SUB(-)")
    print("3. MULTIPLICATION(*)")
    print("4. DIVISION(/)")
    choice = input("ENTER YOUR CHOICE:")

    if choice == "1":
        result = num1 + num2
        print(f"RESULT: {num1}+{num2} =", result)
    elif choice == "2":
        result = num1 - num2
        print(f"RESULT: {num1}-{num2} =", result)
    elif choice == "3":
        result = num1 * num2
        print(f"RESULT: {num1}*{num2} =", result)
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"RESULT: {num1}/{num2} =", result)
        else:
            print("CANNOT DIVIDE BY 0")
    else:
        print("INVALID CHOICE")

    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != "y":
        print("____***END***____")
        break
