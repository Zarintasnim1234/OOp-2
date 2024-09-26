def count_occurrences_with_count(main_string, substring):
    return main_string.count(substring)

# Function to count occurrences of a substring using a loop
def count_occurrences_with_loop(main_string, substring):
    count = 0
    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)  # Move past the last found substring
    return count

# Main function to take user input
if __name__ == "__main__":
    # Input a string and a substring from the user
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to search for: ")
    
    # Count occurrences using count() method
    occurrences_count = count_occurrences_with_count(main_string, substring)
    
    # Count occurrences using loop
    occurrences_loop = count_occurrences_with_loop(main_string, substring)
    
    # Display the results
    print(f"The substring '{substring}' occurs {occurrences_count} times (using count()).")
    print(f"The substring '{substring}' occurs {occurrences_loop} times (using loop).")