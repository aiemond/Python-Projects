def get_user_input():
    rent = int(input("Enter the monthly rent for your hostel or flat: "))
    food = int(input("Enter the total amount spent on food: "))
    electricity_usage = int(input("Enter the total electricity usage in units: "))
    rate_per_unit = int(input("Enter the charge per unit of electricity: "))
    num_persons = int(input("Enter the number of persons living in the room or flat: "))
    return rent, food, electricity_usage, rate_per_unit, num_persons

def calculate_total_electricity_cost(electricity_usage, rate_per_unit):
    return electricity_usage * rate_per_unit

def calculate_total_cost_per_person(rent, food, total_electricity_cost, num_persons):
    return (rent + food + total_electricity_cost) // num_persons

def main():
    rent, food, electricity_usage, rate_per_unit, num_persons = get_user_input()
    total_electricity_cost = calculate_total_electricity_cost(electricity_usage, rate_per_unit)
    total_cost_per_person = calculate_total_cost_per_person(rent, food, total_electricity_cost, num_persons)
    print("Each person will need to pay: ", total_cost_per_person)

if __name__ == "__main__":
    main()
