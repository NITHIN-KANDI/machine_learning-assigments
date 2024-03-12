def common_digits(input_list1, input_list2):
    # Convert input lists to sets to remove duplicate elements and enable set operations
    set1 = set(input_list1)
    set2 = set(input_list2)
    
    # Find the common elements between the sets
    common_digits_set = set1.intersection(set2)
    
    # Return the count of common elements
    return len(common_digits_set)

# Example lists
list1 = [5, 4, 3, 6, 7]
list2 = [1, 2, 3, 4, 5]

print("The first list is:", list1)
print("The second list is:", list2)

# Call the function and print the result
common_digit_count = common_digits(list1, list2)
print("The count of common elements between the lists is:", common_digit_count)
