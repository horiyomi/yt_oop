from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width )



# rectangle = Rectangle(5, 4)

# print(rectangle.area())
# print(rectangle.perimeter())


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length ** 4


square = Square(4)

print(square.area())

print(square.perimeter())



















# class Animal:
    
#     def __init__(self, name):
#         self.name = name

#     def feed(self):
#         print(f"{self.name} is fed")


# animal = Animal("Dog")

# name = animal.name

# feed = animal.feed()

# # Inheritance
# """
# `class` Dog  inherits from the parent class Animal
# """
# # class Dog(Animal):
    
# #     def bark(self):
# #         print(f"{self.name} is barking...woof woof")


# # dog = Dog("Chiwawa")

# # print(dog.name)

# # dog.feed()

# # dog.bark()

# # Inheritance
# """
# `class` Cat  inherits from the parent class Animal
# """
# # class Cat(Animal):

# #     def cry(self):
# #         print(f"{self.name} is crying meow")

# # cat = Cat(name="Musu")
# # cat.feed()
# # cat.cry()


# class Lion(Animal):

#     def __init__(self, name, color):
#         self.color = color
#         super().__init__(name=name)

#     def feed(self, meal):
#         print(f"{self.name} ate {meal}")
#         super().feed()

# lion = Lion(name="Leo", color="Brown")

# print(lion.name)
# print(lion.color)

# lion.feed("Goat")