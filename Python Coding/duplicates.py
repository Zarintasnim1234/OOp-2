# Function to remove duplicates using a set
def remove_duplicates_with_set(my_list):
    return list(set(my_list))  # Convert to set and back to list

# Function to remove duplicates using a loop
def remove_duplicates_with_loop(my_list):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Function to remove duplicates using list comprehension
def remove_duplicates_with_comprehension(my_list):
    unique_list = []
    [unique_list.append(item) for item in my_list if item not in unique_list]
    return unique_list

# Main function to take user input
if __name__ == "__main__":
    # Input a list from the user
    user_input = input("Enter a list of elements (comma-separated): ")
    
    # Create a list from the input and strip whitespace
    my_list = [item.strip() for item in user_input.split(',')]
    
    # Remove duplicates using different methods
    result_set = remove_duplicates_with_set(my_list)
    result_loop = remove_duplicates_with_loop(my_list)
    result_comprehension = remove_duplicates_with_comprehension(my_list)

    # Display the results
    print("Original List:", my_list)
    print("Removed Duplicates (Set Method):", result_set)
    print("Removed Duplicates (Loop Method):", result_loop)
    print("Removed Duplicates (Comprehension Method):", result_comprehension)
