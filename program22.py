#Write a program to find nth largest and nth smallest element from list.

def nth_largest_smallest(lst, n):
    sorted_lst = sorted(lst)
    nth_largest = sorted_lst[-n]
    nth_smallest = sorted_lst[n - 1]
    return nth_largest, nth_smallest


lst = [4, 2, 7, 1, 9, 5]
n = 3
nth_largest, nth_smallest = nth_largest_smallest(lst, n)
print(f"The {n}th largest element is: {nth_largest}")
print(f"The {n}th smallest element is: {nth_smallest}")

