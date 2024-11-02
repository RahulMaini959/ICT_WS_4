class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0  # Default value for enrolled students
        self.audit_log = []  # List to store changes in enrolled students

    def describe_classroom(self):
        """Print the classroom details."""
        print(f"Classroom Name: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Number of Seats: {self.seats_in_class}")
        print(f"Students Enrolled: {self.students_enrolled}")

    def checksize_classroom(self):
        """Check if the classroom has enough seats for enrolled students."""
        if self.students_enrolled <= self.seats_in_class:
            print(f"The classroom has enough seats for {self.students_enrolled} enrolled students.")
        else:
            print(f"The classroom does not have enough seats for {self.students_enrolled} enrolled students.")

    def set_number_enrolled(self, number):
        """Set the number of enrolled students."""
        self.students_enrolled = number
        self.audit_log.append(f"Set enrolled students to {number}.")
        print(f"Number of enrolled students set to: {self.students_enrolled}")

    def update_number_enrolled(self, number):
        """Update the number of enrolled students and log the change."""
        previous_number = self.students_enrolled
        self.students_enrolled = number
        self.audit_log.append(f"Updated enrolled students from {previous_number} to {number}.")
        print(f"Number of enrolled students updated to: {self.students_enrolled}")

    def print_audit_log(self):
        """Print the audit log of changes."""
        print("\nAudit Log:")
        for log in self.audit_log:
            print(log)


# Create an instance of Classroom
classroom = Classroom("Physics Lab", "Building A, Room 101", 30)

# Print initial number of enrolled students
print(f"Initial number of enrolled students: {classroom.students_enrolled}")

# Change the number of enrolled students and print it
classroom.students_enrolled = 15
print(f"Updated number of enrolled students: {classroom.students_enrolled}")

# Set a new number of enrolled students using the method
classroom.set_number_enrolled(20)

# Update the number of enrolled students using the method
classroom.update_number_enrolled(25)

# Print the audit log of changes
classroom.print_audit_log()

# Call the describe_classroom method to see all details
classroom.describe_classroom()
