# Problem Statement:

# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2

speed_of_light = 299792458


def main():

    mass:float = float(input("Enter kilos of mass: "))
    C = speed_of_light

    energy =  mass * (C **  2)

    print("e = m * C^2 ")
    print(f"{mass}kg mass")
    print(f"{energy} joules of energy")


if __name__ == '__main__':
    main()