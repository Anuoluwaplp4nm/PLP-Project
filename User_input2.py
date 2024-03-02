def main():
    # Accept user input to create a list of integers
    num_list = []
    n = int(input("Enter the number of integers you want to add to the list: "))
    
    for i in range(n):
        num = int(input(f"Enter integer {i + 1}: "))
        num_list.append(num)
    
    # Compute the sum of all integers in the list
    total_sum = sum(num_list)
    
    # Print the sum
    print("The sum of all integers in the list is:", total_sum)

    #Creating a tuple.
    my_tuple = ("God big toe", "Think Big", "Outlier", "Think and grow Rich", "Faith")

    #Print with the following loop.
    print (my_tuple [0])
    print (my_tuple [1])
    print (my_tuple [2])
    print (my_tuple [3])
    print (my_tuple [4])

# Create an empty dictionary to store a person's information
person_info = {}

# Ask user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

# Store information in the dictionary
person_info['name'] = name
person_info['age'] = age
person_info['favorite_color'] = favorite_color

# Display the information stored in the dictionary
print("\nPerson's Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")

# Accept user input to create two sets of integers
set1_input = input("Enter integers separated by spaces for the first set: ")
set2_input = input("Enter integers separated by spaces for the second set: ")

# Convert user input strings to sets of integers
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Display the common elements
print("Common elements:", common_elements)

# Store a list of words
word_list = ['benz', 'cadilac', 'lexus', 'g-wagon', 'camry', 'escalade']

# Use list comprehension to create a new list with words of odd length
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Display the new list
print("Words with odd number of characters:", odd_length_words)

if __name__ == "__main__":
    main()