from contact import Contact
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        for c in self.contacts:
            if c.phone == phone:
                print("Contact already exists.(●'◡'●)😊")
                return
        self.contacts.append(Contact(name, phone, email))
        print("📞☎️ Contact added successfully ☎️📞")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available☹️")
            return
        
        for c in self.contacts:
            print(f"Name: {c.name}, phone: {c.phone}, email: {c.email}")

    def update_contact(self, phone, new_name, new_email):
        for c in self.contacts:
            if c.phone == phone:
                c.name = new_name
                c.email = new_email
                print("contact updated successfully👍")
                return
        print("Contact not found🥲")    

    def delete_contact(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                self.contacts.remove(c)
                print("Contact deleted successfully🤗🤗")
                return
        print("Contact not found🥲")

            

