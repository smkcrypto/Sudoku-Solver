def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
def calculate_tax_new_regime(income):

    slabs = [
        (300000, 0.00),
        (700000, 0.05),
        (1000000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (4700000, 0.30)
    ]
    deduction = 75000
    rebate_limit = 700000
    education_cess = 0.04

    # Apply standard deduction
    income -= deduction

    # If income after deduction is less than or equal to rebate limit
    if income <= rebate_limit:
        return 0

    # Calculate tax based on slabs
    tax = 0
    previous_slab = 0
    for slab_limit, slab_rate in slabs:
        if income > slab_limit:
            tax += (slab_limit - previous_slab) * slab_rate
            previous_slab = slab_limit
        else:
            tax += (income - previous_slab) * slab_rate
            break

    # Add education cess
    tax += tax * education_cess

    return tax


def calculate_tax_old_regime(income):
    slabs = [
        (250000, 0.00),
        (500000, 0.05),
        (1000000, 0.20),
        (17750000, 0.30)
    ]
    standard_deduction = 50000
    education_cess = 0.04

    # Apply standard deduction
    income -= standard_deduction

    # Calculate tax based on slabs
    tax = 0
    previous_slab = 0
    for slab_limit, slab_rate in slabs:
        if income > slab_limit:
            tax += (slab_limit - previous_slab) * slab_rate
            previous_slab = slab_limit
        else:
            tax += (income - previous_slab) * slab_rate
            break

    # Add education cess
    tax += tax * education_cess

    return tax
def calculate_tax_old_regime_tax_saving(income):
    slabs = [
        (250000, 0.00),
        (500000, 0.05),
        (1000000, 0.20),
        (17750000, 0.30)
    ]
    standard_deduction = 50000
    education_cess = 0.04

    # Apply standard deduction
    income -= standard_deduction

    deductions_80c = float(input("Enter your deductions under Section 80C:(EPF+LifeInsurance+NPS): "))
    deductions_80d = float(input("Enter your deductions under Section 80D: "))
    home_loan_interest = float(input("Enter your home loan interest deduction under Section 24(b): "))
    income -= min(deductions_80c, 150000)  # Section 80C limit
    income -= deductions_80d  # Section 80D for medical insurance
    income -= min(home_loan_interest, 200000)  # Section 24(b) for home loan interest
    tax = 0
    previous_slab = 0
    for slab_limit, slab_rate in slabs:
        if income > slab_limit:
            tax += (slab_limit - previous_slab) * slab_rate
            previous_slab = slab_limit
        else:
            tax += (income - previous_slab) * slab_rate
            break

    # Add education cess
    tax += tax * education_cess

    return tax



def main():
    global Repeat
    Repeat =True
    while(Repeat):
        income = float(input("Enter your annual income: "))
        user_choice = get_boolean_input("Do you have tax saving schemes? (yes/no): ")
        if (not user_choice):
            tax_new = calculate_tax_new_regime(income)
            tax_old = calculate_tax_old_regime(income)
            print(f"Tax according to the new tax regime: ₹{tax_new:.2f}")
            print(f"Tax according to the old tax regime: ₹{tax_old:.2f}")
            print(f"It's always better to go with new tax regime when you have no tax saving scheme: ₹{tax_new:.2f}")
        else:
            print("You Choosen yes, so let's check some tax savings and find the result")
            tax_new = calculate_tax_new_regime(income)
            tax_old = calculate_tax_old_regime_tax_saving(income)
            print(f"Tax according to the new tax regime: ₹{tax_new:.2f}")
            print(f"Tax according to the old tax regime: ₹{tax_old:.2f}")
            if tax_new < tax_old:
                print(f"It's better to go with new tax regime: ₹{tax_new:.2f}")
            else:
                print(f"It's better to go with old tax regime: ₹{tax_old:.2f}")
        Repeat = get_boolean_input("wanna calculate once more? (yes/no): ")



if __name__ == "__main__":
    main()




