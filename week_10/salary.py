def calculate_overtime(ot_hours):
    return ot_hours * 25.0

def calculate_loyalty_bonus(years_worked):
    if years_worked > 3:
        return 500.0
    return 0.0

def calculate_gross_salary(basic_salary, allowance, ot_hours, years_worked):
    ot_pay = calculate_overtime(ot_hours)
    bonus = calculate_loyalty_bonus(years_worked)
    return basic_salary + allowance + ot_pay + bonus

def calculate_epf(gross_salary):
    return gross_salary * 0.11

def calculate_socso(gross_salary):
    return gross_salary * 0.005

def calculate_net_salary(gross_salary, epf, socso):
    return gross_salary - epf - socso