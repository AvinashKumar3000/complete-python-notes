# other operators

## `comparison/relational operators`

- `==` Equal To
- `! =` Not Equal To
- `>` Greater Than
- `<` Less Than
- `>=` Greater Than or Equal To
- `<=`  Lesser Than or Equal To

`NOTE: make sure you understand your relation`

### `logical operators`

- `and`
- `or`
- `not`

```python
>>> 10 and 20 and 0 and 100 and 200
0
>>> 10 and 20 and [] and 20 and (1,2)
[]

# in above cases. It will convert each and every thing into its boolean type then evaluates. Once it stop evaluation it will through the ans. 
# 10 -> bool(10)  -> True
# 20 -> bool(20)  -> True
# [] -> bool([])  -> False
# 20 -> bool(20)  -> True

# As we are using only `and`. Python will stop once it gets 
# False ( bool([]) -> False ).
# so only we got output as `[]`
```

---

### `walrus operator : :=`

```python
a = 0
if a:
    print("true block")
else:
    print("false block")
```

```python
a = 0
if a:=1:
    print("true block")
else:
    print("false block")
```

another use case

```python
def fn(x):
  print(x)

fn(a:=100)
print(a) # 100
```

`ADDITIONAL NOTES`

## REPL

REPL stands for Read-Eval-Print Loop. It is an interactive programming environment that takes user inputs (one at a time), evaluates them, and returns the result to the user. This process is repeated in a loop, hence the name "Read-Eval-Print Loop."

---    

## ternary operator

conditional operator

- `max_val = a if a>b else b`
- if condition is true then max_val = a else max_val = b

nesting if else

```python
a,b,c = 12,2,12
max_val = a if a>=b and a>=c else b if b>=a and b>=c else c 

a,b,c,d = 12,2,12,2
greatest = a 
if b >= greatest:
    greatest = b
if c >= greatest:
    greatest = c
if d >= greatest:
    greatest = d
print(greatest)
```

`NOTE: the above code will follow R->L associativity`
