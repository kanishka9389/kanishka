#Write a program to check a particular element is present in the array or not.


def is_element_present(arr, element):
    for item in arr:
        if item == element:
            return True
    return False

# Example usage
my_array = [1, 2, 3, 4, 5]
element_to_check = 3

if is_element_present(my_array, element_to_check):
    print(f"The element {element_to_check} is present in the array.")
else:
    print(f"The element {element_to_check} is not present in the array.")

