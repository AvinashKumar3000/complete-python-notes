# 🏷️ PATTERN PRINTING 🏷️

## BASICS

```python
# base code
n =  5
for i in range(n):
    for j in range(n):
        print("{}{}".format(i,j),end=" ")
    print()
```

    00 01 02 03 04
    10 11 12 13 14
    20 21 22 23 24
    30 31 32 33 34
    40 41 42 43 44

```python
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j==0:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * *
    *
    *
    *
    *

```python
# other version of code. alternate version of using `or`
n = 5
for i in range(n):
    for j in range(n):
        if i in [0,n//2,n-1] or j in [0,n//2,n-1]:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * *
    *   *   *
    * * * * *
    *   *   *
    * * * * *

```python
# other version of code. alternate version of using `or`
n = 5
for i in range(n-1):
    for j in range(n):
        if i+j >= n-1 and j==n-1-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,n):
        if i >= j and j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("* "*n + "* "*(n-1))
```

            *
          *   *
        *       *
      *           *
    * * * * * * * * *

```python
n = 5
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    *
      *
        *
          *
            *

```python
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    *
    * *
    * * *
    * * * *
    * * * * *

```python
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * *
      * * * *
        * * *
          * *
            *

```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

            *
          *
        *
      *
    *

```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

            *
          * *
        * * *
      * * * *
    * * * * *

```python
n = 5
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
```

    * * * * *
    * * * *
    * * *
    * *
    *

---
