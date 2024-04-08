#creating a class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#creating method introduce

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of Person
person1 = Person("Juma", 25, "male")

# Call the introduce method to display the person's information
person1.introduce()
