def find_common_elements(list1, list2):
    set1 = set(list1)# Convert lists to sets to find the common elements
    set2 = set(list2)
    common_elements = set1.intersection(set2)# Find the intersection of the sets (common elements)
    # Return the number of common elements
    return len(common_elements)


if __name__ == "__main__":
    # Example lists
    list1 = [2,4,6,7,9]
    list2 = [2,5,4,3,6]

    # Call the find_common_elements function
    result = find_common_elements(list1, list2)

    # Print the result
    print(f"Number of common elements: {result}")
