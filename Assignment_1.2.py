import json

indian_states = """{
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur",
    "West Bengal": "Kolkata"
}"""

# # convert json object to dict
dict_obj = json.loads(indian_states)
print(dict_obj)
print(type(dict_obj))

# # convert dict object to json
json_obj = json.dumps(dict_obj)
print(json_obj)
print(type(json_obj))
# with open('indian_states.json', 'w') as file:
#     json.dump(indian_states, file, indent=4)




