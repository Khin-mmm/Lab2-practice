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
    ascending_temps = sorted(list)
    return ascending_temps

def calc_median_temperature(list):
    temp_num = len(list)
    half_temp_num = int(temp_num / 2)
    if temp_num % 2 == 0:
        median = (list[half_temp_num] + list[half_temp_num - 1]) / 2
    elif temp_num % 2 == 1:
        median = list[half_temp_num]
    return median