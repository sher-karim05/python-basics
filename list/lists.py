fruits = ["Apple", "orange", "Mango","Apricot"]
numbers = [1,6,8,3,7,9,12,9,11,25]
friends = ["Zilan", "Muiz", "Abid", "Waseem", "Nasir", "Hussain", "Nasir", "Hasnat", "Samar", "mehtab", "zeeshan"]
#add list to an array using extend function
# friends.extend(fruits)

#add a single item into a list using append
# friends.append("saleem")

#add a single item in a specified index using inert(2, "ali")
# friends.insert(1, "Ali")

#remove an element from a list
fruits.remove("orange")
print(fruits)

#clear function removes all elements of a list
# friends.clear()

#pop function removes the last element of a list
# friends.pop()

#index function returns the index of list element
# friends.index("mehtab")

#count function is used to count same elements in a list
# print(friends.count("Nasir"))

#sort function arrange strings and numbers in  acending order
# friends.sort()
# numbers.sort()

#reverse function arrage list items by reversing the direction of elements order
# friends.reverse()
# numbers.reverse()

#copy function copies list into a new list

friends2 = friends.copy()

print(friends2)
