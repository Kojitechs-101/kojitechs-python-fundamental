
# We want to create one class/Template that would store employees details

class Employee:

    def assign_name_age_salary_id(self, name, age, salary, id): # This is method one
        self.name = name
        self.age = age  
        self.salary = salary 
        self.id = id
        return None

    def display(self): # this is method two. # Display func doesn't have any variable 
        
        print(f"\tThe employee name is: {self.name}\tand The employee age is: {self.age}\tand The employee salary is: ${ self.salary}\tand employee id is : {self.id }")
        return None

class Car:

    def assign_atr(self, color, name, mileage, year):
        self.color = color
        self.name = name
        self.mileage = mileage
        self.year = year
        # self.display()
        return None

    def display(self):
        print(f"\tthe name of my car is {self.name}\tand the color is {self.color}\tand the mileage is {self.mileage}\tThe year is {self.year}")
        return None


def main():
    # we need to create an object out of our employee template. 
    emp1 = Employee()

    # we want to access either a METHOD inside employee or VARIABLE
    emp1.assign_name_age_salary_id(name="Baca",age=34, salary=200,id=1000)
    # print(emp1.id)


    ## Create am object from the class/template Car
    First_car = Car()
    First_car.assign_atr(color="white", name="Toyota", mileage=200000, year=2005)
    

    ## second car
    second_car = Car()
    second_car.assign_atr(color="white", name="Buic", mileage=90000, year=2013)
    
    
    ## Accessing any variable in class Car
    print(First_car.name)
    print(second_car.name)

    ##  Accessing any method in class Car
    First_car.display()
    second_car.display()


if __name__ == "__main__":
    main()


