def main():
    try:
        # Creating a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
           
            file.write("Hello world, this is my first line.\n")
            file.write("100001 \n")
            file.write("I am Anuoluwa and I am 21 years old and my postal code is: 100001.\n")

        # Reading and Display of File ('r').
        print("Contents of my_file.txt:")
        with open("my_file.txt", "r") as file:
            for line in file:
                print(line.strip())  # Strip to remove newline characters

        # Appending File ('a').
        with open("my_file.txt", "a") as file:
            # Appending additional lines of text to the existing content
            file.write("This is an appended line of code.\n")
            file.write("Appending another line.\n")
            file.write("And one more line for preciseness.\n")

        print("\nContents of my_file.txt after appending:")
        # Display the contents of the file after appending
        with open("my_file.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied to access the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Execution complete.")

if __name__ == "__main__":
    main()
