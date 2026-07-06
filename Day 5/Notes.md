## Notes for Day 5 of learning pyhton ##

## 1- What I have learned :
**import**
- The import keyword in Python is used to bring code from another module or library into your current program so you can use it.
Exemple:
    import random

    pet = random.choice(["Cat", "Dog", "Rabbit", "Fish"])
    print("Your pet is: ", pet)


**From**
- From: keyword in Python is used to import specific parts (such as functions, classes, or variables) from a module instead of importing the entire module.
Exemple:
    from random import choice # using "from" used to import specific parts.

    pet = choice(["Cat", "Dog", "Rabbit", "Fish"])
    print("Your pet is: ", pet)


**random.choice**
- Picks one random item from a list.
Example: 
    fruit = random.choice(["Apple", "Orange", "Kiwi"])
    print(fruit)

**random.randint**
- Generates a random integer between two numbers (inclusive).
Example: 
    number = random.randint(1, 10)
    print(number)


**random.shuffle**
- Shuffles: can Shuffle the items in deferent order. Like Uno cards when we play we shuffle it.
Example: 
    import random
    cards = ["Jack", "Queen", "King"]
    random.shuffle(cards)
    print(cards)



**statistics.mean**
- print the avarege of numbers.
Example:
    import statistics

    print(statistics.mean({x, y}))


## 2- Time Spent :
- Learning: 1 h
- Practice: 50 min