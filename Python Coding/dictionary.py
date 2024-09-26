# Function to convert two lists to a dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Function to convert a list of tuples to a dictionary
def tuples_to_dict(tuples_list):
    return dict(tuples_list)

# Function to convert a list of lists to a dictionary
def lists_of_lists_to_dict(list_of_lists):
    return dict(list_of_lists)

# Main function to take user input
if __name__ == "__main__":
    # Convert two lists to a dictionary
    keys_input = input("Enter the keys (comma-separated): ").split(',')
    values_input = input("Enter the values (comma-separated): ").split(',')
    
    # Stripping whitespace around each element
    keys = [key.strip() for key in keys_input]
    values = [value.strip() for value in values_input]
    
    # Creating the dictionary
    result_dict = lists_to_dict(keys, values)
    print("Dictionary from two lists:", result_dict)

    # Convert a list of tuples to a dictionary
    tuples_input = input("Enter a list of tuples (e.g., (key1, value1), (key2, value2)): ")
    tuples_list = eval(tuples_input)  # Caution: eval() should be used with trusted input
    result_dict_from_tuples = tuples_to_dict(tuples_list)
    print("Dictionary from list of tuples:", result_dict_from_tuples)

    # Convert a list of lists to a dictionary
    list_of_lists_input = input("Enter a list of lists (e.g., [[key1, value1], [key2, value2]]): ")
    list_of_lists = eval(list_of_lists_input)  # Caution: eval() should be used with trusted input
    result_dict_from_lists = lists_of_lists_to_dict(list_of_lists)
    print("Dictionary from list of lists:", result_dict_from_lists)
