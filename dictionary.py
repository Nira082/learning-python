# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23
# }
# # print(marks,type(marks))
# print(marks["Harry"])

#Dictionary methods
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
# print(marks.items())
# print(marks.keys())
#print(marks.values())
marks.update({"Harry":99})
print(marks.get("Harry"))

#Note 
print(marks.get("Harry2")) #prints None
print(marks["Harry2"]) #Returns an error