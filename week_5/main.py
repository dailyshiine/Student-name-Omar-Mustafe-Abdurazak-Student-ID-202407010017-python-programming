from utils import calculate_total, print_receipt

def main():
    name = input("customer name: ")
    age = int(input("customer age: "))
    coffee = int(input("coffee quantity: "))
    tea = int(input("tea quantity: "))
    sandwich = int(input("sandwich quantity: "))

    total = calculate_total(coffee, tea, sandwich)
    print_receipt(name, age, coffee, tea, sandwich, total)


if __name__ == "__main__":
    main()