name:list[str]=['irtiza', 'Ahad', 'hassan', 'asif']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
names:list[str]=['irtiza','Ahad','hassan','asif']
for name in names:
 print(f"maira name {name} hai")
cars:list[str]=['Corolla','khota reery','rolex','Honda City']
for car in cars:
 print(f"I would like to own a {car}")
guest:list[str]=['irtiza','Ahad','ayesha','daniya']
for guests in guest:
 print(f"Dear {guests} please come my home and taste my food")
guest:list[str]=['minahil','alizay','irtiza']
message="i invited you tonight dinner"
for guest1 in guest:
    print(f"{guest1} {message}")
print("\nafter new member:")
guest[2] ="ibrahm"
print("irtiza i dont invite you today this reason maina tumha nikal maraa dinner sai")
print(guest)
for guest1 in guest:
    print(f"{guest1} {message}")
guest:list[str]=['Ahad','Mubashir','Muzamil']

print(guest)

guest.insert(0,"Saif")

print(guest)

guest.insert(2,"Abdullah")

print(guest)

guest.append("zainab")

print(guest)

for guest1 in guest:

 print(f"{guest1} i invite you tonight dinner")
 guest:list[str]=['Ahad','Mubashir','Muzamil','Abdullah','Arslan']

print(guest)

print("I can invite only two people of the dinner")

guest1 = guest.pop()
guest2 = guest.pop()
guest3 = guest.pop()


print(f"sorry {guest1,guest2,guest3} i can not invited them into the dinner")

print(f"{guest} they still invited")

del guest[0]
del guest[0]

print(f"{guest} they have an empty list at the end of your program")
places:list[str]=['lahore','karachi','multan','brooklyne','newyork']
print("Original list :")
print(places)
print("By using sorted method :")
print(sorted(places))
print("By using reverse sorted method")
print(sorted(places ,reverse=True))
print("list is still in its original order :")
print(places)
print("using reverse method :")
places.reverse()
print(places)
print("using reverse method again :")
places.reverse()
print(places)
print("original list print again:")
print(places)
print("sorted list : ")
print(sorted(places))
places:list[str]=['lahore','karachi','multan','brooklyne','newyork']
print("Original list :")
print(places)
print("By using sorted method :")
print(sorted(places))
print("By using reverse sorted method")
print(sorted(places ,reverse=True))
print("list is still in its original order :")
print(places)
print("using reverse method :")
places.reverse()
print(places)
print("using reverse method again :")
places.reverse()
print(places)
print("original list print again:")
print(places)
print("sorted list : ")
print(sorted(places))
cities.remove("Daroghawala")
print(cities)
print("9 del method")
del cities[2]
print(cities)
print("10 count method")
cities.count(3)
print(cities)
print("11 index method")
cities.index("multan")
print(cities)
print("12 copy method")
cities.copy()
print(cities)
print("13 clear method")
cities.clear()
print(cities)
print("extend method")
cities.extend(cities1)
print(cities)
city:list[str]=['lahore','sahiwal','badami bagh','jallo moor']

print(city[4])
