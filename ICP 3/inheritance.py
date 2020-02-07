class Employee:
    emp_count = 0
    emp_salaries = []

    def __init__(self, name, family, salary, department):
        self.emp_department_name = department
        self.emp_salary = salary
        self.emp_family = family
        Employee.emp_count=Employee.emp_count+1
        Employee.emp_salaries.append(salary)
        self.emp_name = name

    def get_salary(self):
        total_salaries = 0
        for s in Employee.emp_salaries:
            total_salaries = total_salaries + s
        return total_salaries / len(Employee.emp_salaries)

class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


f1 = FullTimeEmployee("sahaja", "Adavelli", 1000000, "CS")
f2 = FullTimeEmployee("Sree", "tata", 1200000, "CSE")
f3 = FullTimeEmployee("Zeal", "Patel", 600000, "CS")
avg_salary = f2.get_salary()
print("All the employees together has an average salary of", avg_salary)
