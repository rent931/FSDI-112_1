

## getters and setters
class MyClassA:
    def __init__(self, name="Miguel"):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name 


class MyClassB:
    def __init__(self, age):
        self.age = age 

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

# OOP fundamentals 
# Inheritance 

class MyClassC (MyClassA):    #MyClassC is extending MyClassA
    def __init__(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, lname):
        self.last_name = lname

# Compostion 

class MyClassD: 
    def __init__(self, zip_code, name, last_name, age): #constructors 
        self.name_mgr = MyClassA(name)
        self.last_name_mgr = MyClassC(last_name)
        self.age_mgr = MyClassB(age)
        self.zip_code = zip_code

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code
    def get_zip_code(self):
        return self.zip_code

def main():
    my_class_c = MyClassC('Renteria')   #instance/object Creating an object from a class
    my_class_c.set_name('Miguel')
    print(my_class_c.get_name())

    my_class_d = MyClassD("92101", "Miguel", "Rent", 65)
    print(my_class_d.name_mgr.get_name())
    print(my_class_d.last_name_mgr.get_last_name())
    print(my_class_d.age_mgr.get_age())
    print(my_class_d.get_zip_code())

if __name__ == "__main__":
    main()
