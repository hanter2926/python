import json

X = '{"name" : "vikram", "age": 20, "city" : "bihar", "post" : "shivnar"}'
A = '{"colloge" : "Shobhit" , "admin" : "19th", "form" : "BCA"}'
P = '{"indan" : "in world", "bihar" : "patna", "patna" : "mokama", "mokama" : "shivnar" , "shivnar" : "vikram", "vikram" : "happy" , "happy" : 1947}'
Y = json.loads(X)
M = json.loads(A)
O = json.loads(P)
print(Y["name"])

# print(A)



 