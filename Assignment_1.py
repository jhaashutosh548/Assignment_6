import json

file = open(r"C:\Users\bmd06\OneDrive\Documents\GitHub\DS150423\Myprogram\assignment_JSON\employee.json","r")

# it read the file and converted json data into dict and returned it to us
data = json.load(file)
print(data)
print(type(data))

# # it converted the dict into json and then stored it inside the file
# file1 = open(r"C:\Users\bmd06\OneDrive\Documents\GitHub\DS150423\Myprogram\assignment_JSON\employee.json","w")
# json.dump(data,file1)


