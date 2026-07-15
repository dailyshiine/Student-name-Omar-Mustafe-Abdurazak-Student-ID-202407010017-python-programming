def get_customer():
    print("=== Customer Information ===")
    
    
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    
    
    if food.lower() == "cake":
        price = 3.00
    else:
        price = 2.50
        
    print(f"Price per Item (RM): {price:.2f}")
    
    delivery_input = input("Delivery (Y/N): ")
    
    
    if delivery_input.upper() == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00
        
   
    return name, food, quantity, price, delivery_charges