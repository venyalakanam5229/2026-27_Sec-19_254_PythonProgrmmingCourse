list_data = [11, 12, 12, 13, 11, 13, 14]
unique = []
for item in list_data:
    if item not in unique:
        unique.append(item)
print("Original:", list_data)
print("Non Repetition:", unique)
