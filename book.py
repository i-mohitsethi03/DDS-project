import os
import json

class ContactNode:
    """A node in the linked list representing a single contact."""
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None

    def to_dict(self):
        """Converts the contact data to a dictionary for JSON serialization."""
        return {"name": self.name, "phone": self.phone, "email": self.email}

class ContactBook:
    """Manages the linked list of contacts with file persistence."""
    def __init__(self, filename="contacts.json"):
        self.head = None
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        """Loads contacts from the file and builds the linked list."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    contacts_data = json.load(f)
                    for contact in contacts_data:
                        # Insert contacts one by one to maintain alphabetical order
                        self.insert_contact(contact['name'], contact['phone'], contact['email'])
                except (json.JSONDecodeError, FileNotFoundError):
                    print("Error loading contacts. Starting with an empty contact book.")
                    self.head = None

    def save_contacts(self):
        """Saves all contacts from the linked list to the file."""
        contacts_list = []
        current = self.head
        while current:
            contacts_list.append(current.to_dict())
            current = current.next
        
        with open(self.filename, 'w') as f:
            json.dump(contacts_list, f, indent=4)
        print("Contacts saved successfully.")

    def insert_contact(self, name, phone, email):
        """Inserts a new contact while maintaining alphabetical order by name."""
        new_node = ContactNode(name, phone, email)

        if not self.head or name.lower() < self.head.name.lower():
            new_node.next = self.head
            self.head = new_node
            print(f"Contact '{name}' added.")
            self.save_contacts()
            return

        current = self.head
        while current.next and current.next.name.lower() < name.lower():
            current = current.next

        new_node.next = current.next
        current.next = new_node
        print(f"Contact '{name}' added.")
        self.save_contacts()

    def search_contact(self, name):
        """Searches for a contact by name and returns the node or None."""
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print("\n--- Contact Found ---")
                print(f"Name: {current.name}")
                print(f"Phone: {current.phone}")
                print(f"Email: {current.email}")
                print("---------------------")
                return current
            current = current.next
        print(f"Contact '{name}' not found.")
        return None

    def update_contact(self, name, new_phone=None, new_email=None):
        """Updates the phone and/or email of an existing contact."""
        contact = self.search_contact(name)
        if contact:
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            print(f"Contact '{name}' updated.")
            self.save_contacts()

    def delete_contact(self, name):
        """Deletes a contact by name."""
        if not self.head:
            print("Contact book is empty.")
            return

        # Case 1: Deleting the head node
        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            print(f"Contact '{name}' deleted.")
            self.save_contacts()
            return

        # Case 2: Deleting a node in the middle or end
        current = self.head
        while current.next and current.next.name.lower() != name.lower():
            current = current.next

        if current.next:
            current.next = current.next.next
            print(f"Contact '{name}' deleted.")
            self.save_contacts()
        else:
            print(f"Contact '{name}' not found.")

    def view_all_contacts(self):
        """Displays all contacts in the contact book."""
        if not self.head:
            print("The contact book is empty.")
            return

        print("\n--- All Contacts ---")
        current = self.head
        while current:
            print(f"Name: {current.name}, Phone: {current.phone}, Email: {current.email}")
            current = current.next
        print("---------------------\n")

def main():
    contact_book = ContactBook()

    print("\n--- Contact Book Manager ---")
    print("Commands:")
    print("  1. Add a new contact")
    print("  2. Search for a contact")
    print("  3. Update a contact")
    print("  4. Delete a contact")
    print("  5. View all contacts")
    print("  6. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-6): ")

            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                email = input("Enter contact email: ")
                contact_book.insert_contact(name, phone, email)
            
            elif choice == '2':
                name = input("Enter name to search: ")
                contact_book.search_contact(name)

            elif choice == '3':
                name = input("Enter name of contact to update: ")
                new_phone = input("Enter new phone (leave blank to skip): ")
                new_email = input("Enter new email (leave blank to skip): ")
                contact_book.update_contact(name, new_phone or None, new_email or None)

            elif choice == '4':
                name = input("Enter name of contact to delete: ")
                contact_book.delete_contact(name)

            elif choice == '5':
                contact_book.view_all_contacts()
            
            elif choice == '6':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
