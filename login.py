def login(username, password):
    if username and password:
        return "Login successful"
    return "Invalid credentials"

print(login("student", "1234"))
