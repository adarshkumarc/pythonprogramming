list1 = ["apple", "banana", "orange", "papaya", "papaya"]
print(list1)
# append()
list1.append("luly")  # last mai value add karta hai
print(list1)
# extend()
# two list value ko merge karta hai
list1.extend(["mango", "pineAPPLE"])
print(list1)
# index
print(list1.index("luly"))
print(list1)
# insert
print(list1.insert(1, "mmm"))
print(list1)
# count duplicate count karta hai
list2 = [1, 2, 3, 4, 4, 55, 66, 6, 7, 8, 9, "aa", "aa", "v"]

print(list2.count("aa"))
print(list2.count(4))
# remove
print(list2.remove(9))
print(list2)
# pop index ke according delete karta hai
print(list2.pop(2))
print(list2)
# reverse
print(list2.reverse())
print(list2)
# sort
# accending order
list3 = [1, 22, 3, 4, 4, 5, 5, 6, 65, 3, 2, 9, 1, 0]
list3.sort()
print(list3)
# reverse sorting
list3.sort(reverse=True)
print(list3)
