def convert_case(input_string):
    
    lower_case = input_string.lower()
    upper_case = input_string.upper()
    return lower_case, upper_case


if __name__ == "__main__":
    
    user_input = input("Enter a string: ")
    
    
    lower_case, upper_case = convert_case(user_input)
    
    
    print("Lowercase:", lower_case)
    print("Uppercase:", upper_case)