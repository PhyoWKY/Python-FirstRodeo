lucky_numbers = [4, 57, 67, 32, 45, 99, 89, 104]

friends = ["Jimmy", "Tom", "John", "Luke", "Kevin", "Pomni", "Pomni"]

#friends.extend(lucky_numbers)

#friends.append("Caine") for adding the new last element

friends.insert(1, "James")

friends.remove("Tom")

friends.sort()

#friends.pop() for removing the last element
#friends.clear() for deleting everything

print(friends)

print(friends.index("Pomni"))

print(friends.count("Pomni"))

lucky_numbers.sort()

lucky_numbers.reverse()

print(lucky_numbers)

friends2 = friends.copy()

print(friends2)