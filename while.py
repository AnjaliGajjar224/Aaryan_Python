"""
Loops:
------------
1 . Entry Controlled loops - e.g. while , for
2 . Exit controlled loops - e.g do..while
"""

"""
Syntax:
------------

intialization

while condition:
    statements
    increment/decrement  # i += 1 , i -= 1
"""

# i = 1  # intialization

# while i <= 5:        # condition
#     print("Hello")
#     i += 1     # increment

# i = 5

# while i >= 1:
#     print("Hello")
#     i -= 1

"""
1. Take n from the user and print the numbers from 1 to n.

e.g. n = 5

Output: 1 2 3 4 5 

e.g. n = 5
     5 4 3 2 1
""" 

"""
1. Check whether the number is Armstrong or not.

e.g. n = 153

digits = 3
 
  1 ^ 3 + 5 ^ 3 + 3 ^ 3 
= 1 + 125 + 27
= 153

n == sum ---> Armstrong Numbers

3 digits = 153, 370 , 371 , 407
4 digits = 1634 , 
"""



n = int(input("Enter a number you want to check: "))

sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(n))    # sum = sum + digit ** 3 
    temp //= 10   # temp = temp // 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")

"""
1. Check whether the number is Palindrome or not.

e.g. 121 , 12321, 545

2. Check whether the number is Twin or not.

e.g. n = 123

    sum = 1 + 2 + 3 = 6
    mul = 1 * 2 * 3 = 6

    sum == mul ---> Twin number

3. Check whether the number is Prime or not.
"""