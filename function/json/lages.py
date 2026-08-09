import json
x = {
   " name" : "vikram pal",
    "age" : 20,
    "city" : "patana",
    "married" : False,
    "girlfriend" : True,
    "friends" : ("aditya", "prsool", "Rambhol", "Rahul", "vikash", "ravi", "pardip"),
    "pats" : None,
    "bike" : True,
}
print(x)
print(json.dumps(x))