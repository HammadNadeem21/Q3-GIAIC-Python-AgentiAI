def fahrenheit_to_celsius():

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit -32) * 5.0 / 9.0

    print(f"Tempreture: {float(fahrenheit):.1f}°F = {celsius:.4f}°C")


if __name__ == '__main__':
    fahrenheit_to_celsius()
