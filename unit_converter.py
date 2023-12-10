def temperature_converter():
    print("Temperature Converter: Celsius to Fahrenheit and vice versa")
    while True:
        try:
            value = float(input("Enter temperature value: "))
            source_unit = input("Enter source unit (C or F): ").upper()
            target_unit = input("Enter target unit (C or F): ").upper()

            if source_unit == 'C' and target_unit == 'F':
                result = (value * 9/5) + 32
                print(f"{value}°C is equal to {result:.2f}°F")
            elif source_unit == 'F' and target_unit == 'C':
                result = (value - 32) * 5/9
                print(f"{value}°F is equal to {result:.2f}°C")
            else:
                print("Invalid source or target unit. Please enter 'C' or 'F'.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        except Exception as e:
            print(f"Error: {e}")

        another_conversion = input("Do you want to perform another temperature conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

def length_converter():
    print("Length Converter: Meters to Feet and vice versa")
    while True:
        try:
            value = float(input("Enter length value: "))
            source_unit = input("Enter source unit (M or F): ").upper()
            target_unit = input("Enter target unit (M or F): ").upper()

            if source_unit == 'M' and target_unit == 'F':
                result = value * 3.28084
                print(f"{value} meters is equal to {result:.2f} feet")
            elif source_unit == 'F' and target_unit == 'M':
                result = value / 3.28084
                print(f"{value} feet is equal to {result:.2f} meters")
            else:
                print("Invalid source or target unit. Please enter 'M' or 'F'.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        except Exception as e:
            print(f"Error: {e}")

        another_conversion = input("Do you want to perform another length conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

def weight_converter():
    print("Weight Converter: Kilograms to Pounds and vice versa")
    while True:
        try:
            value = float(input("Enter weight value: "))
            source_unit = input("Enter source unit (K or P): ").upper()
            target_unit = input("Enter target unit (K or P): ").upper()

            if source_unit == 'K' and target_unit == 'P':
                result = value * 2.20462
                print(f"{value} kilograms is equal to {result:.2f} pounds")
            elif source_unit == 'P' and target_unit == 'K':
                result = value / 2.20462
                print(f"{value} pounds is equal to {result:.2f} kilograms")
            else:
                print("Invalid source or target unit. Please enter 'K' or 'P'.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        except Exception as e:
            print(f"Error: {e}")

        another_conversion = input("Do you want to perform another weight conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

def main():
    print("Welcome to the Unit Converter!")

    while True:
        print("\nChoose an option:")
        print("1. Temperature Converter")
        print("2. Length Converter")
        print("3. Weight Converter")
        print("4. Quit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            temperature_converter()
        elif choice == '2':
            length_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
