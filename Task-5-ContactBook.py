contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists. Use 'Update Contact' to modify it.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['Phone']:
            print(f"\nContact found: Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
    if not found:
        print("No contact found matching the query.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Current details: {contacts[name]}")
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    email = input("Enter new email (leave blank to keep current): ").strip()
    address = input("Enter new address (leave blank to keep current): ").strip()
    if phone:
        contacts[name]['Phone'] = phone
    if email:
        contacts[name]['Email'] = email
    if address:
        contacts[name]['Address'] = address

    print(f"Contact '{name}' updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def contact_management_system():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting,Thank you for using the Contact Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

contact_management_system()