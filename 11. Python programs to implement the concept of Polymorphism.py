#11. Python programs to implement the concept of Polymorphism.

# Define a class 'Bird'
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


# Define a class 'Sparrow' that inherits from the 'Bird' class
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


# Define a class 'Ostrich' that inherits from the 'Bird' class
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


# Create instances of each class
obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

# Call methods
obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
