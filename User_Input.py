def main():
    # Prompt user to enter their name
    name = input("Please enter your name: ")

    # Prompt user to enter their age
    age = input("Please enter your age: ")

    # Prompt user to enter their location
    location = input("Please enter your location: ")

    # Print out the user's information
    print("\nHello, {}! It's nice to meet you.".format(name))
    print("I see you're {} years old, and you're located in {}.".format(age, location))
    print("Have a great day!")

if __name__ == "__main__":
    main()
