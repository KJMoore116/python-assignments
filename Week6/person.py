"""Module providing a function printing python version."""
# person.py

class Person:
    """Class representing a person object with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the instance with the arguments passed to the constructor.
        
        Parameters:
        first_name (str): The first name of the person.
        last_name (str) The last name of the person.
        age (int): The age of the person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def isMinor(self):
        """Determine if the person is a minor (under 18)."""
        return self.age < 18
    
## Test Code
from person import Person

people_list =  [Person('Robert', 'Johnson', 15), 
                Person('Bob', 'Robby', 18),
                Person('John', 'Smith', 25)]

for x in people_list:
    age_desc = 'Adult'
    if x.isMinor(): age_desc = 'Minor'
    print(f"{x.first_name} {x.last_name} is a {age_desc}")