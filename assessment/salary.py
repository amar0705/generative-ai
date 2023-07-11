def max_salary_employee(employees):
    max_salary = float('-inf')
    max_salary_employee = None
    for employee in employees:
        salary = employee.get('salary', 0)
        if(salary>max_salary):
            max_salary = salary
            max_salary_employee = employee


    return max_salary_employee
