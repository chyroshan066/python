# In order to make a class completely abstract we need to import two methods which are
from abc import ABC, abstractmethod

class Computer(ABC):  # It is abstract class because it only has abstract methods
    @abstractmethod
    def process(self):  # It is abstract method since it only has declaration but not any definition
        pass

class Laptop(Computer):
    def process(self):
        print("It's running")

com = Laptop()  # We can't instantiate abstract class
com.process()