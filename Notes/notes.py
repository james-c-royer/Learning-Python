class Animal():
    pass

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# fish hunt other fish, but are also preyed upon
class Fish(Prey, Predator):
    pass