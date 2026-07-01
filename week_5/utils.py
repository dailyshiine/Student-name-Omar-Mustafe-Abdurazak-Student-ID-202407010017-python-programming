COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


# THIS IS THE FUNCTION FOR CALCULATING
def calculate_total(coffee, tea, sandwich):
    total = (coffee * COFFEE_PRICE) + (tea * TEA_PRICE) + (sandwich * SANDWICH_PRICE)
    return total


# this is the function for printing the receipt
def print_receipt(name, age, coffee, tea, sandwich, total):
    print("\n====== RECEIPT ====")
    print(f"customer : {name}")
    print(f"age      : {age}")
    print(f"coffee   : {coffee}")
    print(f"tea      : {tea}")
    print(f"sandwich : {sandwich}")
    print("_____________")
    print(f"total = RM {total:.2f}")