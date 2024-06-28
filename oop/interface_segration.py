# Implementing Walkable and Swimable classes, you are given Frog and Giraffe classes which implements the new classes.
# Create abstract class Walkable which has only one abstract function walk(self)
# Create abstract class Swimable which has only one abstract function swim(self)

from abc import ABC, abstractmethod


class Walkable(ABC):
    def walk(self):
        pass


class Swimable(ABC):
    def swim(self):
        pass


class Frog(Walkable, Swimable):
	def walk(self):
		print("Walking")
	
	def swim(self):
		print("Swimming")


class Giraffe(Walkable):
	def walk(self):
		print("Walking")


if __name__ == "__main__":
	animal_type = input()
	if animal_type == "frog":
		animal = Frog()
		animal.walk()
		animal.swim()
	elif animal_type == "giraffe":
		animal = Giraffe()
		animal.walk()
		print("not Swimming")
			