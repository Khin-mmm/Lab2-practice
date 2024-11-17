def calculate_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    
    bmi = weight/ (height ** 2)
    return_value = print_result(weight, height, bmi)
    return return_value


def analyse_bmi(bmi):
    if bmi < 18.5:
        condition = 'under weight'
        val = -1
    elif bmi >= 18.5 and bmi <= 25.0:
        condition = 'normal weight'
        val = 0
    elif bmi > 25.0:
        condition = 'over weight'
        val = 1
    print(f"You are {condition.title()}.")
    return val


def print_result(weight, height, bmi):
    print(f"Your Height is {height} m.")
    print(f"Your Weight is {weight} kg.")
    #print(f"Your Bmi is {bmi}.")
    print(f"Your Bmi is {round(bmi, 2)}.")
    #print(f"Your Bmi is {bmi:.2f}.")
    #print(f"Your Bmi is {"%.2f" % bmi}.")

    return_value = analyse_bmi(bmi)
     
    return return_value


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
        calculate_bmi(weight=weight, height=height)
        again = input("Do you want to calculate again? (Yes/No): ")
        if again.lower() == 'no':
            active = False
            
if __name__ == "__main__":
    main()

