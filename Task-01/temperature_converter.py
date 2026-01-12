# Temperature Conversion Program

def convert_temperature(value, unit):
    if unit == "C":
        f = (value * 9/5) + 32
        k = value + 273.15
        return f, k
    elif unit == "F":
        c = (value - 32) * 5/9
        k = c + 273.15
        return c, k
    elif unit == "K":
        c = value - 273.15
        f = (c * 9/5) + 32
        return c, f
    else:
        return None

print("Temperature Converter")
value = float(input("Enter temperature value: "))
unit = input("Enter unit (C, F, K): ").upper()

result = convert_temperature(value, unit)

if result:
    if unit == "C":
        print(f"Fahrenheit: {result[0]:.2f}, Kelvin: {result[1]:.2f}")
    elif unit == "F":
        print(f"Celsius: {result[0]:.2f}, Kelvin: {result[1]:.2f}")
    elif unit == "K":
        print(f"Celsius: {result[0]:.2f}, Fahrenheit: {result[1]:.2f}")
else:
    print("Invalid unit")

