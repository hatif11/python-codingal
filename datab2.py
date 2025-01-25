name =("hatif","mehdi","ali","hatif")
print(name)

print(name[0])
print(name[2])
print(name[-1])

print(name[0:3])

for name in name:
    print(name)

print(name.count("hatif"))

# print(name.index("ali"))
 #######################################
numerics ={1,2,3,3,4,5,6,6,8,}
print(numerics)
numerics.add(7)
print(numerics)
numerics.remove(8)
print(numerics)

set1= {1,2,5}
set2= {5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set2.difference(set1))
print(set1.difference(set2))