def main():
    earth_wight = float(input("Enter your weight on Earth (kg): "))

    mars_weight = earth_wight * 0.378

    print(f"The equivalent on Mars: {round(mars_weight)} kg")


if __name__ == '__main__':
    main()