def drink_size():
    print("1. Small")
    print("1. Medium")
    print("1. Large")
    while True:
        try:
            choice = int(input("Enter your Drink Size: ")) 
            if choice in [1, 2, 3]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 and 3")    
        except ValueError:
            print("Invalid input Please enter a valid number")   

def order_type():
    print("Order for 1. Pickup or 2. Delivery") 
    while True:
        try:
            choice_order_type = int(input("Enter your option")) 
            if choice_order_type in [1, 2,]:   
                break 
            else:
                print("Invalid choice Please enter a number between 1 or2")    
        except ValueError:
            print("Invalid input Please enter a valid number")
        if choice_order_type == 1:
            print("Pickup is free and should be ready in 5-10 minites")
            drink_size()
        if choice_order_type == 1: 
            print("Delivery is $3.49 , Orders talke 5-10 minites after order")
            drink_size()
        
def menu():
    print("welcome to Dash Drink")
    order_type()

menu()