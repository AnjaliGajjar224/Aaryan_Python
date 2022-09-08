"""
for loop:
---------------

for(initialization;condition;increment/decrement)
{

}

Syntax:
----------

for var_name in range(start,end,step):
    statement
"""

# for i in range(5):                   # i = 0 to 4(5 is not included)
#     print(i)

# for i in range(1,6):                # i = 1 to 5 (6 is not included)
#     print(i)

# for i in range(11,21):                # i = 11 to 20(21 is not included)
#     print(i)

"""
5 4 3 2 1
"""

# for i in range(5,0,-1):                # i = 5 to 1 (0 is not included)
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# s = "Hello, world!"

# for i in s:
#     print(i)

# l = ["Hello",12,34.56,2+5j,[12,3,4,4]]

# for i in l:
#     print(type(i))
#     print(i)

# print(l)

"""
Write a program to find Prime numbers between range.

e.g. 1 to 10

2 3 5 7 
"""

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

print("Prime Numbers: ")
for num in range(start,end+1):
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        print(num,end=" ")
