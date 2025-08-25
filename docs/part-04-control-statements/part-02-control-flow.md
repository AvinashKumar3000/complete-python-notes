# control flow statements

## flow control

1. while
1. for
1. break, continue
1. match case

### `while`

| Feature                | `for` Loop                                           | `while` Loop                                                              |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------- |
| **Purpose**            | Iterates over a sequence (e.g., list, tuple, string) | Repeats as long as a condition is true                                    |
| **Syntax**             | `for item in sequence:`                              | `while condition:`                                                        |
| **Use Case**           | When the number of iterations is known or finite     | When the number of iterations is not known or is dependent on a condition |
| **Initialization**     | Automatically takes the first item from the sequence | Must initialize variables before the loop                                 |
| **Condition**          | Implicitly checks for the end of the sequence        | Explicit condition is checked each iteration                              |
| **Iteration**          | Automatically moves to the next item in the sequence | Must manually update variables within the loop                            |
| **Example**            | `for i in range(5):`<br>`print(i)`                   | `i = 0`<br>`while i < 5:`<br>`print(i)`<br>`i += 1`                       |
| **Break and Continue** | Supports `break` and `continue` statements           | Supports `break` and `continue` statements                                |
| **Readability**        | Often more readable for simple iterations            | May be less readable if the condition or updates are complex              |

```python
# the basic concept of while
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("The while loop has completed without a break.")

# --------------------------------------------------------------

count = 0

while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        print("Breaking out of the loop.")
        break
else:
    print("The while loop has completed without a break.")

# --------------------------------------------------------------

s1 = "BYTS"
n = len(s1)
i = 0
while i<n:
    print(s[i])
    i = i + 1

```

### `for`

```python

li = [1,2,3,4,5]
for x in li:
    print(x)

# ------------------------------------------------------

li = [1,2,3,4,5]

for i in range(len(li)):
    print(li[i])

# ------------------------------------------------------
my_list = ['apple', 'banana', 'cherry', 'date']

# Using enumerate to get index and item
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")
# ------------------------------------------------------

```

### `match case`

```python
# program to find exam grading system

grade = input() # A B C D E

def fn(grade):
    match grade:
        case "A":
            print("very good")
        case "B":
            print("good")
        case "C":
            print("average")
        case "D":
            print("below average")
        case "E":
            print("poor")
        case _:
            print("invalid grade")

```

```python
# a combination of while with else.
# else will execute only if loop ends.
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        print("Breaking out of the loop.")
        break
else:
    print("The while loop has completed without a break.")
```

```python
for i in range(20):
    print(i,end=" ")
    if i == 10:
        break
else:
    # this will execute only if for loop condition fails
    print("end of for loop")
    # now in output you won't see this line.
    # because as break statement will be executed first.
```
