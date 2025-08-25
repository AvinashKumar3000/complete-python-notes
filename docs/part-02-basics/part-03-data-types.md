# `Data types`

```md
     Data types
       /      \

Numberic string datatype
/ \
int str
float
bool
complex
```

- Numeric type basics is enough for problem solving
- In case of strings
  - usage of single, double and triple quotes
  - freq used method is : `.format()`
  - and `.split()` which is used while getting input values.
  - `"hello"*3` for multiplying strings.

```python
>>> print("Hello my name is {}.".format('doremon'))
```

## int

    >>> amount = 1,00,000 # stored as tuple
    >>> amount = 1_00_000 # stored as int

Here \_ is used to make int readable.

    >>> b = _12 here _12 is not defined
    >>> 0000 valid
    >>> 0001 invalid
    >>> 01 invalid
    >>> leading zero not permitted.

- number system in python int.
- we have to prefix with following
- 0b binary eg: 0b1010 (10)
- 0o or 0O octal eg: 0o11 (9)
- 0x or 0X hexadecimal eg: 0xA (10)
- without any prefix is decimal

## float:

```python
>>> .             # invalid
>>> .1            # valid
>>> 0.1           # valid
>>> 1.
>>> 1.0           # valid
>>> 2.
>>> 0.0           # valid
>>> 3.
>>> 1.0           # valid
>>> 4.
>>> 0.0           # valid
>>> speed = 3e8   # here e is used in float type.
>>> # where 'e' is exponential ( e = 10 to the power )
>>> # In above example `3e8` is `3*10 to the power of 8`.
>>> 2*3.0         # where * is supported.
```

## bool

`True` , `False`

```python

>>> True
True
>>> True + True
2
# why ? internally True is 1 and False is 0
# where ever bool is applied on calculation.
```

## EXTRA NOTES :

- `0b`,`0o`,`0x` not available in float type
- 3 keyword in python, that starts with capital letter
- `True`, `False`, `None`

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True',... 'yield']
>>> len(keyword.kwlist)
35
```

## strings

- how to represent strings
  - single quotes
  - double quotes
  - triple single quotes
  - triple double quotes
  - raw string
  - format string

```python
>>> val   =   "I don't like maths"
>>> greet =   'always say "thank you" at end'
>>> val   =   'i don't like clg'
# invalid error
# when to use triple quotes ?
# when you have to store multiple lines of string.

para = '''the quick brown
fox jumps over
a lazy do''' # valid

para = 'line
line2
line3' # invalid
```

- what is mean by empty string ?

```python
>>> x = ''
>>> len(x)
0
>>> len("don't")
5
>>> len("a\nb") # here '\n' is a single character.
3
```

## Escape sequence

a special character start with '\'

- `\n` new line
- `\t` tab
- `\'` single quote
- `\"` double quote
- `\\` a single slash as character

```python
>>> x = '\t\\\' invalid
>>> x = '\t\\\''
>>> x[0]
'\t'
>>> x[1]
'\\'
>>> x[2]
"'"
>>> a = str()
# Empty sting is stored in a, '' which is empty string
```

string is immutable ?
prove it ?

```python
>>> x = "abc"
>>> x[0]
'a'
>>> x[0] = 'z'
# ERROR
```

- string is sequence type.
- ( it hold more than one value )

## copy / referencing

### accessing

- indexing [0]
- slicing [start:stop:step]

### `NOTE`

- delete within and modify within is not possible in string as it is immutable.

### string access ( indexing )

```python
>>> a = 'abcde'
>>> a[0]
'a'
>>> a[-1]
'e'
>>> a[100]
# IndexError: string index out of range
>>> a[1.0]
# TypeError: string indices must be integers
>>> a[True]
'b'
>>> a[False]
'a'
```

### string slicing ([::])

            [ start:  stop  : step ]
    default     0  :        :  1

```python
>>> a = 'abcde'
>>> a[::]
'abcde'
>>> a[::-1]
'edcba'
>>> a[10:1:-1]
'edc'
>>> a[:100]
'abcde'
>>> a[50:100]
''
>>> type(None)
<class 'NoneType'>
>>> a[4:1]
''
>>> a[4:1:-1]
'edc'
```

#### In slicing

- `start` -> inclusive
- `stop` -> exclusive

```python
>>> a = 'abcde'
>>> a[0:3]
abc
>>> a[4:1:-1]
edc
>>> a[::0]
ValueError: slice step cannot be zero
>>> a
'abcde'
>>> a[::100]
'a'
```

    modify is not possible with string
    del is not possible with string
    because it is immutable

```python
>>> a = "hai"
>>> del a
# will delete variable a from memory
>>> a = "hai"
>>> del a[0]
# ERROR: delete is not supported
```

## String operations

`+` will concat 2 strings

```python
>>> x = 'a' + 'b'
>>> x
'ab'
>>> x += 'c'
>>> x
'abc'
>>> 1 + '2'
ERROR
```

`*` multiplies / repeatation

```python
>>> x = 'a' * 4
>>> x
'aaaa'
>>> x = 4 * 'a'
>>> x
'aaaa'
>>> x = 4 + 2 * 'a'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x = (4 + 2) * 'a'
```
