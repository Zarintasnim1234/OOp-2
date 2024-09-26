import random
import string


def generate_random_string(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


if __name__ == "__main__":
    
    length = int(input("Enter the length of the random string: "))
    
    
    result_string = generate_random_string(length)
    
    
    print("Generated random string:", result_string)