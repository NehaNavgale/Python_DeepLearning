#Importing Employee Class
from employee import Employee

#Inheriting parent class Employee to child class FullTimeEmployee
class FulltimeEmployee(Employee):
    def __init__(self):
        Employee.__init__(self)

#Created instance of parant class
Employee1 = Employee()
print(Employee1.employeeDetails())

##Created instance of child class
FulltimeEmployee1 = FulltimeEmployee()
print(FulltimeEmployee1.employeeDetails())

print("First Employee Name: ", Employee1.name)
print("Second Employee Name: ", FulltimeEmployee1.name)

# Access data member using FulltimeEmployee class
print("Number of Employees: " , Employee.noOfEmployee)
print(FulltimeEmployee1.displayAvg())