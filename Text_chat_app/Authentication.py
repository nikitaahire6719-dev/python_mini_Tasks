class Auth:
    def __init__(self):
        self.users = {}          # username -> password
        self.current_user = None

    def register(self):
        username = input("New username: ")
        if username in self.users:
            print("❌ User already exists")
            return

        password = input("Password: ")
        self.users[username] = password
        print("✅ Registration successful")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        if self.users.get(username) == password:
            self.current_user = username
            print(f"✅ Logged in as {username}")
        else:
            print("❌ Invalid credentials")

    def logout(self):
        self.current_user = None
        print("👋 Logged out")


