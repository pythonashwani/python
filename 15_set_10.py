Frozenset = frozenset([1, 2, 3, 4, 5])
print(type(Frozenset))
print("\nprinting the content of frozen set...")
for i in Frozenset:
    print(i)
# gives an error since we cannot change the content of Frozenset after creation
Frozenset.add(6)