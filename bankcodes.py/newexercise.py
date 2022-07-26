# def generate_pin():
#     number="0123456789"
#     whole="0"
#     string= whole + number
#     length= 4
#     account= "".join(random.sample(string, length))
#     pin = whole + account
#     token = pin
#     return token

# transaction_pin= generate_pin()


#A METHOD IS AFUNCTION THAT GOES INSIDE OF A CLASS. 


# print(type(6))



# def hello():
#     print("hello")


# print(type(hello))


# class Example:
#     def __init__(self,name, age):
#         self.name= name #this is an attribute
#         self.age = age
        



#     def add_one(self, x):
#         return (x + 1)


    

#     def bark(self, name:str):
#         return "wolf dog" #ALTERNATIVE ONE


#     def get_name(self): #ALTERNATIVE TWO
#         return self.name 

#     def get_age(self):
#         return self.age

#     def set_age(self,age):
#         self.age= age
# # d= Example
# # print(d.add_one(6))
# # print(d.bark("tola"))

# d1= Example("wolfie",45) # IT COULD BE PRINTED THIS WAY 
# print(d1.name)

# # d2= Example("oscar", 55)
# # print(d2.name)

# # print(d2.get_name()) # OR THIS WAY
# print(d1.get_age())
# d1.set_age(34)  # this helps to change the given age of the object 

# print(d1.get_age())

# HOW TO USE TWO CLASSES TOGETHER
# class Student:
#     def __init__(self, name:str, age:int, grade:int):
#         self.name = name # attribute are what ever we decide to assign
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade


#     def set_grade(self, grade):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False


#     def get_average(self): # FUNCTION TO GET THE AVERAGE SCORE OF THE STUDENTS
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
            
#         return value / len(self.students)


# call1= Student("gloria", 19, 100)
# call2= Student("fola", 19, 90)
# call3= Student("denfah", 19, 90)


# course = Course("mathematics", 2)
# course.add_student(call1)
# course.add_student(call2)

# print(course.students[0].name)
# print(course.get_average()) #THIS IS THE AVERAGE
# print(course.add_student(call3))
    



#INHERITANCE

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')


    def speak(self):
        print("I am blessed and lifted")

class Dog(Pet):
    '''provides info on the dog class. note this is a subclass for pet'''
    def __inti__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour # why is this not functioning
        
       
    def speak(self):
        print("bark")

    def show(self):
        print(f'I am {self.name}, I am {self.age} years old and I have {self.colour} fur')



class Cat(Pet):

    def speak(self):
        print("meow")



p = Pet("Gloria", 20)
p.show()

c = Cat("Allison", 30)
c.show()

d = Dog("George", 60, "brown")
print(d.show())


# p.speak()
# c.speak()
d.speak()



# class Person:

#     num_of_persons = 0
#     def __init__(self,name):
#         self.name =name
#         Person.add_person()
    
#     @classmethod
#     def num_of_persons1(cls):
#         return cls.num_of_persons

#     @classmethod
#     def add_person(cls):
#         cls.num_of_persons += 1



# dol = Person("jill")
# print(Person.num_of_persons)

# dol2= Person('gloria')
# print(Person.num_of_persons)


# print(Person.num_of_persons1())

# class Math:

#     @staticmethod # this is a method that stays the same, the do not have access to the instance. they do something but they dont change something
#     def math(x):
#         return x + 6

#     @staticmethod 
#     def pr():
#         print("run")


# print(Math.math(4))

# Math.pr()