# Creating an Empty list.
my_list = []
# Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print (my_list)

#Insert the value of 15 at the second position in the list.
my_list.insert(1, 15)

print (my_list)

#Extending my_list with another list of 50, 60, 70.
my_list.extend([50, 60, 70])

print (my_list)

#Removing the last element from my_list.
my_list.pop(-1)

print (my_list)

#Sorting my_list in ascending order.
my_list.sort ()

print (my_list)

#finding and printing the index with the value of 30.
index_of_30 = my_list.index(30)
print("Index of 30 in my_list is", index_of_30)