def reverse_string(string):
    return string[::-1]


user_string = input("Enter a string: ")


reversed_string = reverse_string(user_string)


print(f"The reverse of '{user_string}' is '{reversed_string}'.")
