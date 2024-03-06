#Write a program to print ASCII value of all the characters of string with character. 

print("Enter a String: ", end="")

text = input()

textlength = len(text)

for char in text:

    ascii = ord(char)

    print(char, "\t", ascii)


