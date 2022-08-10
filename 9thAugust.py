# print("ABC123".isalnum())            # Returns True if String Contains Alphabets or numbers
# print("ABCD".isalnum())
# print("1234".isalnum())
# print("!@ABC&".isalnum())

# print("ABCD".isalpha())             # Returns True if String contains only Alphabets

"""
isdigit
isdecimal
isnumeric
"""

s5 = "2022"
print(s5.isdecimal())   # considers strictly plain digits from 0 to 9 only, nothing else
print(s5.isdigit())     # considers subscripts, superscripts and circled numbers also as numbers
print(s5.isnumeric())   # considers vulgar fractions, roman numerals, numbers from other languages

s6 = "2⁸"
print(s6)
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())

s7 = "②⓪②②"
print(s7)
print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())

s8 = "¼"
print(s8)
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())

s9 = "二千二十二"
print(s9)
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())

s10 = "VI"
s11 = "Ⅵ"
print(s10)
print(s10.isnumeric())
print(s11)
print(s11.isnumeric())

print("Python".isascii())
print("num1".isidentifier())         #True
print("num 1".isidentifier())        #False
print("123num".isidentifier())
print("&num".isidentifier())


print("python programming".islower())
print("PYTHON".isupper())
print("Python Is A Programming Language".istitle())


print("PYTHON".lower())
print("python".upper())
print("Python is a programming language".title())

print("Are you #1?".isprintable())
print("Are you \n#1?".isprintable())

print("                    hey             ".isspace())
print("    ".isspace())
print("\t".isspace())
print("\n".isspace())

s1 = "Hello!Good Evening"
s2 = "Hey"
myList = ["Royal","Hey","Technology"]


print(s1.join(s2))
print(s1.join(myList))
print(" ".join(myList))


print(s2.ljust(10))
print(s2.ljust(10,"#"))

print(s2.rjust(10))
print(s2.rjust(10,"*"))

s3 = "$$$$$$$$$$$$$$Hello$$$$$$$$$$$$$$$"
s4 = "             HI        "

print(s4.lstrip())
print(s3.lstrip("$"))


s5 = "HelloHelloHelloHelloGoodHelloHelloHello"
print(s5.lstrip("l"))

print(s3.rstrip("$"))

print(s3.strip("$"))

print("Good_Morning_Hey_Hello_Bye".partition("_"))
print("Good_Morning_Hey_Hello_Bye".rpartition("_"))

print("Good_Morning_Hey_Hello_Bye".split("_",2))

print("Good_Morning_Hey_Hello_Bye".rsplit("_",2))

print("Good  Evening.".startswith("Good"))

print("Good Evening".swapcase())

print("Good\nevening\nHello\nHey".splitlines())

print("Good evening".replace(" ","_"))

d = "9-08-2022"

print(d.zfill(10))

text = "Hello"

print(text.zfill(10))