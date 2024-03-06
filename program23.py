#Write a program to remove kth character from string.

def remove_kth_character(string, k):
    if k < 0 or k >= len(string):
        return "Invalid index"
    return string[:k] + string[k+1:]

# Example usage:
input_string = "example"
k = 3
result = remove_kth_character(input_string, k)
print("Original string:", input_string)
print("After removing", k, "th character:", result)


