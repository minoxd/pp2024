import numpy as np


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 22)

# Creating a list of objects
people_list = [person1, person2, person3]

# Converting the list of objects to a NumPy array
people_array = np.array(people_list, dtype=object)

# Sorting the array based on the 'age' attribute
sorted_indices = np.argsort([person.age for person in people_array])

# Creating a sorted list of objects
sorted_people_list = people_array[sorted_indices]

# Accessing objects in the sorted list
for person in sorted_people_list:
    print(f"{person.name} is {person.age} years old.")

a = 1
a += 2
print(a)
