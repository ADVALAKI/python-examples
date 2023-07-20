my_contact = {}

age = 30
# update dictionary
my_contact.update({'name': 'John Doe',
                     'age': age,
                        'phone': '123-456-7890',
                        'email': 'abc@demo.com'})

# print dictionary
print(my_contact)

# update key value
my_contact['age'] = 40
# my_contact.update({'age': 40})

print(my_contact)


# duplicate key
new_dict = {'name': 'John Doe',
 'age': 40, 'phone': '123-456-7890', 'email': 'abc@demo.com',
 'name': "Sachin"}

print(new_dict)


# delete key

del new_dict['name']

# clear dictionary
new_dict.clear()
print(new_dict)

# # delete dictionary
# del new_dict
#
# print(new_dict)


# loop over dictionary
for key, value in my_contact.items():
    print(f"{key} : {value}")

# get keys
# print(my_contact.keys())
for key in my_contact.keys():
    print(my_contact.get('dfdsfsfs', 0))


# student marks
student_marks = {'John': 90, 'Jane': 80, 'Jack': 70, 'Jill': 60}

total_marks = 0
for value in student_marks.values():
    total_marks += value
print(sum(student_marks.values()))

result = {'sanjay-math': 50,
        'sameer-hindi': 40,
        'sanjay-hindi': 60,
        'mehul-math': 50,
        'sameer-math': 70,
        'sanjay-guj':80,
        'jay-guj': 44,
        'sameer-guj': 75,
        'jay-math': 55,
        'mehul-guj': 60,
        'mehul-hindi': 70,
        'jay-hindi': 80,
        'mehul-english': 90,
        'sameer-science': 150,
        'sanjay-science': 160,
        'jay-english': 100,
        'sameer-english': 110,
        'sanjay-english': 120,
        'mehul-science': 130,
        'jay-science': 140,
        'mehul-social': 170,
        'jay-social': 180,
        'sameer-social': 190,
        'sanjay-social': 200,
		}

student_total_marks = {'sanjay': 400,
                       'jay': 600,
                       'mehul': 440}

student_avg_marks = {'sanjay': 66.66,
                     'jay': ''}




