# my_dictionary = dict()

my_dictionary = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4
}

my_dictionary["A"] = 4 #UPDATE
my_dictionary["E"] = 5 #NEW KEY ADD

#print all keys
for key in my_dictionary:
    print(key , end=" ")
print()

#print all values
for value in my_dictionary.values():
    print(value, end=" ")
print()

#print all key & values
for key in my_dictionary:
    print(f"{key} = {my_dictionary.get(key)}")
print()

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
