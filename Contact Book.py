contact_list = []
#Add Contacts
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contact_list.append(contact)
    print("Contact added successfully!")
#View Contacts
def view_contacts():
    print("\n--- Contact List ---")
    if not contact_list:
        print("No contacts found.")
        return
    for i, contact in enumerate(contact_list, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
#Search Contacts
def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").lower()
    for contact in contact_list:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            return
    print("No matching contact found.")
#Update Contacts
def update_contact():
    print("\n--- Update Contact ---")
    target = input("Enter name of contact to update: ").lower()
    for contact in contact_list:
        if contact['name'].lower() == target:
            print("Leave field empty to keep current value.")
            new_phone = input(f"New phone (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"New email (current: {contact['email']}): ") or contact['email']
            new_address = input(f"New address (current: {contact['address']}): ") or contact['address']
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")
#Delete Contacts
def delete_contact():
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter name of contact to delete: ").lower()
    for contact in contact_list:
        if contact['name'].lower() == name_to_delete:
            contact_list.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
def show_menu():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        option = input("Choose an option (1-6): ")
        if option == '1':
            add_contact()
        elif option == '2':
            view_contacts()
        elif option == '3':
            search_contact()
        elif option == '4':
            update_contact()
        elif option == '5':
            delete_contact()
        elif option == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
show_menu()
