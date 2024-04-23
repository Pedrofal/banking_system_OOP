class Person():
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age 
    
    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

