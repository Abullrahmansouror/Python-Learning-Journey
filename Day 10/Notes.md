## 1- What I Have Learned:

### Loop:
- Loop: A loop repeats a block of code multiple times. Also Loops save time and reduce repeated code.
Example:
    print("Hello")
    print("Hello")
    print("Hello")

    You can write:

    for i in range(3):
        print("Hello")


### For loop:
- for loop: A for loop repeats a block of code a specific number of times or for each item in a sequence.
Example:
    for i in range(5):
    print(i)


### range():
- range() generates a sequence of numbers.
- It is commonly used with a `for` loop.
- The **stop** number is **not included**.

Example:
for i in range(5):
    print(i)


Output:

0
1
2
3
4


Example:
for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5

**range(start, stop, step)**
  - `start` → Start counting from this number.
  - `stop` → Stop **before** this number.
  - `step` → Increase by this value each time.

Example:
for i in range(5, 16, 5):
    print(i)

output:
5
10
15


### Loop Through a List
Example:
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

Output:

Apple
Banana
Orange




### while:
while Loop : A while loop repeats a block of code as long as a condition is True.
Syntax:

while condition:
    # Code to repeat

Example:
count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5


> 💡 Remember:
> - The condition is checked before each repetition.
> - Update the variable inside the loop (e.g., `count += 1`) to avoid an infinite loop.








## 2- Time Spent:
- Learning: 
- Practice: 

## 3- Resources:
CS50 course 2022 | Introduction to Porgraming with Python.
- Lecture 2: https://youtu.be/OvKCESUCWII?si=lnx_0SOsTNRlKVat
- Chat GPT