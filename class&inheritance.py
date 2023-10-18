class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

class Dog(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.dog_breed = 'German Sherphard'
    def bark(self):
        print(f"{self.name} is barking...")
    def stop(self):
        print(f"{self.name} has stopped barking.")
    
p1 = Person('Kelvin',20)
d1 = Dog("Kamau", 10)
person_name = p1.getName()
person_age = p1.getAge()
dogName = d1.name
dogAge = d1.age
print(f'{person_name}:{person_age} and the dog is {dogName}:{dogAge}')
d1.bark()
d1.stop()