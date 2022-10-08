# Constructor:
# >> A constructor is a special method that is called by default whenever you create an object from a class 

class Person(object):
    def __init__(self, name, age):
        print("An object has been created")
        self.name = name 
        self.age = age 
        return None 
        
## Destructor:
# >> Destructors are called when an object get destroyed. 
# >> in python, destructors are not needed as much needed in C++ \
# because Python has a garbage collector that handler memory manegement automatically 
    def __del__(self):
        print("Object has been deleted")
        return None     

## Polymorphism:
# >> Polymophism allows us to define same methods in d/f classes. 
## This process is also known as Method overriding 


class Tomcat(object):
    def __init__(self, home, version):
        print("An object has been created")
        self.home = home 
        self.version = version 
        return None 

    def display(self):
        print("This is from apache class")
        print(self.home)
        print(self.version)
        return None

class Appache(object):
    def __init__(self, home, version):
        print("An object has been created")
        self.home = home 
        self.version = version 
        return None 

    def display(self):
        print("This is from apache class")
        print(self.home)
        print(self.version)
        return None

def main():
    tomcat = Tomcat("/home/tomcat9", "7.6")
    appache = Appache("/ect/httpd", "2.4")
    tomcat.display()
    appache.display()


## Inheritance... 
# >> Inheritance is a mechanism that allows us to create a new class - known as child class 
# >> - that is based upon an existing class that parent class 


class Animal:
    def eat(self):
        print("I can eat")
        return None 

class Dog(Animal):
    def bark(self):
        print("I can bark")


dog1 = Dog()



# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Another 
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class PayrollSystem:

    def calculate_payroll(self, employees):
        print("-"*88)
        print("calculating Payroll")
        print("-"*88)
        for employee in employees:
            print(f'Payroll for employee with id: {employee.id} and name: {employee.name} has salary: {employee.calculate_payroll()}')
    
        return None      

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name   
        return None    

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        return None  

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        return None  

    def calculate_payroll(self):
         return self.hours_worked * self.hour_rate
          

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
        return None    

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


# employee_salary = SalaryEmployee(1,"John Smith", 1500)
# hour_salary = HourlyEmployee(20,"John Smith", 40, 60)
# commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = PayrollSystem()

# payroll_system.calculate_payroll([
#     employee_salary,
#     hour_salary,
#     commission_employee
# ])




# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Another 
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Employee: 

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.email = first + '.' + last + '@email.com'
        self.pay = pay 
        return None 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


dev_1 = Employee('Corey', 'Schafer', 50000)   
print(dev_1.email)
print(dev_1.apply_raise())
# print(dev_1.fullname())



# if __name__ == "__main__":
#     pass

## Iterator


numbers = [1,2,3,5,7]

item = iter(numbers)


while (True):
    try:
        element = next(item)
        print(element)
    except StopIteration:
        break

class Even(object):
    def __init__(self, *args):
        super(Even, self).__init__(*args)
        


#  We want to create one class/Template that would store employees details

class Employee:
    
    def __init__(self, name, age,salary, employee_id):
        self.name = name
        self.age = age  
        self.salary = salary 
        self.employee_id = employee_id
        return None

#     def assign_name_age_salary_id(self, name, age, salary, id): # This is method one
#         self.name = name
#         self.age = age  
#         self.salary = salary 
#         self.id = id
#         return None

    def display(self): # this is method two. # Display func doesn't have any variable 
    
        print(f"The employee name is: {self.name}\tand The employee age is: {self.age}\tand The employee salary is: ${ self.salary}\tand employee id is : {self.employee_id }")
        return None

# class Car:

#     def assign_atr(self, color, name, mileage, year):
#         self.color = color
#         self.name = name
#         self.mileage = mileage
#         self.year = year
#         # self.display()
#         return None

#     def display(self):
#         print(f"\tthe name of my car is {self.name}\tand the color is {self.color}\tand the mileage is {self.mileage}\tThe year is {self.year}")
#         return None


def main():
    # we need to create an object out of our employee template. 
    emp1 = Employee(name="Koji", age=25, salary=45000, employee_id=100)
    emp1.display()


if __name__ == "__main__":
    main()  

if __name__ == "__main__":
    main()
