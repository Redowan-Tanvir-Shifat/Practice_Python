## Inputs-->
# Total rent
# Total food ordered
# Electricity units
# Charge per units
# Number of persons 

## output
# Total amount you have to pay

rent = int(input("Enter your flat rent: "))
food = int(input("Enter the amount of food order: "))
electricity_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons: "))

total_electricity_bill = (electricity_spend * charge_per_unit)

each_person_cost = (rent + food + total_electricity_bill) // persons

print("\nEach person will pay: ", each_person_cost)