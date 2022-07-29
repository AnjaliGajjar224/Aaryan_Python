"""
Encode method in String

    encode(string, encoding)

"""
# from encodings.aliases import aliases

# print("Available encodings:")
# print(aliases)


# my_str = "Hello World"
# print("\nOriginal string:", my_str)
# # Encode string to UTF-8 by default
# print("Encoded string:", my_str.encode())

# print()

# text = "PŸTHØN"

# print("Original string:", text)
# # Encode string to UTF-8 by default
# print("Encoded string:", text.encode())

# myStr = "Good Môrning"
# print("\nOriginal string:", myStr)
# # Encode string to latin10
# print("Encoded string:", myStr.encode("latin10"))
# print()

# word = 'Δ π θ'
# print('String is:', word)
# # encodes to greek
# print('Encoded string is:', word.encode('greek'))

# # Python program to illustrate encode()
greet = 'Wełcøme'

# print('The encoded version (with ignore) is:', greet.encode("ascii","strict"))

# print('The encoded version (with ignore) is:', greet.encode("ascii","ignore"))

print('The encoded version (with replace) is:', greet.encode("ascii","replace"))

print('The encoded version (with namereplace) is:', greet.encode("ascii","namereplace"))

print('The encoded version (with backslashreplace) is:', greet.encode("ascii","backslashreplace"))

print('The encoded version (with xmlcharrefreplace) is:', greet.encode("ascii","xmlcharrefreplace"))

