def get_student():
    print("===== Computer Lab Access =====")
    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Y/N): ").upper() == "Y"
    lab_open = input("Is the lab open? (Y/N): ").upper() == "Y"
    computer_available = input("Computer Available? (Y/N): ").upper() == "Y"
    return name, student_id, registered, lab_open, computer_available