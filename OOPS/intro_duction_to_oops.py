# OOP'S
# OBJECT
# ORIENTED 
# PROGRAMMING (OOP's)

## Class (collect or grouping of method.)
## Object (These are like variables)
## Polymorphism... 
## Encapsulation ... 
## Inheritance... 
## Inheritance...

class Employee:

    def list_of_empoyee_attr(self, first_name, last_name, salary, hired_date, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.hired_date = hired_date 
        self.employee_id = employee_id
        return None 

    def display_employee_attr(self):
        print(f"MY first_name is: {self.first_name} MY last_name  is: {self.last_name}\
            My salary is: ${self.salary}\tmy hired date is {self.hired_date}\
                my Employee id is: {self.employee_id}")
        return None         


def main():
    emp1 = Employee()
    emp2 = Employee()
    emp1.list_of_empoyee_attr(first_name=" koji", last_name= "Bello", salary = 40000, hired_date="09-10-2020",employee_id = 101)
    emp1.display_employee_attr()

    emp2.list_of_empoyee_attr(first_name="jason", last_name= "paul", salary = 5000, hired_date="09-10-2020",employee_id = 104)

    emp2.display_employee_attr()

my_buckets = [
    "ecs.terraform.cluster.terraform", 
    "ecs.working.cluster.terraform",
    "elasticbeanstalk-us-east-1-735972722491",
    "hqr.common.database.module.kojitechs.tf",
    "kojibello.com",
    "kojitechs.aws.eks.with.terraform.tf",
    "kojitechs.github.organizatio"
]

class S3Object:

    def list_all_buckets(self, bucket_name):
        """This method list all buckets in aws account
        paramter: bucket_name: (list)
        Return: None
        """
        self.bucket_name = bucket_name  # this variable can be used in all method 
        for each_bucket in self.bucket_name:
            print(f"\t{each_bucket}")
        return None    
            
    def create_bucket(self,name):
        self.name = name # init parameter 
        print(f"creating bucket with name: {self.bucket_name}")  
        self.bucket_name.append(name)
        print(self.bucket_name)
        return None
          

    def list_object_in_buket(self):
        pass
    
    def delete_bucket(self,name):
        print(f"Deleting bucket with name: {self.name}")
        if name in self.bucket_name:
            self.bucket_name.remove(name)
            print(self.bucket_name)
        else:
            print(f"OOOPS.... Bucket doesn't exits with name: {name}")    

        return None  


def main():
    ## initializing class and creating an object
    s3_objects = S3Object()
    s3_objects.list_all_buckets(my_buckets)

    # create new bucket 
    s3_objects.create_bucket("newbucket")

    ## Delete a bucket
    s3_objects.delete_bucket("newbucket")
  

if __name__ == "__main__":
    main()


