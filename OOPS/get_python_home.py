#! /bin/python3
import os 


"""

def get_all_python(search_app):
    list_of_config_file = []
    for r, d , f in os.walk("/"):
        for each_file in f:
            if each_file == search_app:
                list_of_config_file.append(os.path.join(r,each_file))
    return list_of_config_file


def main():
    print("Finding list of python....")
    path = "python"
    list_of_python = get_all_python(path) 
    # print(list_of_python)
    for each_config_file in list_of_python:
        print('postgres home is: ', os.path.dirname(os.path.dirname(each_config_file)))
        print("Postgres config file: ",each_config_file)
    return None

""" 

class PythonHome(object):

    def __init__(self, home):
        self.search_home = os.path.dirname(os.path.dirname(home))
        self.search_confi_file = home
        return None

    def get_all_home(self):
        list_of_python = []
        for r,d,f in os.walk("/"):
            for each_file in f:
                if each_file == self.search_confi_file:
                    list_of_python.append(os.path.join(r,each_file))
        return list_of_python       

    def display(self):
        python_object = []
        print(f"Finding list of {self.search_confi_file}: ")
        list_of_python = self.get_all_home()
        for each_file in list_of_python:
            print(each_file)
        return None
        
def main():
    path = "postgres"
    
    python_pbject = PythonHome(path)
    objects = python_pbject.get_all_home()
    python_pbject.display()



if __name__ == '__main__':
    main()


