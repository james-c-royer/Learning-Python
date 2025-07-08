class Student:
    # class variables covers things that apply to every object
    classYear = 2025
    num_students = 0

    # instance variables cover things unique to each object
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # increments class variable whenever
        # an object is initilized 
        num_students += 1


# good practice to call the class itself when accessing a 
# class variables, rather than a specific class object
print(Student.classYear) # 2025
print(Student.num_students)
 