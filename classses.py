class Employee:
    def __init__(self, first, last, pay): #how to init classes, always make self first because convention, then put all the variables you want the user to have to enter. this is the method to init classses
        self.first = first #now you equate these variables to things in the class
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self): #now we have a new method to ge the full name of a user
        return(f"{self.first} {self.last}") #here we use self so it apples ot all ionstances
    def __str__(self):
        return f"Employee {self.first} {self.last} has been performing satisfactorily. If you have any complaints, email them at {self.email}"


emp1 = Employee("jada", "dixon", 34343) #here we make an instanve of a class
# print(emp1)

class Car:
    def __init__(self, colour, miles):
        self.colour = colour
        self.miles = miles
    
    def car_info(self):
        return f"The {self.colour} car has {self.miles} miles"

    def drive(self, distance): #adds a given distance to the mileage
        
        self.miles = self.miles + distance
        
        return f"The {self.colour} car has travelled {distance} miles on this drive. The new mileage is {self.miles} miles. "
       

class Baby:
    def __init__(self, weight, sex):
        self.sex = sex 
        self.weight = weight

car1 = Car('burgundy', 23423488238)
car2 = Car('chartreuse', 99999)
car3 = Car("teal", 2)
print(car3.drive(122))