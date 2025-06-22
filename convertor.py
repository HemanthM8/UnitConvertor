import argparse
import sys

#Function to convert celsius to fahrenheit
def celsius_to_fahrenheit(c :float) -> float:
    return (c * 9/5) + 32

#Function to convert fahrenheit to celsius
def fahrenheit_to_celsius(f :float) -> float:
    return (f - 32) * 5/9

# Function to print the banner
def print_banner():
    banner = """
=====================================
     Temperature Converter Tool
=====================================
"""
    print(banner)

# Main function to handle command line arguments and perform conversions
def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description='Convert temperatures between Celsius and Fahrenheit.',
        epilog='Example: python temp_converter.py --c2f 100'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--c2f', metavar='C', help='Convert Celsius to Fahrenheit')
    group.add_argument('--f2c', metavar='F', help='Convert Fahrenheit to Celsius')

    try:
        args = parser.parse_args()

        if args.c2f is not None:
            try:
                celsius = float(args.c2f)
                result = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f} °C is {result:.2f} °F")
            except ValueError:
                print("\n❌ Invalid Celsius value! Please enter a numeric value.")
                print("\n❌ Invalid input or argument! Use --help for usage instructions.")
                sys.exit(1)
        elif args.f2c is not None:
            try:
                fahrenheit = float(args.f2c)
                result = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f} °F is {result:.2f} °C")
            except ValueError:
                print("\n❌ Invalid Fahrenheit value! Please enter a numeric value.")
                print("\n❌ Invalid input or argument! Use --help for usage instructions.")
                sys.exit(1)

    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    main()
