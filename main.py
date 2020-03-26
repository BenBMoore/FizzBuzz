import fizzbuzz

if __name__ == "__main__":
    print("Welcome to Fizzbuzz! ")
    userInput = input("Enter the number to fizz buzz too: ")
    try:
        int(userInput)
        if int(userInput) < 0:  # If it isn't a positive number, print error message
            print("Sorry, it must be a positive number")
        for x in range(0, int(userInput)):
            print(fizzbuzz.fizzbuzz(x))
    except ValueError:
        print("Please Enter a whole number")
