class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0  # New attribute to track login attempts

    def describe_user(self):
        """Print a concise overview of the user's details."""
        print(f"User Profile:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Email: {self.email}\n"
              f"Username: {self.username}\n"
              f"Date of Birth: {self.date_of_birth}\n"
              f"Location: {self.location}\n"
              f"Login Attempts: {self.login_attempts}\n")  # Include login attempts

    def greet_user(self):
        """Print a personalized welcome message."""
        print(f"Hello, {self.first_name}! Welcome to your profile.")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0


# Create an instance of the User class
user = User("Alice", "Smith", "alice.smith@example.com", "alice123", "1995-06-12", "New York")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the current number of login attempts
print(f"Login attempts after incrementing: {user.login_attempts}")

# Reset the login attempts
user.reset_login_attempts()

# Print the number of login attempts after resetting
print(f"Login attempts after resetting: {user.login_attempts}")
