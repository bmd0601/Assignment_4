# Write a Python program to square the elements of a list using map() function.

lst = [4, 5, 2, 9]

squared_numbers = list(map(lambda x: x ** 2, lst))

print("Square the elements of the list:")
print(squared_numbers)