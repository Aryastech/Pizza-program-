
def caffeinated_menu():
    print("\n--- Caffeinated Drinks Menu ---")
    drinks = [
        "1. Espresso",
        "2. Latte",
        "3. Flat White",
        "4. Mocha",
        "5. Tea"
    ]
    for drink in drinks:
        print(drink)
    
    while True:
        try:
            caffeinated_choice = int(input("Select your drink: "))
            if 1 <= caffeinated_choice <= 5:
                print(f"Adding drink {caffeinated_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def Fruit_menu():
    print("\n--- Fruit Refreshers Drinks Menu ---")
    drinks = [
        "1. Strawberry Refreshers",
        "2. Watermellon Refreshers",
        "3. Mango Refreshers",
        "4. Lemonade Refreshers",
        "5. Blueberry Refreshers"
    ]
    for drink in drinks:
        print(drink)
    
    while True:
        try:
            fruit_choice = int(input("Select your drink: "))
            if 1 <= fruit_choice <= 5:
                print(f"Adding drink {fruit_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def Cream_menu():
    print("\n--- Cream-based Drinks Menu ---")
    drinks = [
        "1. Strawberry Refreshers",
        "2. Watermellon Refreshers",
        "3. Mango Refreshers",
        "4. Lemonade Refreshers",
        "5. Blueberry Refreshers"
    ]
    for drink in drinks:
        print(drink)
    
    while True:
        try:
            _choice = int(input("Select your drink: "))
            if 1 <= fruit_choice <= 5:
                print(f"Adding drink {fruit_choice} to your order.")
                break
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")





def drink_type():
     print("\n--- Drinks Type ---")
     print("1. Caffeinated Drinks")
     print("2. Fruit Refreshers")
     print("3. Cream-Based Refreshers")
     while True:
        try:
            drink_type_choice = int(input("Enter your Drink Type: "))
            if drink_type_choice in [1, 2, 3]:
                if drink_type_choice == 1:
                    caffeinated_menu()  
                if drink_type_choice == 2:
                    Fruit_menu()      
                break
            else:
                print("Invalid choice Please enter a number between 1 and 3")    
        except ValueError:
            print("Invalid input Please enter a valid number")
            
         
        
        return drink_type_choice 

def drink_size():
    print("\n--- Drink Size ---")
    print("1. Small - $5.00")
    print("2. Medium- $6.50")
    print("3. Large- $7.50")
    while True:
        try:
            drink_choice = int(input("Enter your Drink Size: ")) 
            if drink_choice in [1, 2, 3]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 and 3")    
        except ValueError:
            print("Invalid input Please enter a valid number")  
    drink_type()
    return drink_choice 

def order_type():
    print("\n --- Order Type ---")
    print("Order for 1. Pickup or 2. Delivery") 
    while True:
        try:
            choice_order_type = int(input("Enter your option")) 
            if choice_order_type in [1, 2]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 or 2")    
        except ValueError:
            print("Invalid input Please enter a valid number")
    if choice_order_type == 1:
            print("Pickup is free and should be ready in 5-10 minites")
            drink_size()
    elif choice_order_type == 2: 
            print("Delivery is $3.49 , Orders talke 5-10 minites after order")
            drink_size()
        
def menu():
    print("\n--- Welcome to Dash Drink ---")
    order_type()

menu()