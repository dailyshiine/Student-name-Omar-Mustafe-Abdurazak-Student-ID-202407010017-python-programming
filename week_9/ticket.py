def create_ticket():
    """
    This will collect the ticket information from the user, assign it to a technician,
    and return the ticket information to the main function.
    """
    print("=== IT Helpdesk Ticket ===")

    name = input("Student Name : ")
    student_id = input("Student ID  : ")
    issue = input("Issue        : ")
    location = input("Location    : ")

    # Keep asking until a valid priority is entered
    priority = input("Priority (High/Medium/Low): ").strip().capitalize()
    while priority not in ("High", "Medium", "Low"):
        print("Invalid priority. Please enter High, Medium, or Low.")
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()

    technician_map = {
        "High": "Shiine",
        "Medium": "Mustafe",
        "Low": "Siti"
    }
    technician = technician_map[priority]

    ticket = {
        "name": name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": "Pending"
    }

    return ticket