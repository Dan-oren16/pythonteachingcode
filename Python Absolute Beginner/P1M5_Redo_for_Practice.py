def adding_report(report = "T"): 
    total = 0
    items = "Items\n"
    full_name = "Dan Oren"
    while True: 
        user_input = input("Enter an integer or \"Quit\": ")
        if user_input.isdigit(): 
            total += int(user_input)
            if report.upper() == "A": 
                items += user_input + "\n"
        elif user_input.lower().startswith("q"): 
            if report.upper() == "A":
                print("\n" + items + "\ntotal:\n" + str(total) + "\nCalculated by: " + full_name)
                break
            else: 
                print("\nTotal:\n" + str(total) + "\n" + "Calculated by: " + full_name)
                break 
        else: 
            print("Input is invalid.")
adding_report("A")
