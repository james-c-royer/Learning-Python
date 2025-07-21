class Student:

    # automatically called when an object of type Student
    # is declared
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    # defines what "equals" is for student objects. If
    # we check if student1 == student2, it will return
    # T/F depending on if the names are the same
    def __eq__ (self, other):
        return self.name == other.name
    
    # by default, printing an object returns its memory address
    # defining str changes what happens when it is printed 
    def __str__(self):
        return f"I am {self.name} and my GPA is {self.gpa}"
    
    # defines greater than (>)
    def __gt__(self, other):
        return(self.gpa > other.gpa)
    
    # defines indexing an  object. Without a definition,
    # this would return a TypeError 
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "gpa" or "GPA":
            return self.gpa
        else:
            return f"{key} not found in the object"
        
    # other dunder methods can be found at:
    # https://realpython.com/python-magic-methods/
    
student1 = Student("Stacy", 3.2)
student2 = Student("Stacy", 3)

print(student1 == student2) # True
print(student1) # I am Stacy and my GPA is 3.2
print(student2 > student1) # False
print(student1["name"]) # Stacy