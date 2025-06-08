# Prompt the user to enter a student's name
student_name = input("Enter the student's name: ")  # Get input from user

# Dictionary storing student names as keys and their marks as values
students = {
    'Alok' : 90,
    'Aman' : 85,
    'Deepak' : 92,
    'Suryansh' : 80
}

# Check if the entered student name exists in the dictionary
if student_name in students:
    print(student_name, 'marks: ', students[student_name])  # Print marks if found

else:
    print('Student not found')  # Inform user if student is not in the dictionary