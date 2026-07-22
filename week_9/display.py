def display_ticket(ticket):
    print("\n======== helpdesk ticket =======")
    print(f"student name : {ticket['name']}")
    print(f"student_id: {ticket['student_id']}")
    print(f"issue: {ticket['issue']}")
    print(f"location: {ticket['location']}")
    print(f"priority: {ticket['priority']}")
    print(f"technician: {ticket['technician']}")
    print(f"status: {ticket['status']}")
    print("==================================")
    