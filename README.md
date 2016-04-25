# MATLAB to Python cheatsheet
<!-- MarkdownTOC depth=4 -->

- Getting started
    - What do we need ?
    - Important
- Language fundamentals
    - Variables
    - Operators
        - Arithmetic operators
        - Relational operators
        - Logical operators
    - Control flow
        - if-else if-else
        - For loop
        - While loop
        - Try - Catch
    - Functions
        - Creating a function
- References

<!-- /MarkdownTOC -->

- [Getting started]("#getting-started")
    - What do we need ?
    - Important
- Language fundamentals
    - Variables
    - Operators
        - Arithmetic operators
        - Relational operators
        - Logical operators
    - Control flow
        - if-else if-else
        - For loop
        - While loop
        - Try - Catch
    - Functions
        - Creating a function
- References

## Getting started

### What do we need ?

Some Python libraries installed to start:

* NumPy
* SciPy
* Matplotlib
* SymPy

### Important

The general structure of these notes is:

```matlab
% Some MATLAB code
x = 10;
disp(x);
```

```python
# followed by a equivalent/similar Python code
x = 10
print(x)
```


## Language fundamentals

### Variables

Assign variables:

```matlab
% Assign variables
a = 10;
```

```python
# Assign variables
a = 10
```

Multi assign:

```matlab
% Unsupported
```

```python
# Multi assign
a, b, c = 10, 20, 30
# a = 10 
# b = 20
# c = 30
```

### Operators

#### Arithmetic operators

```matlab
% MATLAB
a = 10;
b = 20;
a + b; % Addition
a - b; % Subtraction
a * b; % Multiplication
a / b; % Division
```

```python
# Python
a , b = 10, 20
a + b # Addition
a - b # Subtraction
a * b # Multiplication
a / b # Division
```

#### Relational operators

```matlab
a == b  % Equal
a > b   % Greater than
a < b   % Less than
a >= b  % Greater than or equal
a <= b  % Less than or equal
a ~= b  % Not equal
```

```python
a == b  # Equal
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal
a <= b  # Less than or equal
a != b  # Not equal
```

#### Logical operators

```matlab
a && b      % Short-circuit logical AND
a || b      % Short-circuit logical OR
a & b       % Element-wise logical AND
a | b       % Element-wise logical OR
xor(a, b)   % Logical EXCLUSIVE OR
~a          % Logical NOT
```

```python
a and b     # Short-circuit logical AND
a or b      # Short-circuit logical OR
a and b     # Element-wise logical AND
a or b      # Element-wise logical OR
a ^ b       # Logical EXCLUSIVE OR
not a       # Logical NOT
```


### Control flow

#### if-else if-else

Only `if`:

```matlab
% Using if
a = 11
if a > 10
    disp('a is greater than 10');
end
```

```python
a = 11
if a > 10:
    print("a is greater than 10")
```

`if-else` structure:

```matlab
n = 1
if n > 0
    disp('n is positive');
else
    disp('n is negative or zero');
end
```

```python
n = 1
if n > 0:
    print('n is positive')
else:
    print('n is negative or zero')
```

#### For loop

```matlab
% for loop
for i = 1:10
    disp(i)
end
```

```python
# for loop
for i in range(1,11):
    print(i)
```

#### While loop

```matlab
% while loop
a = 1
while a < 10
    disp(a);
    a = a + 1;
end
```

```python
# while loop
a = 1
while a < 10:
    print(a)
     a += 1
```

#### Try - Catch

```matlab
try
    % Do something ...
catch err
    % On failure
end
```

```python
try:
    % Do something
except Exception:
    % On failure
end
```


### Functions

#### Creating a function

General syntax:

```matlab
function [out1, out2,...] = MyFun(arg1, arg2, ...)
% Code here...
% out1 = some1
% out2 = some2
% ...
end
```

```python
def MyFun(arg1, arg2, ...):
    # Code here ...
    return out1, out2, ...
```

Calling functions:

```matlab
% Calling MyFun
[out1, out2, ...] = MyFun(arg1, arg2, ...)
```

```python
# Calling MyFun
out1, out2, ... = MyFun(arg1, arg2, ...)
```

A simple example:




## References

1. [http://mathesaurus.sourceforge.net/matlab-numpy.html](http://mathesaurus.sourceforge.net/matlab-numpy.html)
