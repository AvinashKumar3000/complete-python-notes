
# `Print`

```python

# print(*args, sep=' ', end='\n')
#     
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     
```

example 1

```python
li = ['samsung', 'iphone','nokia','oppo','vivo']
print(*li,sep=" and ")
# samsung and iphone and nokia and oppo and vivo 
```

example 2

```python
li = [1,2,3,4]
n = len(li)
for i in range(n):
   print(li[i],end=",")
#  1,2,3,4,
```

NOTE: Below code will remove last `,`

```python
li = [1,2,3,4]
n = len(li)
for i in range(n):
    if i!=n-1:
       print(li[i],end=",")
    else:
       print(li[i],end="")
#  1,2,3,4
```

```python
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# file:  a file-like object (stream); defaults to the current sys.stdout.
# flush: whether to forcibly flush the stream.
```

`print` flush example

```python
# flush example
# --------------------------------------------
# example 1
import time

i = 0
while i<5:
    print(i)
    time.sleep(1)
# output
# The output will be like print each i value
# with a 1 second delay.
# --------------------------------------------
# example 2
import time

i = 0
while i<5:
    print(i,end=" ")
    time.sleep(1)
# output
# The output will be like print each i value
# side by side. But It will show the output 
# only after 5 second
# REASON : that is because by default flush=False,
#   - Which means first it will store all character that should be 
#     printing in a single line.
#   - Then it will flush all the values to output screen

# To make our code run with following scenario
# we have to pass flush=True

i = 0
while i<5:
    print(i,end=" ",flush=True)
    time.sleep(1)
# output will be same but different behavior
```

print `file`

```python
# by default python will print output in output screen.
# But instead you can print the output in other streams like in files.
fs = open('output.txt','w')
print('hello world!', file=fs)
print('sample text', file=fs)
print('End of the code', file=fs)
# Now output will be saved in a file. Instead of output screen.
```