# string methods

`dir(object)`` : list all available methods and
variables inside the object

## Helper and Formatting Methods

- `casefold` : used when doing caseless comparison the character will align at center
- `count` : count the character that u passed.
- `encode` : used to encode in any format.
- `decode` : used to decode in encoded format.
- `expandtabs` : set tab size.
- `format` : used to format a string
- `zfill(width)` : fill numeric string with zero.

## comparison

- `isascii` : return True if all chars are ASCII ( codepoint < 128 )
- `isidentifier` : return True if string is valid variable name.
- `isprintable` : return True if all chars are printable
- `isspace` : return True if all chars are space
- `islower` : return True if all chars are lower case
- `istitle` : return True if all first letter of each word is caps.
- `isupper` : return True if all chars are upper case.
- `isalpha` : return True if all chars are alphabets `"python3".isalpha()  False`
- `isalnum` : return True if all chars are alphameric `"Python 3".isalnum() False` space is not alphanum.
- `isnumeric` : return True if all chars are numeric have more items than isdigit. it includes Roman numeral, fractions
- `isdigit` : return True if all chars are digit check 0-9, super script's unicode
- `isdecimal` : return True if all chars are check only 0-9,

## align

- `ljust(width)` : left align
- `center(width)` : center align
- `rjust(width)` : right align

## case conversion

- `lower` : converts to lower case
- `capitalize` : converts to capital and returns
- `upper` : converts to upper case
- `title` : converts to title case
- `swapcase` : upper 2 lower and vice versa

## cleaning process

- `strip` : remove spaces on left and right
- `lstrip` : remove spaces from left
- `rstrip` : remove spaces from right
- `removeprefix` : remove specified prefix string
- `removesuffix` : remove specified suffix string

## search and find

- `find` : find substring and return its position index.
- `index` : find substring and return its position index.
- `rfind` : find in reverse
- `rindex` : find in reverse
- `replace` : replace the string where it found
- `startswith` : checks if string starts with specified
- `endswith`: checks if string ends with specified

`NOTE: index, rindex will raise ValueError on not found.`

## split and join

- `partition` : split into 2 parts
- `rpartition` : split into 2 parts but search from last
- `split` : Splits a string into a list
- `rsplit` : Splits in reverse order
- `splitlines` : Splits a string into a list of lines,
- `join(li)` : join the string list.

```python 
>>> "-".join(['neni','bochan','shinchan'])
neni-bochan-shinchan`
```
    
```python
>>> "a\tb".expandtabs(10)
'a b'
>>> "123".zfill(5)
'00123'
>>> "👏".isascii()
False
>>> "A".isascii()
True
>>> "<".isascii()
True
>>> "\_123".isidentifier()
True
>>> "123a".isidentifier()
False
>>> "\n".isprintable()
False
>>> "\t".isprintable()
False
>>> "😄".isprintable()
True
>>> "".isspace()
False
>>> " ".isspace()
True
>>> " a".isspace()
False
>>> " ".isspace()
True
>>> "This Is My Day #".istitle()
True
>>> '²'.isnumeric()
True
>>> '²'.isdigit()
True
>>> '²'.isdecimal()
False
>>> '3'.isdecimal()
True
>>> 'hari'.center(10)
' hari '
>>> 'hari'.ljust(10)
'hari '
>>> 'hari'.rjust(10)
' hari'
>>> "i like ice-cream".title()
'I Like Ice-Cream'
>>> "i like ice-cream".capitalize()
'I like ice-cream'
>>> li = ['1','2','3','4']
>>> "-".join(li)
'1-2-3-4'
```