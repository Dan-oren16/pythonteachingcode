# [ ] create, call and test the adding_report() function
def adding_report(report = "T"):  
    total = 0 
    items = "Items\n" 
    full_name = "Dan Oren"  
    while True: 
        user_input = input("Enter an integer or \"Quit\": ") 
        if user_input.isdigit():
            total += int(user_input)
            if report == "A":
                items += user_input + "\n"
        elif user_input.lower().startswith("q"):
            if report == "A":
                print("\n" + items + "\n" + "Total:\n" + str(total) + "\nCalculated by: " + full_name) 
                break
            else:
                print("\nTotal:\n" + str(total) + "\nCalculated by: " + full_name)
                break
        else:
            print("Input is Invalid")
adding_report("A")  