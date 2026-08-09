import json

x = {
    "name" : "vikram pal",
    "age " :20,
    "city" : "patan"
}
m = {
    "colloge" : "shobhit",
    "student" : "vikram pal",
    "cours" : "BCA"
}
n = json.dumps(m)
y = json.dumps(x)
print(n)
print(y)


