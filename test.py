print("Hello World");

num1 = 22
num2 = 34

print(num1 + num2)

def greet(name):
    print("hello " + name + " how are you ?")

greet("Bob")

age = 17

if age > 18:
    print("you can drive")
elif age < 18:
    print("you can not drive")
else :
  print("asked to your parrents")
  
# for loop

for i in range(5):
    print(i)
    
    
# while loop

count = 0

while count < 5:
  print(count)
  count += 1
  
# lists

studentName = ["Vihaan", "Umesh", "Gautam"]
print(studentName[0])

# adding into an list

studentName.append("urvi")

print(studentName)

# removing

studentName.remove("Umesh")

print(studentName)

# dictionaries

data = {
  "name": "umesh",
  "rollno": 234,
  "id": 1234,
}

print(data["name"])
print(data["rollno"])

# adding some new keys

data["email"] = "urwwehwhf@gmail.com"

print(data)

# iterating on to the dictionary 

for key, value in data.items():
  print(key,":",value)
  
  # tuples 
  
  # Note: Tupl are immutable Hmm thats why we cant change their value Umm got it 
  
point = (10,20)

print(point[0])

# Lets Move on to the sets 

# Umm sets are unordered they are no duplicate you find go and try damn got it 😁

name_set = {"radhe", "Shradha", "Pranita"}

print(name_set)

name_set.add("Vihaan")

print(name_set)

# not append work on set LOL😅


# lets check remove is work or ?
name_set.remove("radhe")

print(name_set)

# ohh its workable 

# Lets Handle dive solve a problem 
# problem statement is pretty simple
# we gon a to calculate a squares of the numbers from 0 to the 5 
# this concept knows a "List Comprehension"

square = [i**2 for i in range(5)]

print(square)

# Yeah we got it right output: [0, 1, 4, 9, 16]

# Umm file handling exception handling and for sure Oops in python are remains 
