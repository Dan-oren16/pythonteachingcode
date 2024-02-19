# [ ] create, call and test fishstore() function 
def fishstore(full_name, fish, price): 
    return ("Report for " + full_name.title() + ". " + "Fish Type: " + fish_entry.title() + " costs " + "$" + price_entry)

full_name = "Dan Oren"
fish_entry = input("Enter the name of the fish: ")
price_entry = input("Enter the price of the fish: ")

fishstore_final = fishstore(full_name, fish_entry, price_entry)

print(fishstore_final)