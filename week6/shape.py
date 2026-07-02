from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, shape_type):
        self.__name = name
        self.__shape_type = shape_type

    @property
    def name(self):
        return self.__name
    
    @property
    def shape_type(self):
        return self.__shape_type
    
    @shape_type.setter
    def shape_type(self, value):
        self.__shape_type = value
    
    
    @property
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.__shape_type} {self.__name} area {self.area:.2f} m2'