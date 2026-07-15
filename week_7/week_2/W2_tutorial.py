# Step 1: Get inputs from the user
age = int(input("Enter your age: "))

# For yes/no questions, we convert the text to lowercase and check if it equals 'yes'
is_accompanied_input = input("Are you accompanied by an adult? (yes/no): ").strip().lower()
is_accompanied = (is_accompanied_input == "yes")

has_ticket_input = input("Do you have a valid ticket? (yes/no): ").strip().lower()
has_ticket = (has_ticket_input == "yes")

# Step 2 & 3: Evaluate the expression based on the theater rules
# Rule: (Age >= 13 OR Accompanied) AND Must have a ticket
if (age >= 13 or is_accompanied) and has_ticket:
    print("Access Allowed")
else:
    print("Access Denied")