# Decorators

- In Python, a decorator is a concept that used to add new functionality to an existing function without modifying source-code.
- Some times, it can be used to update class functionality also.

```python
def validate_zero(fn):
    def validate(x,y):
        if y==0:
            return float('inf')
        return fn(x,y)
    return validate
    
@validate_zero
def div(x,y):
    return x/y
```

- Here by default in python, if we do val divide by zero, we will get an ZeroDivisionError.
- Mathematically anything divided by zero suppose to give infinity.
- So here We are giving additional functionality to division function.
- For that we are using a python concept called decorators.

```python
# def smart_div(fn):
#     def update(a):
#         if a==0:
#             print("0 div not possible")
#         else:
#             print(fn(a,2))
#     return update

# # @smart_div
# def div(a,b):
#     return a/b

# smart_div(div)(4,2)

def bread(fn):
    def bread_layer():
        print("bread 1")
        fn()
        print("bread 2")
    return bread_layer

def cheese(fn):
    def cheese_layer():
        print("cheese 1")
        fn()
        print("cheese 2")
    return cheese_layer

# # p1 = bread(p1)
# @bread
# def p1():
#     print("potato")

# # p2 = cheese(p2)
# @cheese
# def p2():
#     print(" potato")

# this below code changes to
# bread(cheese(p3))
@bread
@cheese
def p3():
    print("potato")

print("initiated")
p3()

# bread(cheese(p3))()
# p1() # bread(p1)()

# p2() # cheese(p2)()
```