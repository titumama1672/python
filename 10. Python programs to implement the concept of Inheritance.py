#10. Python programs to implement the concept of Inheritance.

class Animal:
    name= " "
    def eat(self):
        print("I can Eat")
class Cat(Animal):
    def display(self):
        print("My Name Is",self.name)
c= Cat()
c.name="Kitty"
c.eat()
c.display()
