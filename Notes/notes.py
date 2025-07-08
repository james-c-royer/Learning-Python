from class import Car


# calling the initilizer function -- self is provided behind
# the scenes
car1 = Car("Saturn Aura", 2009, "Silver", False)

# print(car1) would give you memory address of the car

print(car1.model) # this is how you print specific attributes

# calling methods
car1.drive()
car1.stop()