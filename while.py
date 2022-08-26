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



# n = int(input("Enter a number you want to check: "))

# sum = 0
# temp = n

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** len(str(n))    # sum = sum + digit ** 3 
#     temp //= 10   # temp = temp // 10

# if sum == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

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
# n = int(input("Enter a number you want to check: "))

# rev = 0
# temp = n 

# while temp > 0:
#   digit = temp % 10
#   rev = rev * 10 + digit
#   temp //= 10   # temp = temp // 10

# if n == rev:
#   print("Palindrome")
# else:
#   print("Not Palindrome")

"""
Nested while loop:
------------------

initialization

while condition:
  initialization
  while condition:
    statements
    incremet/decrement
  increment/decrement
"""

# i = 1

# while i <= 5:
#   j = 1
#   while j <= 5:
#     print("*",end=" ")
#     j += 1
#   print()
#   i += 1

"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

# i = 1
# num = int(input("Number: "))
# n = 1

# while i <= num:
#   j = 1
#   while j <= num:
#     print(n,end=" ")
#     n += 1
#     j += 1
#   print()
#   i += 1

"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""

# ch = 65

# print(chr(ch))

# i = 0
# ch = 65
# while i < 5:
#   j = 1
#   while j <= 5:
#     print(chr(ch + i),end=" ")
#     j += 1
#   print()
#   i += 1

"""
*
* *
* * *
* * * *
* * * * *

* * * * *
* * * *
* * *
* *
*

* * * * *
  * * * *
    * * *
      * *
        *

1 2 3 4 5 
2 3 4 5
3 4 5
4 5 
5

5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1

     *
   * * *
 * * * * *
* * * * * * 
"""
"""
Control statements
1. break
2. continue
3. pass
"""

# i = 1

# while i <= 10:
#     if i == 5:
#       break
#     print(i)
#     i += 1

# i = 1

# while i <= 10:
#     i += 1

#     if i == 5:
#       continue
#     print(i)

# i =1

# while i <= 5:
#   pass
#   i += 1

"""
while...else
"""

# i = 1

# while i <= 10:
#   print(i)
#   i += 1
# else:
#   print("Loop is over")

i = 1

while i <= 10:
  print(i)
  if i == 5:
    break
  i += 1
else:
  print("Loop is over")