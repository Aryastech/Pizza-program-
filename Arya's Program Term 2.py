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
    print("")





def menu():
    print("Welcome to Dash Drink ") 



menu()