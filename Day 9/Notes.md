## 1- What I Have Learned:

### Conditionals
- Conditionals allow your program to make decisions based on whether a condition is `True` or `False`.

| Operator | Meaning | Example |
|----------|---------|---------|
| `>` | Greater than | `10 > 5` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<` | Less than | `3 < 7` |
| `<=` | Less than or equal to | `4 <= 6` |
| `==` | Equal to | `8 == 8` |
| `!=` | Not equal to | `9 != 8` |

---

### if:
- if: is a conditional statement that lets your program make a decision.

**Example:**

    if x > y:
        print("x is bigger than y")



### elif
- elif: checks another condition if the previous condition was False.

**Example:**

    if x > y:
        print("x is bigger than y")
    elif x < y:
        print("x is less than y")


---

### else:
- else: runs if none of the previous conditions are True.

**Example:**

    if x > y:
        print("x is bigger than y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is equal to y")



### or:
- or: checks multiple conditions. If **at least one** condition is True, the result is True.

**Example:**

    if x > y or x < y:
        print("x is not equal to y")
    else:
        print("x is equal to y")



### And:
- and: checks multiple conditions. **All** conditions must be True for the result to be True.

**Example:**

    if x > y and x < y:
        print("x is not equal to y")
    else:
        print("x is equal to y")