friends = ["Apple","orange",5,345.06,False,"Aakash","Rohan"]
print(friends[0:8])
print(friends[0])
friends[0] = "Grapes" #Unlike strings lists are muteable
print(friends[0])
friends.append("Harry")
print(friends)

l1 = [5,3,90,2,34,9,34,12,78,45]
# l1.sort()
# l1.reverse()
# l1.insert(5,999)
# l1.pop(1)
l1.remove(5)
print(l1)