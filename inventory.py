item_name = []
item_price = {}


print("\n ====INVENTORY MENU====")
print("1. Add Item")
print("2. Update Price")
print("3. Exit")

while True:

    choice = input("\nChoice: ")

    if choice == '1':
        name = input("Enter item name:")

        if name in item_name:
            print("Item already exists.")

        else:
            try:
                price_input = float (input("Enter item price:"))
                item_name.append(name)
                item_price[name] = price_input
                print("Item added successfully!")
            except ValueError:
                print("Invalid price. Enter price again.")

    elif choice == '2':
        name = input("Enter item name to update:")

        if name in item_name:
            try:
                new_price = float(input("Enter new price:"))
                item_price[name] = new_price
                print("Price updated successfully!")
            except ValueError:
                print("Invalid price. Enter price again.")
        else:
            print("Item not found in the inventory.")

    elif choice == '3':
        print("Exiting the program.")
        break   
    else:
        print("Invalid choice. Please try again.")