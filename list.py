list = [30, 43, 40, 50 ,2, 60, 70, 80, 5, 90, 100]
new_list = []
for element in list:
    if element % 2 == 0:
        print(f"Element {element} is even")
    else:
        print(f"Element {element} is odd")

# for element in list:
#     total = element * 2
#     new_list.append(total)

new_list = [element * 2 for element in list]

print("new list=",new_list)

# add value in list
c = 200
list.append(c)
print(list)

# insert value in list
list.insert(0, c)
print(list)

# remove value in list
list.remove(c)
print(list)

# find length of list
print(len(list))

# find min value in list
print(min(list))

# find max value in list
print(max(list))

# reverse list
# list.reverse()
# print(list)

# sort list
# new_lst = sorted(list)
# print(new_lst)
#
# # sort using sort() method
# list.sort()
# print(list)


list2 = ["alpesh", "amit", "jay", 30, 545]

list3 = [[1,2,4],[[43,54,6],6,7], [8,9,10]]

list4 = [{'name': "alpesh", 'age': 30}, {'name': "amit", 'age': 40}, {'name': "jay", 'age': 50}]


for element in list4:

    print(element)


# tuple

# tuple = (1,2,3,4)
# print("tuple", tuple)

tuple2 = 3,
print(tuple2)

new_tuple = tuple(list)

print(new_tuple)

