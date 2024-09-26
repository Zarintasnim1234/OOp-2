def compare_lists(list1, list2):
    # Check if the lists are equal
    are_equal = list1 == list2
    
    # Check if list1 is a subset of list2
    is_subset = set(list1).issubset(set(list2))
    
    # Find common elements
    common_elements = list(set(list1) & set(list2))
    
    # Find unique elements
    unique_to_list1 = list(set(list1) - set(list2))
    unique_to_list2 = list(set(list2) - set(list1))
    
    return are_equal, is_subset, common_elements, unique_to_list1, unique_to_list2

# Main function to take user input
if __name__ == "__main__":
    # Input two lists from the user
    list1 = input("Enter the first list of elements (comma-separated): ").split(',')
    list2 = input("Enter the second list of elements (comma-separated): ").split(',')
    
    # Strip whitespace around each element
    list1 = [item.strip() for item in list1]
    list2 = [item.strip() for item in list2]
    
    # Compare the lists
    are_equal, is_subset, common_elements, unique_to_list1, unique_to_list2 = compare_lists(list1, list2)
    
    # Display the results
    print(f"Are the lists equal? {are_equal}")
    print(f"Is the first list a subset of the second list? {is_subset}")
    print(f"Common elements: {common_elements}")
    print(f"Unique to the first list: {unique_to_list1}")
    print(f"Unique to the second list: {unique_to_list2}")