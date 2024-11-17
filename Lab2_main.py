import Lab2 as l2

def main():
    l2.display_main_menu()
    user_inputs = l2.get_user_input()
    average = l2.calc_averge(user_inputs)
    min_max = l2.find_min_max(user_inputs)
    ascending_temps = l2.sort_temperature(user_inputs)
    median = l2.calc_median_temperature(ascending_temps)

    print(f"Average Temperature is {average}.")
    print(f"Minimum Temperature - {min_max[0]}\nMaximum Temperature - {min_max[1]}")
    print(f"Median Temperature is {median}.")


if __name__ == "__main__":
    main()