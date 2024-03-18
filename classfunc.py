class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        introduction = f"Hello, my name is {self.name} from Lagos, Nigeria. " \
                       f"I am {self.age} years old and I am an Alpha {self.gender}."
        print(introduction)

# Creating the instance of the Person class
person1 = Person("Anuoluwa Gboyega", 21, "male")

# Calling the introduce method to display the my informations.
person1.introduce()
