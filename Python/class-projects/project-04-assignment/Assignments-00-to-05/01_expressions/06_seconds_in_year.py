# Problem Statement

# Use Python to calculate the number of seconds in a year, and tell the user what the result

days_per_year = 365
hours_per_day = 24
min_per_hour = 60
sec_per_min = 60

def seconds_in_year():

    sec_in_year = days_per_year * hours_per_day * min_per_hour * sec_per_min

    print(f"There are {sec_in_year} seconds in a year")

if __name__ == '__main__':
    seconds_in_year()