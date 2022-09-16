spam = {'color' : 'red', 'age' : 42}

# .value() mehtod return all value's of each key in Dict
print("All value are:")
for v in spam.values():
    print(v)

# .key() mehtod return key's in Dict
print("All key's are:")
for k in spam.keys():
    print(k)

# .items() mehtod return all item in Dict
print("All items in Dict: ")
for i in spam.items():
    print(i)
for k, v in spam.items():
    print("Key: " + k + ', Value: ' + str(v))