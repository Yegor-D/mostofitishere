
counts = dict()
names = ['Aman','Aman','Aman','Aman', 'Bman', 'Bman', 'Bman', 'Bman', 'Cman', 'Dman', 'Dman', 'Dman', 'Eman']
for name in names:
  counts[name] = counts.get(name, 0) +
print(counts)

