# Define the function to register a student for a course
def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    # Check if action is set to 'Add'
    if action == "Add":
        print(f"Student {student_id} - {first_name} {last_name} has been added to the course {course_id} - {course_name}.")
    else:
        print(f"Student {student_id} - {first_name} {last_name} enrolled in the course {course_id} - {course_name}. Action: {action}")

# Call the function using positional arguments
course_enrollment(1001, "Alice", "Smith", "CS101", "Introduction to Computer Science")

# Call the function a second time with a keyword argument 'Add'
course_enrollment(1001, "Alice", "Smith", "CS101", "Introduction to Computer Science", action="Add")



# Define the modified function to include multiple actions
def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    # Determine the message based on action type
    if action == "Amend":
        print(f"Amend: Student {student_id} - {first_name} {last_name}'s enrollment in course {course_id} - {course_name}.")
    elif action == "Delete":
        print(f"Delete: Student {student_id} - {first_name} {last_name} has been removed from course {course_id} - {course_name}.")
    else:  # Default action is Echo
        print(f"Echo: Student {student_id} - {first_name} {last_name} is enrolled in course {course_id} - {course_name}.")

# Call the function with different actions
course_enrollment(1002, "Bob", "Johnson", "MATH101", "Calculus I")  # Default action, Echo
course_enrollment(1002, "Bob", "Johnson", "MATH101", "Calculus I", action="Amend")
course_enrollment(1002, "Bob", "Johnson", "MATH101", "Calculus I", action="Delete")
