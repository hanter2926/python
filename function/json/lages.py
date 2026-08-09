import json
x = {
    "name" : "vikram pal",
    "age" : 20,
    "city" : "patana",
    "married" : False,
    "girlfriend" : True,
    "friends" : ("aditya", "prsool", "Rambhol", "Rahul", "vikash", "ravi", "pardip"),
    "pats" : None,
    "bike" : True,
}
print(x)
print(json.dumps("name"))        
print(json.dumps(x, indent=0))
print(json.dumps(x, indent=2 , sort_keys=True))