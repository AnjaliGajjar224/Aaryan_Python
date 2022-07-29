my_str = "Python is a Programming Language"

# print(my_str.count("o"))    # count the number of o's in the string
# print(my_str.count("o",0,10))    # count the number of o's in the string from 0 to 10

# print(my_str.capitalize())   # capitalizes the first letter of the string
# print(my_str.casefold())    # converts the string to lowercase

# print("Length of the String:",len(my_str))
# print(my_str.center(52))        # 52 - length of the string = 52 - 32 = 20 / 2 = 10 spaces on both sides

# print(my_str.center(52,"*"))        # 52 - length of the string = 52 - 32 = 20 / 2 = 10 * on both sides

# print(my_str.center(53,"*"))        # 53 - length of the string = 53 - 33 = 20 / 2 = 10 * on both sides

# print(my_str.encode())           # by default UTF - 8

# print(my_str.encode("ascii"))    # converts the string to ascii
# print(my_str.encode("greek"))

# str1 = my_str.encode("greek")

# if str1 == my_str:
#     print("Strings are equal")
# else:
#     print("Strings are not equal")

# print(my_str.endswith("Language"))   # checks if the string ends with the given string
# print(my_str.endswith("L"))

# print(my_str.endswith("Language",0,10))   # checks if the string ends with the given string from 0 to 10
# print(my_str.startswith("P"))   # checks if the string starts with the given string

# print("Hello\tWorld\tHey")

# print("Hello\tWorld\tHey".expandtabs(25))

# print(my_str.find("o"))   # returns the index of the first occurrence of the substring

# print(my_str.find("o",5))   # returns the index of the first occurrence of the substring from 5 to length of the string

# print(my_str.rfind("o"))  # returns the index of the last occurrence of the substring

# num1 = 12
# num2 = 10

# print(num1,"+",num2,"=",num1+num2)

# print(f"{num1} + {num2} = {num1+num2}")

# print("My name is {name} and My age is {age}".format(age = int(input("Enter your age:")),name = input("Enter name:")))

# if num1 > num2:
#     print("num1 is greater than num2")
# else:
#     print("num2 is greater than num1")

# print("num1 is greater than num2") if num1 > num2 else print("num2 is greater than num1")

print(my_str.index("o"))   # returns the index of the first occurrence of the substring

print(my_str.index("o",5))   # returns the index of the first occurrence of the substring from 5 to length of the string

print(my_str.rindex("o"))  # returns the index of the last occurrence of the substring

print(my_str.find("b"))     # Returns -1 if the substring is not found
print(my_str.index("b"))    # Raises ValueError if the substring is not found

"""
Task 1:
---------------
Take a full name as input and print the following:

Input: 

full name: John Michel Smith

Output:

J.M.Smith

Task 2:
---------------
Input: Python Programming

Output:

vowels -  4
white spaces -  1
consonents - 13
"""