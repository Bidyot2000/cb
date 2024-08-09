class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                self.display_contact(contact)

    def update_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            print("Updating contact details (leave blank to keep current value):")
            contact.name = input(f"Name ({contact.name}): ") or contact.name
            contact.phone = input(f"Phone ({contact.phone}): ") or contact.phone
            contact.email = input(f"Email ({contact.email}): ") or contact.email
            contact.address = input(f"Address ({contact.address}): ") or contact.address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contact(self, contact):
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            manager.update_contact(name)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

