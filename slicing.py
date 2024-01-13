# initializing a list with elements of different data types
mixed_data = [3,8,5.82,6.3,2+3j,54-99j,"hello","python"]

# displaying the required elements using list slicing 
# indexing in python starts from 0
print("The first three elements are",mixed_data[0:3])
print("Elements starting from the 2nd to the 5th position are",mixed_data[1:5])
print("The last two elements are",mixed_data[6:])

# initializing a for loop to iterate through each element in the list
for element in mixed_data:
    # displaying the data type of the element using type().__name__ function
    print("\nElement:", element,[type(element).__name__])