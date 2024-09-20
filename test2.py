# let deep dive into the lists
# append() -- adds an elment into the list 
# insert() -- insrt an element acording to index [index:value]
# extend() its like merge a two list -- [list1] [list2] after used extend its like [list1list2]

name_data = ["umesh", "urvi", "virat", "shyam"];

# name_data.append("Shri Hanuman");

# name_data.insert(0,"shri Hanuman")
# name_data.remove("shyam")
# name_data.insert(1,"shyam")

# numbers = [1, 2, 3, 4, 5,]

# name_data.extend(numbers)

# pop()

# name_data.pop(1)

# lets sort an lists oh its make an easy 

# name_data.sort() --> by default it sorts in ascending way 

name_data.sort(reverse=True) #its sort in descending way

# list comprehension in deep 

print(name_data)

new_name = [name_data for name_data in name_data if "a" in name_data]

# new_name = name_data.copy()

# concanited 

new_name = name_data + new_name

# print(new_name)

# nested list 

name_data.insert(2, ["Gripal", "swastik", "Puja"])

# print(name_data)

