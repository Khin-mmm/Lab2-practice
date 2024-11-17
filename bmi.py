def calculate_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    
    bmi = weight/ (height ** 2)

    return bmi


def analyse_bmi(bmi):
    if bmi < 18.5:
        condition = 'under weight'
    elif bmi >= 18.5 and bmi <= 25.0:
        condition = 'normal weight'
    elif bmi > 25.0:
        condition = 'over weight'
    return condition


def print_result(weight, height, bmi):
    print(f"Your Height is {height} m.")
    print(f"Your Weight is {weight} kg.")
    #print(f"Your Bmi is {bmi}.")
    print(f"Your Bmi is {round(bmi, 2)}.")
    #print(f"Your Bmi is {bmi:.2f}.")
    #print(f"Your Bmi is {"%.2f" % bmi}.")

    condition = analyse_bmi(bmi)
    print(f"You are {condition.title()}.")

    again = input("Do you want to calculate again? (Yes/No): ")
    return again


active = True
def main():
    global active
    while active:
        print("Enter 'q' anytime to quit the program.")
        height = input("Enter your height in m: ")
        if height == 'q':
            break
        weight = input("Enter your weight in kg: ")
        if weight == 'q':
            break
        bmi = calculate_bmi(weight=weight, height=height)
        again = print_result(weight, height, bmi)
        if again.lower() == 'no':
            active = False
            
main()

