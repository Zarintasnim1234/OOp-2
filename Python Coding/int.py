def int_to_string(number):
    return str(number)


if __name__ == "__main__":
    
    user_input = input("Enter an integer: ")
    
    try:
        
        number = int(user_input)
        
        result_string = int_to_string(number)
        
        
        print("Converted string:", result_string)
    except ValueError:
        print("Please enter a valid integer.")