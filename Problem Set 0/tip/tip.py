# Calculate the tip to leave on a meal
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Convert a the dollar amount to a float
def dollars_to_float(d):
    return float(d.replace("$", ""))

# Convert a percentage to a float
def percent_to_float(p):
    return float(p.replace("%", "")) / 100


main()