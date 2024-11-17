#print("ET0735 (DevOps for AToT) - Lab2 - Introduction to Python")
def display_main_menu():
    print('Enter some numbers seperated by commas (e.g. 5, 67, 32)')


def get_user_input():
    input_string = input()
    input_list = input_string.split(',')
    final_input_list = []
    for value in input_list:
        final_input_list.append(float(value.strip()))
    return final_input_list


def calc_averge(list):
    average = round(sum(list)/len(list), 2)
    return average


def find_min_max(list):
    min_temp = int(min(list))
    max_temp = int(max(list))
    min_max = [min_temp, max_temp]
    return min_max

def sort_temperature(list):
    return

def calc_median_temperature(list):
    return

def main():
    display_main_menu()
    user_inputs = get_user_input()
    average = calc_averge(user_inputs)
    min_max = find_min_max(user_inputs)

    print(f"Average Temperature is {average}.")
    print(f"Minimum Temperature - {min_max[0]}\nMaximum Temperature - {min_max[1]}")

if __name__ == "__main__":
    main()