import math

def menu():
    print("\n=== Scientific Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sin (degrees)")
    print("8. Cos (degrees)")
    print("9. Tan (degrees)")
    print("10. Log (base e)")
    print("11. Log (base 10)")
    print("12. Exit")

def calculator():
    while True:
        menu()
        choice = input("Enter your choice (1-12): ")

        try:
            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a + b)

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a - b)

            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", a * b)

            elif choice == "4":
                a = float(input("Enter numerator: "))
                b = float(input("Enter denominator: "))
                print("Result:", a / b)

            elif choice == "5":
                x = float(input("Enter base: "))
                y = float(input("Enter exponent: "))
                print("Result:", math.pow(x, y))

            elif choice == "6":
                x = float(input("Enter number: "))
                print("Result:", math.sqrt(x))

            elif choice == "7":
                x = float(input("Enter angle in degrees: "))
                print("Result:", math.sin(math.radians(x)))

            elif choice == "8":
                x = float(input("Enter angle in degrees: "))
                print("Result:", math.cos(math.radians(x)))

            elif choice == "9":
                x = float(input("Enter angle in degrees: "))
                print("Result:", math.tan(math.radians(x)))

            elif choice == "10":
                x = float(input("Enter number: "))
                print("Result:", math.log(x))

            elif choice == "11":
                x = float(input("Enter number: "))
                print("Result:", math.log10(x))

            elif choice == "12":
                print("Calculator closed.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
