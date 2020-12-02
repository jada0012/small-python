print(type('Hello'))

# x is an object, strings, classes, functions, etc. everything is an object 
#when you do string,upper, its a method. things you can do with objects are based on the classes

class Dog:
    def __init__(self, name, age):
        self.name = name #attribute of the class doge
        self.age = age

    def add_one(self, x):
        return x+1

    def bark(self): #method = function in a class
        print('bark')
    
    def get_name(self):#the first argument alwasy has to be self so we can pass the do object to kno wthe dog we're acessing 
        return self.name
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Jorg", 14) #creatin a new instance of the class dog
d2 = Dog("Fran", 99)
# d.bark()
# print(d.get_age())
# print(d2.get_age())


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []


    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)


s1 = Student('Fredward', 13, 88)
s2 = Student('Rebeccason', 18, 66)
s3 = Student('Pamothy', 16, 94)

course = Course('Econ', 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
# print(course.get_avg_grade())
class Pet:
    def __init__(self, name , age):
       self.name = name
       self.age = age
    def show(self):
        print(f"I am {self.name} and I an {self.age} years old")
   
        

   
    
class Cat(Pet):
   
    def speak(self):
        print('meow')
class Dogg(Pet):
    def speak(self):
        print('bark')
p = Pet('arandol', 19)
p.show()




