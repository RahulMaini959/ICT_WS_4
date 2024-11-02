def collect_courses(student_id, student_name):
    # Initialize a list to store course IDs
    courses = []
    
    print(f"Enrolling courses for Student ID: {student_id}, Name: {student_name}")
    
    # Loop to collect four course IDs
    for i in range(4):
        course_id = input(f"Enter course ID for course {i+1}: ")
        courses.append(course_id)
    
    # Collect semester and year information
    semester = input("Enter the semester (e.g., S1, S2): ")
    year = input("Enter the year (e.g., 2024): ")
    
    # Display the summary of the enrolled courses
    print(f"\nStudent {student_id} - {student_name} is enrolled in the following courses:")
    for course in courses:
        print(f"- Course ID: {course}")
    print(f"Semester: {semester}, Year: {year}")

# Example of how the function might be called
collect_courses(1001, "Alice Smith")


def store_course_info(**courses):
    # Dictionary to hold course ID as key and course name as value
    course_dict = {}
    
    for course_id, course_name in courses.items():
        course_dict[course_id] = course_name
    
    # Print the dictionary for confirmation
    print("\nStored Course Information:")
    for course_id, course_name in course_dict.items():
        print(f"Course ID: {course_id}, Course Name: {course_name}")
    
    return course_dict

# Example of how the function might be called
stored_courses = store_course_info(CS101="Introduction to Computer Science", MATH101="Calculus I",
                                   PHY101="General Physics I", CHEM101="General Chemistry I")
