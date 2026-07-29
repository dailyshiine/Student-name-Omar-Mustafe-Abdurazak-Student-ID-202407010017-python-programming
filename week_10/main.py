import employee
import salary
import report

def main():
    name, emp_id, basic_salary, allowance, ot_hours, years_worked = employee.get_employee()

    gross_salary = salary.calculate_gross_salary(basic_salary, allowance, ot_hours, years_worked)
    epf = salary.calculate_epf(gross_salary)
    socso = salary.calculate_socso(gross_salary)
    net_salary = salary.calculate_net_salary(gross_salary, epf, socso)

    report.print_report(name, emp_id, gross_salary, epf, socso, net_salary)

if __name__ == "__main__":
    main()