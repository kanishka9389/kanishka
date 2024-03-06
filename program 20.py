#Write a program to check wether a list is monotonic or not.

def is_monotonic(lst):
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
    
    return increasing or decreasing


lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]
lst3 = [1, 3, 2, 4, 5]

print(is_monotonic(lst1))  # Output: True
print(is_monotonic(lst2))  # Output: True
print(is_monotonic(lst3))


