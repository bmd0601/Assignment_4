# Write a Python program to triple all numbers of a given list of integers. Use Python map.

lst = [1, 2, 3, 4, 5, 6, 7]
triple_numbers = list(map(lambda input_list : input_list * 3, lst ))
print("Triple of list numbers:")
print(triple_numbers)
