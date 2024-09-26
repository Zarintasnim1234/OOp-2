def list_to_string(string_list):
    
    return ' '.join(string_list)  
if __name__ == "__main__":
    
    user_input = input("Enter a list of words separated by spaces: ")
    
    
    string_list = user_input.split()
    
    
    result_string = list_to_string(string_list)
    
    
    print("Converted string:")
    print(result_string)