import string


def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
    
    return input_string.translate(translator)


if __name__ == "__main__":
    
    user_input = input("Enter a string: ")
    result = remove_punctuation(user_input)
    
    
    print("String without punctuation:")
    print(result)