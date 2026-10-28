import copy

user = {"name":"Nilin","age":27,"address":{
    "location":"Manarcad"
}}

print("user",user)

# we need to use .get to get values from keys
print("users age", user.get("age"))

user["name"] = "Nilin Jacob"
# but we can reassign values/update like this

print(user)


# directly mutating object
user["address"]["location"] = "Kottayam";
print(user)

# take a deep copy and mutate
copiedUser = copy.deepcopy(user)
copiedUser["address"]["location"] = "India"
print(copiedUser)





