def calculate_total(price, quantity):
    # Validation
    if price <= 0:
        raise ValueError("Invalid price")
    if quantity <= 0:
        raise ValueError("Invalid quantity")
    return price * quantity