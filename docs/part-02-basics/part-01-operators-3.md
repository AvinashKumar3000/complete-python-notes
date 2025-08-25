## bitwise operator

1. AND (&)
   The bitwise AND operation compares each bit of two numbers and returns 1 if both bits are 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a & b  # (binary: 0001)
print(result)   # Output: 1
```

2. OR (|)
   The bitwise OR operation compares each bit of two numbers and returns 1 if at least one of the bits is 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a | b  # (binary: 0111)
print(result)   # Output: 7
```

3. XOR (^)
   The bitwise XOR operation compares each bit of two numbers and returns 1 if only one of the bits is 1, otherwise it returns 0.

```python
a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

result = a ^ b  # (binary: 0110)
print(result)   # Output: 6
```

4. NOT (~)
   The bitwise NOT operation flips all the bits of a number, turning 1s into 0s and 0s into 1s. This is also known as the bitwise complement.

```python
a = 5  # (binary: 0101)

result = ~a  # (binary: 1010, which is -6 in decimal due to two's complement representation)
print(result)  # Output: -6

# ~ will change sign bit also.

# 1010
# 0101 <- 1s compliment
#    1 <- 2s compliment
# 0110 <- result (6)

```

5. Left Shift (<<)
   The left shift operation shifts all the bits of a number to the left by a specified number of positions. This is equivalent to multiplying the number by 2 raised to the power of the number of positions shifted.

```python
a = 5  # (binary: 0101)

result = a << 1  # (binary: 1010)
print(result)    # Output: 10

```

6. Right Shift (>>)
   The right shift operation shifts all the bits of a number to the right by a specified number of positions. This is equivalent to dividing the number by 2 raised to the power of the number of positions shifted, discarding any remainder.

```python
a = 5  # (binary: 0101)

result = a >> 1  # (binary: 0010)
print(result)    # Output: 2
```

| Operation   | Symbol | Description| Example| Result|
| -------- | ------ | ------------------------------------------------- | --------------------------------------- | ----------- |
| AND         | `&`    | Bits that are 1 in both operands                  | `5 & 3` (0101 & 0011)                   | `1` (0001)  |
| OR |     | Bits that are 1 in at least one operand | `5`          | `3` (0101 | 0011) | `7` (0111) |
| XOR         | `^`    | Bits that are 1 in one operand but not both       | `5 ^ 3` (0101 ^ 0011)                   | `6` (0110)  |
| NOT         | `~`    | Bits that are flipped                             | `~5` (~0101)                            | `-6` (1010) |
| Left Shift  | `<<`   | Shifts bits to the left, filling with 0s          | `5 << 1` (0101 << 1)                    | `10` (1010) |
| Right Shift | `>>`   | Shifts bits to the right, discarding shifted bits | `5 >> 1` (0101 >> 1)                    | `2` (0010)  |

In above case `OR` has pipe symbol `|`.