# Week 8 - Food Delivery Receipt Generator

## Purpose
This project is a small backend component for a Food Delivery System. Since the UI part wasn't built yet, my task was to create the receipt generator that takes customer info and calculates the final bill (subtotal, service charge, delivery fee, and total).

## Tech Stack
- Python 3
- Ran on GitHub Codespaces

## Files
- `customer.py` - gets customer input (name, food, quantity, delivery option)
- `receipt.py` - calculates and prints the receipt
- `main.py` - runs the program

## How to Use
1. Open the `week_8` folder
2. Run:
```bash
python main.py
```
3. Enter the customer's name, food (Cake/Muffin), quantity, and delivery option (Y/N)
4. It will print out the full receipt with subtotal, service charge, delivery charge, and total

## Demo
![Food Order Demo](./demo.gif)