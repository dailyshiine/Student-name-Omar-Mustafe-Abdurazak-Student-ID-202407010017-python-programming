def get_employee():
    print("=== Employee Information ===")
    name = input("Employee Name : ")
    emp_id = input("Employee ID   : ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))

    ot_hours = float(input("Overtime Hours Worked: "))
    years_worked = int(input("Years of Service: "))

    return name, emp_id, basic_salary, allowance, ot_hours, years_worked