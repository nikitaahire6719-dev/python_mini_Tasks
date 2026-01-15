class Chat:
    def __init__(self):
        self.messages = {}   # username -> list of messages

    def add_user(self, username):
        if username not in self.messages:
            self.messages[username] = []

    def send_message(self, sender, receiver, message):
        if receiver not in self.messages:
            print("❌ Receiver does not exist")
            return

        self.messages[receiver].append(
            f"From {sender}: {message}"
        )
        print("📨 Message sent")

    def view_messages(self, username):
        inbox = self.messages.get(username, [])

        if not inbox:
            print("📭 No messages")
            return

        print("\n📨 Inbox:")
        for msg in inbox:
            print(msg)
