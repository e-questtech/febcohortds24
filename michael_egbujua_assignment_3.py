# 1. Write a python script that would create a new list containing the data type of the elements in the list below:

new_list= [1,2,"great", "faithful",(1,2,3), False]

list_type = []
for i in new_list:
    display = type(new_list)
    list_type.append(display)
print(list_type)


# 2. Create two lists, then write a python script to merge both lists

list_1 = ["Wike", 8.9, True, 3j, 43]
list_2 = [32, "Seyi", "Blue", 2.33]
merge_list = list_1 + list_2
print(merge_list)

# 3. Given the following dictionary

warehouse = {
    'cables' : {"Colman":500, "Alinco": 600},
    'paint' : ['saclux', 'demalux', 'silklux'],
    'metals' : ['roofing sheets','binding wires', 'coils']
}

#Add a key to inventory called 'safety gear'.
#Set the value of 'safety gear' to be a list consisting of 
#the strings 'red wings boot', 'hard hat', and 'coverall'

warehouse.update({"safety gear": ["red wings boot", "hard hat", "coverall"]})
print(warehouse)

#remove Colman from the dictionary
del warehouse["cables"]["Colman"]

print(warehouse)