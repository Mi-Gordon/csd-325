# Michael Gordon
# CSD325 Advanced Python
# Module 8.2

import json
from os import path

filename = 'student.json'
students = []

if path.isfile(filename) is False:
    raise Exception("File not found")

# Open the file and use the JSON load() function to load the file into a Python class list
with open(filename, 'r') as file:
    students = json.load(file)


# Create a function that loops through the .json class list and prints out each value
def student_values(file):
    for student in file:
        first_name = student['F_Name']
        last_name = student['L_Name']
        student_id = student['Student_ID']
        email = student['Email']

        print(f'{last_name}, {first_name} : ID = {student_id}, Email = {email}')


# Output notification to the user that this is the original Student list
print('\nThis is the original Student list.\n')


# Call your print function
student_values(students)


# Add your last name, first name, fictional ID, and email to the class list using append()
students.append({
    "F_Name": "Mike",
    "L_Name": "Gordon",
    "Student_ID": 99999,
    "Email": "migordon@my365.bellevue.edu"
})

# Output notification to the user that this is the updated Student list
print('\nThis is the updated Student list.\n')


# Call your print function
student_values(students)

# Use the JSON dump() function to append the new data to the .json file
with open(filename, 'w') as json_file:
    json.dump(students, json_file,
              indent=4,
              separators=(',', ': '))

# Output notification to the user that the .json file was updated
print('\nSuccessfully appended to the JSON file!\n')
