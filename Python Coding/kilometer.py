def kilometers_to_miles(kilometers):
    
    conversion_factor = 0.621371
    return kilometers * conversion_factor


kilometers = float(input("Enter the distance in kilometers: "))


miles = kilometers_to_miles(kilometers)


print(f"{kilometers} kilometers is equal to {miles} miles.")