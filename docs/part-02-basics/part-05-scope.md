# scope of variables in python

- local scope
  - This refers to variables defined within a function or a block of code. These variables are only accessible from within that specific function or block.
- global scope
  - Variables defined at the top level of a script or module, outside of any function or class, reside in the global scope. They are accessible throughout the entire program.

```python

print("start of code")
val = input("input 1:")

def fn():
    # print last element
    li = [ x for x in range(10_00_00_000) ]
    print("the last value",li[-1])
    # The above code will take around 800 MB space.
    # as it is declared inside function.
    # it act as a local variable. So it will consume RAM only on its execution
fn()
# Once after function logic is executed.
# The memory used to run the logic inside function will
# get removed from memory.

val = input("input 2:")
print("end of code")
```

```python
# scope

x = 100

def fn():
 global x
 x = 200
 print('inside fn ',x)

fn()
print("outside fn ",x) # 200
```

---

## `nonlocal` keyword

The `nonlocal` keyword in Python is used within nested functions to explicitly declare that a variable refers to a variable in the nearest enclosing (non-global) scope, rather than creating a new local variable within the inner function.

### Specific use cases for `nonlocal`

- **Modifying variables in an outer function's scope from an inner function**: This is the primary purpose of `nonlocal`. When you have a variable defined in an outer function, and you want to modify its value from within a nested function, `nonlocal` is required. Without it, Python would create a new local variable with the same name in the inner function's scope, leaving the outer function's variable unchanged.

```python
    def outer_function():
        count = 0  # Variable in the outer function's scope

        def inner_function():
            nonlocal count  # Declare 'count' as nonlocal
            count += 1
            print(f"Inner function count: {count}")

        inner_function()
        print(f"Outer function count: {count}")

    outer_function()
```

- **Implementing closures with mutable state**: nonlocal is crucial for closures where the inner function needs to maintain or update a state that resides in its enclosing scope. This allows for patterns like counters or accumulators.

```python
    def make_counter():
        count = 0

        def counter():
            nonlocal count
            count += 1
            return count
        return counter

    my_counter = make_counter()
    print(my_counter()) # Output: 1
    print(my_counter()) # Output: 2
```

- **Distinguishing between local and enclosing scope variables with the same name**: If an inner function has a variable with the same name as a variable in an enclosing scope, nonlocal clarifies that you intend to interact with the enclosing scope's variable.

### When NOT to use `nonlocal`:

#### Global variables:

- If you need to modify a variable in the global scope, use the global keyword instead of nonlocal. nonlocal specifically targets non-global enclosing scopes.
- Creating new local variables:
- If you intend to create a new variable that is local only to the inner function, do not use nonlocal. Simply assign a value to the variable name, and it will be treated as local by default.
