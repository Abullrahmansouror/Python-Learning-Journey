## Notes for Day 4 of learning pyhton ##

## 1- What I have learned :

**Exception**
- Exception: is an error that happens while the program is running.
Example:
    print("hello, world)
    output: SyntaxError: unterminated string literal


**SyntaxError**
- SyntaxError happens when you write Python code incorrectly.
Example:
    if x == 5
    print("x equals 5")
    output: SyntaxError. ## Because I'm don't write the ":".


**ValueError**
- ValueError happens when the value is the wrong type for an operation.
Example: 
    age = int("hello")
    output: ValueError ## Bescause "hello" is a string can't convert into int.

**try and except**
- I use this "try" + "except" to Handle invalid user input using try and except.
Example: 
    try:
        x = int(input("What's x? "))
        print("x is:", x)
    except ValueError:
        print("x is not a int")


**NameError**
- NameError: happens when you use a variable that doesn't exist.
Example: 
    print(username)
    output: NameError  ## Because I'm not use a variable "number".


**else**
- else: Runs only if the try block finishes without any exception (error).
Example:
    try:
    age = int(input("What's your age? "))
        except ValueError:
        print("Please try again!")
    else: 
        print("This is your age : ", age)


## 2- Time Spent :
- Learning: 50 min
- Practice: 1 h

## 3- Helpful Resources :
https://youtu.be/LW7g1169v7w?si=kneJlYgXram9qiIY