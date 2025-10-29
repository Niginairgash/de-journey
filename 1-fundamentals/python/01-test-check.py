# 1. Create list of first letters from words:
words = ["apple", "banana", "cherry"]
alphabet = [item[0] for item in words]

# 2. Swap keys and values in dictionary:
original = {"a": 1, "b": 2, "c": 3}
#org = { original[key]:key for key in original}
org = { value:key for key, value in original.items()}
# → {1: "a", 2: "b", 3: "c"}

# 3. Find common elements in two lists:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
commonlist = list(set(list1) & set(list2))
# → [3, 4]
