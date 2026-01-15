from Authentication import Auth
from Chat import Chat

class ChatApp:
    def __init__(self):
        self.auth = Auth()
        self.chat = Chat()

    def menu(self):
        while True:
            print("""
========= CHAT APPLICATION =========
1. Register
2. Login
3. Send Message
4. View Messages
5. Logout
6. Exit
""")
            choice = input("Choose: ")

            match choice:
                case "1":
                    self.auth.register()

                case "2":
                    self.auth.login()
                    if self.auth.current_user:
                        self.chat.add_user(self.auth.current_user)

                case "3":
                    if not self.auth.current_user:
                        print("❌ Login first")
                        continue

                    receiver = input("Send to: ")
                    message = input("Message: ")
                    self.chat.send_message(
                        self.auth.current_user,
                        receiver,
                        message
                    )

                case "4":
                    if not self.auth.current_user:
                        print("❌ Login first")
                        continue

                    self.chat.view_messages(self.auth.current_user)

                case "5":
                    self.auth.logout()

                case "6":
                    print("🚪 Exiting application")
                    break

                case _:
                    print("❌ Invalid choice")


if __name__ == "__main__":
    app = ChatApp()
    app.menu()
