dict = {"a": 1, "b": 2, "c": 3}
dict1 = {"a": 1, "b": 2, "c": 3}
result = {}
for key, value in dict.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

for key, value in dict1.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)
