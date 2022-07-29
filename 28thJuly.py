"""
Bitwise Operators:
1. & : AND
2. | : OR
3. ^ : XOR
4. << : Left Shift
5. >> : Right Shift

45 - 101101
43 - 101011

1) & AND

Truth Table
---------
a | b | a & b
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1

45 - 1 0 1 1 0 1
&    & & & & & &
43 - 1 0 1 0 1 1
------------------
     1 0 1 0 0 1  
"""
# print(45&43)

"""
2. OR Operator(|)

    Truth Table
    ---------
    a | b | a | b
    0 | 0 | 0
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 1

    45 - 1 0 1 1 0 1
    |    | | | | | |
    43 - 1 0 1 0 1 1
    ------------------
         1 0 1 1 1 1 (47)
"""
# print(45|43)

"""
3. XOR Operator(^)

    Truth Table
    ---------
    a | b | a ^ b
    0 | 0 | 0
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 0

    45 - 1 0 1 1 0 1
    ^    ^ ^ ^ ^ ^ ^
    43 - 1 0 1 0 1 1
    ------------------
         0 0 0 1 1 0 
"""
# print(45^43)

"""
Shift Operators:

    1) << : Left Shift
    2) >> : Right Shift

45 - 101101
42>>2
           32  16   8  4  2  1
45    -    1    0   1  1  0  1
45>>1 -          1  0  1  1  0  1
45>>2               1   0 1  1  0  1

    2) << : Left Shift

    45 - 101101
       
         128 64 32 16 8 4 2 1
    45           1 0  1 1 0 1 
    45<<2 1   0  1  1 0 1 0 0
# """
# print(45>>2)           #1011
# print(45<<2)           #10110100

"""
Membership Operators:

1. in 
2. not in

# Returns True if the specified value is found in the sequence and False otherwise.
"""

# print('b' in 'banana')             # True

# print('k' in 'banana')           # False    

# print('b' not in 'banana')     # False
# print('k' not in 'banana')     # True

# List1 = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# if "banana" not in List1:
#     print("Yes, 'banana' is available in the fruits list")

"""
Identity Operators:
1. is
2. is not
# """
# a = 10
# b = 20
# c = 10

# print(id(a))
# print(id(b))
# print(id(c))

# print(a is b)
# print(a is c)

# print(a is not b)
# print(a is not c)

"""
Sequence Data Types:
1. Strings
2. Tuples
3. Lists

String - String is a sequence of characters.

---> String is immutable.
---> String is ordered.
# """
# ch = 'a'
# print(type(ch))
# print(ch)

my_str = "Python"
print(my_str)

"""
    Positive indexing   Negative Indexing
P       0                   -6
y       1                   -5
t       2                   -4
h       3                   -3
o       4                   -2
n       5                   -1
"""
print("Length of the String:",len(my_str))
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[3])
print(my_str[4])
print(my_str[5])
# print(my_str[6])

print(my_str[-1])
print(my_str[-2])
print(my_str[-3])
print(my_str[-4])
print(my_str[-5])
print(my_str[-6])
# print(my_str[-7])

"""
Slicing of the String - Extracting Substring

1. var_name[start:end:step]
2. var_name[start:end]
3. var_name[start:]
4. var_name[:end]
5. var_name[:]
"""

s1 = "Python is a Programming Language"
print("Length of the String:",len(s1))
print(s1)

print(s1[0:15])              # starts from 0 to 14(15 not included) 
# print(s1[15])
# print(s1)

print(s1[5:30])             # starts from 5 to 29(30 not included)
print(s1[-30:-15])


print(s1[15:])         # starts from 15 to end
print(s1[:15])         # starts from 0 to 14

print(s1[-25:])       # starts from -25 to -1(end)
print(s1[:-12])       # starts from -32 to -11(-12 not included)

print(s1[:])

print(s1[0:30:1])    # starts from 0 to 29(30 not included) with step 1
print(s1[0:30:2])    # starts from 0 to 29(30 not included) with step 2
print(s1[::5])

print(s1[-30:-2:3])

print(s1[-15:-30:-1])
print(s1[30:15:-1])
print(s1[::-1])
print(s1[::-2])
