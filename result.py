result = {'sanjay-math': 50,
        'sameer-hindi': 40,
        'sanjay-hindi': 60,
        'mehul-math': 50,
        'sameer-math': 70,
        'sanjay-guj':80,
        'jay-guj': 44,
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
# task 1
student_marks = {}
for key, value in result.items():
    name = key.split('-')[0]
    if student_marks.get(name):
        student_marks[name] += value
    else:
        student_marks[name] = value
        student_marks.update({name: value})
print(student_marks)

# Task 2
# {'sanjay': [670, 3], 'sameer': [670, count], 'mehul': [670, count], 'jay': 464}
student_avg_marks = {}
for key, value in result.items():
    name = key.split('-')[0]
    if student_avg_marks.get(name):
        # student_marks[name] += value
        total = student_avg_marks[name][0] + value
        count = student_avg_marks[name][1] + 1
        student_avg_marks.update({name: [total, count]})
    else:
        lst = [value, 1]
        student_avg_marks[name] = lst

final_avg_marks = {}
for key, value in student_avg_marks.items():
    avg_marks = round(value[0] / value[1], 4)
    # final_avg_marks.update({key: avg_marks})
    final_avg_marks[key] = avg_marks

print(final_avg_marks)