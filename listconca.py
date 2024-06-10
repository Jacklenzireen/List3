list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
odd_values = list1[1::2] # the odd index values
even_values = list2[0::2] # the even index values 
list3  = odd_values + even_values # list sum of two lists (Concatenation )
print(list3)