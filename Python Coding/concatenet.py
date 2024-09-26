def concatenate_strings(str1, str2):
    return str1 + str2


if __name__ == "__main__":
    
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    
    result_string = concatenate_strings(string1, string2)
    
    
    print("Concatenated string:", result_string)