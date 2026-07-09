## Notes for Day 8 of learning pyhton

## 1- What I have learned: 

### Functions:
- A function is a block of code that does a specific task.

**input**
- input: It's a function that gets input from the user and returns it as a string.
Example:
    # Here is the function is "input"
    age = input("How old are you? ")

**print**
- print: Is a function that displays output on the screen.
Example:
    # Here I'm use print function to print any thing between ""
    print("Hello, world!")


### String Methods:
- A function that belongs to a string and performs an operation on it.

    name = name.strip()             # Remove whitespace from both sides
    name = name.lstrip()            # Remove whitespace from the left
    name = name.rstrip()            # Remove whitespace from the right
    name = name.lower()             # Convert to lowercase
    name = name.upper()             # Convert to uppercase
    name = name.capitalize()        # Capitalize the first letter
    name = name.title()             # Capitalize the first letter of each word
    name = name.replace("a", "b")   # Replace one substring with another
    words = name.split()            # Split the string into a list of words
    result = name.startswith("A")   # Check if the string starts with "A"
    result = name.endswith("z")     # Check if the string ends with "z"

also I can write it in short way:
    name = name.strip().capitalize().title() # Make all the styles in one line
                                    **Or**
    name = input("What's your name? ").strip().title()


### Defining Functions
- Defining Functions: used to create your own function.
Example:

def age():
    print("How old are you?")

    age()    # Calls the function


### Parameter:
- A variable in a function that receives a value.
**sep**
- Separator: It specifies what is printed between multiple objects in print().
It only works when the objects are separated with commas ,, not when they are joined with +.
Example:
    # Use the 'sep' parameter to display "-" between the printed values
    print("word1", "word2", sep="-")
    output: word1-word2

**end**
- End: It specifies what is printed at the end of the output.
Example:
    # 'end' sets what is printed after the output (default is a new line)
    print("word1", "word2", end="\n")
    output: word1 word2


### Variabels:
- A variable is a name that I can stores a value and return it when I need it.
Example:
    # The variable here is "name"
    name = input("What's your name? ")


### str:
- String: A built-in type for storing text.
Example:
    # This is a string (text). It should be inside quotes.
    print("This is a string")


### int:
- Integer: A built-in type for storing whole numbers.

Example:
    # This is an integer (whole number).
    print(4)
                    **Also**
    # Convert the user's input from a string to an integer.
    age = int(input("What's your age? "))


### float:
- Float: A built-in type for storing decimal numbers.
Example:
    # This is a float (decimal number).
    print(3.14)




## 2- Time Spent:
- Learning: 
- Practice: 

## 3- Resources:
CS50 course 2022 | Introduction to Porgraming with Python.
Lecture 0: https://youtu.be/JP7ITIXGpHk?si=z5qJMjQygppNuzXN