class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location

    def describe_user(self):
        """Print a concise overview of the user's details."""
        print(f"User Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Email: {self.email}\n"
              f"Username: {self.username}\n"
              f"Date of Birth: {self.date_of_birth}\n"
              f"Location: {self.location}\n")

    def greet_user(self):
        """Print a personalized welcome message."""
        print(f"Hello, {self.first_name}! Welcome to your profile.")


# Creating instances of the User class
user1 = User("Alice", "Smith", "alice.smith@example.com", "alice123", "1995-06-12", "New York")
user2 = User("Bob", "Johnson", "bob.johnson@example.com", "bob456", "1990-03-25", "Los Angeles")
user3 = User("Charlie", "Brown", "charlie.brown@example.com", "charlie789", "1988-11-07", "Chicago")

# Calling the methods for each user
for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
    print()  # Print an empty line for better separation
