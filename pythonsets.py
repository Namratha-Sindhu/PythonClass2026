# sets

set1 = {1,5,7}
set2 = {8,6,5}

res = set1 in set2
print(res)

print(set1.union(set2))
#print(set1.add({9,7,3,1}))
#print(set1.copy(set2))
print(set1.difference(set2))
print(set1.intersection(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.clear)
print(set2)
print(set1)
