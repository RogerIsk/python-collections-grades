https://github.com/dci-fbw-p-24-e02/python-basics-functions-decorators-i-RogerIskimport os

clear = lambda: os.system('clear')
clear()

# Task - Sort students by grade
# You have a list of students. Each student is made up of a dict containing a key with the name and a list with their subjects. 
# The list of subjects holds dictionaries with the subject name and the grade of the students. If a student has two or more Fs they will need to leave class.
# Implement a method that removes the students from the class that have more than two Fs.

students = [
  {
    'name': 'Peter', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'C'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Robin', 
    'subjects': [
      {'name': 'English', 'grade': 'D'},
      {'name': 'German', 'grade': 'B'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Michael', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'F'},
      {'name': 'Maths', 'grade': 'F'}
    ]
  },
]

def remove_students(students): # Function that checks if the student has more than 2 Fs and removes them from the list if they do
    for student in students:   # Loop through the students list
        count = 0
        for subject in student['subjects']:
            if subject['grade'] == 'F':
                count += 1
        if count >= 2:
            students.remove(student)
    return students

print("students = [") # Print the students list like the required output
for student in remove_students(students):
    print("  {")
    print(f"    'name': '{student['name']}',")
    print("    'subjects': [")
    for subject in student['subjects']:
        print(f"      {{'name': '{subject['name']}', 'grade': '{subject['grade']}'}}")
    print("    ]")
    print("  },")
print("]")
