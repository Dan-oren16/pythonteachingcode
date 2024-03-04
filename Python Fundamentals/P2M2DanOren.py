# Initialize variables first 
full_name = "Dan Oren"
plant_list = ["Pothos", "Snake", "Monstera", "Fittonia"]

# Defining the function list_o_matic 
def list_o_matic(input_string, input_list):
    if input_string == "":
        return print('"'+input_list.pop()+'"', "popped from list.")
    elif input_string.isdigit():
        return print("Invalid input, please try again.")
    else:
        if input_string in input_list:
            input_list.remove(input_string)
            return print('"'+input_string+'"', "removed from list.")
        else:
            input_list.append(input_string)
            return print("1 instance of", '"' + input_string + '"', "appended to list.")

        
# Start program flow        
while plant_list:
    print("\nWelcome, " + full_name + "." + " Look at the list of plants:", plant_list)
    check_string = input("Enter the name of a plant or \"quit\": ")
    if check_string.lower().startswith("q"):
        break
    else:
        list_o_matic(check_string, plant_list)
print("\nGoodbye!")