```python
def fn(n):
    result = (n*(n+1))/2
    return result


n = int(input("The vlaue of a: "))
res1 = fn(n)
print(res1)

n = int(input("The vlaue of a: "))
res2 = fn(n)
print(res2)
```

    The vlaue of a:  5
    

    15.0
    

    The vlaue of a:  10
    

    55.0
    


```python
# call by value & reference
# when you pass a variable with 
#       (int, float, bool, complex, string, tuple)
# it will pass as call by value
# for mutable types like ( list, dict, set )
#   it will pass as call by ref

# call by value eg.
def fn(a,b):
    a = 100
    b = 200
    print(f"inside fn {a} and {b}")

x,y = 10,20
print(f"outside before {x} and {y}")
fn(x,y)
print(f"outside after {x} and {y}")



```

    outside before 10 and 20
    inside fn 100 and 200
    outside after 10 and 20
    


```python

# call by ref eg
def fn(li):
    li[0] = 1200
    print(li)

item = [10,20,30]
fn(item)
print(item)
```

    [1200, 20, 30]
    [1200, 20, 30]
    


```python
# return 
# if func, not return anything, default it returns None.

def fn(x): print(x%2)
r = fn(10)
print(r)
```

    0
    None
    


```python
# types of arguments
def fn(x,y):  # func definition
    print(x,y)

# fn() # ERROR
# [😄] positional argument
# fn(10) # ERROR  y value send panala
fn(10,20)    # valid:   10 20
# [😄] keyword argument
fn(10,y=20)   # valid:   10 20
fn(y=20,x=30) # valid:   30 20  
# fn(10,x=20,y=30) # invalid assign multi value to param x
# fn(y=10,20)      #  invalid
```

    10 20
    10 20
    30 20
    


```python
# types of parameters
# a -> normal parameter or non-default-parameter ( positional arg )
# b -> default parameter 
def fn(a,b = 20): print(a,b)
# def fn(a = 10,b): print(a,b)   # invalid

fn(10)
fn(10,30)
```

    10 20
    10 30
    


```python
def fn(a,b=30,c=40,d=50): print(a,b,c,d)
# fn() # ERROR
fn(3)
fn(a=30)
# fn(b=123123) # ERROR
fn(d=123123,a=2)
```

    3 30 40 50
    30 30 40 50
    2 30 40 123123
    


```python
# > arbitrary argument
#     1. variable argument           stores as tuple
#     2. variable keyword argument   stores as dict
#  (*a)  when you want to accept n no of positional argument
#  (**b) when you want to accept n no of keyword argument
#  In a func def, only one var-arg and keyword-arg should be there. 
#  Always var-arg then keyword-arg.

def fn(*a, **b):
    print(a,b)
fn()
fn(10)
fn(1,2)
fn(1,2,3,4,4)
fn(10,20,30,a=10,b=20,c=30)
```

    () {}
    (10,) {}
    (1, 2) {}
    (1, 2, 3, 4, 4) {}
    (10, 20, 30) {'a': 10, 'b': 20, 'c': 30}
    


```python
def fn(a,b,*c,**d): print(a,b,c,d)
# fn() # error a no value
# fn(1) # error b no value
fn(1,2) # 1 2 () {}
fn(1,2,3)
fn(1,2,3,4)
# fn(1,2,3,4,a=10) # ERROR
fn(1,2,3,4,c=10,d=20) # 1 2 (3,4) {'c':10,'d':20}
```

    1 2 () {}
    1 2 (3,) {}
    1 2 (3, 4) {}
    1 2 (3, 4) {'c': 10, 'd': 20}
    


```python
# packing and unpacking in func

# unpacking 
#  mult variables = sequence type ( left and right value count should match) 
a,b,c = "hai"
# a,b,c,d = "hai" # ERROR
x,y = 10,20
a,b,c = [10,20,30]
a,b,c = {10,20,30}
```


```python
# packing
# using * we can do unpacking
bag1 = [10,20,30]
bag2 = [40,50]
new_bag = [*bag1, *bag2] # unpack
print(new_bag)
```

    [[10, 20, 30], [40, 50]]
    


```python
def fn(a,b,c=3,d=4,*e,**f):
    print(a,b,c,d,e,f)
# packing
fn( *[10,20,30,40,50] ) 
# fn(10,20,30,40,50)
fn(*[10,20], *[30,40,50])
# fn(10,20,30,40,50)
fn(*[10,20], *[30,40,50], **{'sep':'-','end':'\n'})
# fn(10,20,30,40,50,sep='-',end='\n')
```

    10 20 30 40 (50,) {}
    10 20 30 40 (50,) {}
    10 20 30 40 (50,) {'sep': '-', 'end': '\n'}
    


```python
# unpacking in func
def fn():
    return 10,20,30,40

a,b,c,d = fn()
```


```python
# recursion
# sum of n number
def fn(n):
    if n==1:
        return 1
    return n + fn(n-1)
fn(5)
```




    15




```python
def fn(n,a):
    if n<a:
        return a
    if n==2:
        return n
    return (n+a) + fn(n-1,a)

fn(5,1) # 17 ?
```




    17




```python
def fn(a,b):
    if b==1:
        return 1
    return a + b + fn(a+1,b-1) + fn(a,b-1)

fn(5,3) # 27 ?
```




    27




```python
def fn(n):
    # base case
    if n==0:
        return 0
    if n%2==0:
        return n + fn(n-2)
    else:
        return n + fn(n-1)
fn(10) # 30
fn(5)
```




    11




```python

```
