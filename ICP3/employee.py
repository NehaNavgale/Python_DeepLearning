#employee class 'Parent class'
class Employee:

   noOfEmployee = 0 # a data member to count the number of Employees

   totSalary = 0 # a data member to save the total salary

   # constructor for Employee class
   def __init__(self):
      self.name = input('Name :')
      self.family = input('Family :')
      self.department = input('Department :')
      self.salary = int(input('Salary :'))
      Employee.noOfEmployee += 1
      Employee.totSalary += self.salary

    #a function to return employee data
   def employeeDetails(self):
          employeeData = {}
          employeeData['Details of employee'] = Employee.noOfEmployee
          employeeData['Name'] = self.name
          employeeData['Family'] = self.family
          employeeData['Department'] = self.department
          employeeData['Salary'] = self.salary
          return employeeData

    #function to average salary
   def displayAvg(self):
        avg = Employee.totSalary/Employee.noOfEmployee
        return avg