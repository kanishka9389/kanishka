#Write a program to display a character whose is more than other characters.

def most_common_char(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_count = 0
    most_common_char = ''
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_common_char = char
    return most_common_char

input_string = input("Enter a string: ")
most_common = most_common_char(input_string)
print(f"The most common character in the string is: {most_common}")

