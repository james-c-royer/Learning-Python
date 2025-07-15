# static method declaration
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # this is an instance method used to return an
    # employee's name and position attributes
    def get_info(self):
        return f"{self.name}, {self.position}"
    
    # declaration of a static method
    @staticmethod
    # does not use self because it does not check an object
    def is_valid_position(position):
        valid_positions = ["Cook", "Cashier", "Manager", "Janitor"]
        return position in valid_positions

# accessing static method
print(Employee.is_valid_position("Cook")) # True

