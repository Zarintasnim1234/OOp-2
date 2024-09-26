def append_to_list(my_list, element):
    my_list.append(element)  
if __name__ == "__main__":
    
    my_list = []
    
    
    while True:
        user_input = input("Enter an element to append to the list (or type 'exit' to finish): ")
        if user_input.lower() == 'exit':
            break  
        my_list.append(user_input)  
    print("Final list:", my_list)