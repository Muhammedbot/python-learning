# Day 14 - Contact Book with File Storage

import os

print("===== CONTACT BOOK =====")

# File to store contacts
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    """Load contacts from file"""
    contacts = []

    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as file:
                lines = file.readlines()

                for i in range(0, len(lines), 4):  # Each contact is 4 lines
                    if i + 3 < len(lines):
                        name = lines[i].strip().replace("Name: ", "")
                        phone = lines[i + 1].strip().replace("Phone: ", "")
                        email = lines[i + 2].strip().replace("Email: ", "")

                        contact = {
                            "name": name,
                            "phone": phone,
                            "email": email
                        }
                        contacts.append(contact)
        except:
            print("Error loading contacts file!")

    return contacts


def save_contacts(contacts):
    """Save contacts to file"""
    try:
        with open(CONTACTS_FILE, "w") as file:
            for contact in contacts:
                file.write(f"Name: {contact['name']}\n")
                file.write(f"Phone: {contact['phone']}\n")
                file.write(f"Email: {contact['email']}\n")
                file.write("---\n")
        return True
    except:
        print("Error saving contacts!")
        return False


def add_contact(contacts):
    """Add new contact"""
    print("\n--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    if save_contacts(contacts):
        print("✅ Contact added and saved!")

    return contacts


def view_contacts(contacts):
    """View all contacts"""
    if len(contacts) == 0:
        print("\nNo contacts yet!")
    else:
        print("\n===== ALL CONTACTS =====")
        for i in range(len(contacts)):
            c = contacts[i]
            print(f"\n{i + 1}. {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")


def search_contacts(contacts):
    """Search for contacts"""
    search = input("\nSearch for: ").lower()

    found = []
    for contact in contacts:
        if (search in contact['name'].lower() or 
            search in contact['phone'] or 
            search in contact['email'].lower()):
            found.append(contact)

    if len(found) == 0:
        print("\n❌ No contacts found!")
    else:
        print("\n--- Search Results ---")
        for c in found:
            print(f"\n• {c['name']}")
            print(f"  Phone: {c['phone']}")
            print(f"  Email: {c['email']}")


def delete_contact(contacts):
    """Delete a contact"""
    if len(contacts) == 0:
        print("\nNo contacts to delete!")
        return contacts

    print("\n--- Your Contacts ---")
    for i in range(len(contacts)):
        print(f"{i + 1}. {contacts[i]['name']}")

    try:
        num = int(input("\nDelete which contact? "))
        if 1 <= num <= len(contacts):
            deleted = contacts.pop(num - 1)
            if save_contacts(contacts):
                print(f"🗑️ Deleted: {deleted['name']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number!")

    return contacts


def edit_contact(contacts):
    """Edit existing contact"""
    if len(contacts) == 0:
        print("\nNo contacts to edit!")
        return contacts

    print("\n--- Your Contacts ---")
    for i in range(len(contacts)):
        print(f"{i + 1}. {contacts[i]['name']}")

    try:
                num = int(input("\nEdit which contact? "))
                if 1 <= num <= len(contacts):
                    contact = contacts[num - 1]

                    print(f"\nEditing: {contact['name']}")
                    print("(Press Enter to keep current value)")

                    new_name = input(f"Name [{contact['name']}]: ")
                    new_phone = input(f"Phone [{contact['phone']}]: ")
                    new_email = input(f"Email [{contact['email']}]: ")

                    # Update only if new value provided
                    if new_name:
                        contact['name'] = new_name
                    if new_phone:
                        contact['phone'] = new_phone
                    if new_email:
                        contact['email'] = new_email

                    if save_contacts(contacts):
                        print("✅ Contact updated!")
                else:
                    print("Invalid number!")
    except ValueError:
                
         print("Please enter a number!")

    return contacts
    
def export_contacts(contacts):
            """Export contacts to readable format"""
            if len(contacts) == 0:
                print("\nNo contacts to export!")
                return

            filename = input("\nExport filename (e.g., my_contacts.txt): ")

            try:
                with open(filename, "w") as file:
                    file.write("=" * 50 + "\n")
                    file.write("       MY CONTACT BOOK\n")
                    file.write("=" * 50 + "\n\n")

                    for i, contact in enumerate(contacts, 1):
                        file.write(f"{i}. {contact['name']}\n")
                        file.write(f"   Phone: {contact['phone']}\n")
                        file.write(f"   Email: {contact['email']}\n")
                        file.write("\n")

                    file.write("=" * 50 + "\n")
                    file.write(f"Total Contacts: {len(contacts)}\n")

                print(f"✅ Contacts exported to {filename}!")
            except:
                print("Error exporting contacts!")


        # Load existing contacts
        contacts = load_contacts()
print(f"Loaded {len(contacts)} contacts from file.")

        # Main menu
awhile True:
            print("\n" + "=" * 40)
            print("          CONTACT BOOK MENU")
            print("=" * 40)
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Edit Contact")
            print("5. Delete Contact")
            print("6. Export Contacts")
            print("7. Statistics")
            print("8. Exit")
            print("=" * 40)

            choice = input("\nChoice (1-8): ")

            if choice == "1":
                contacts = add_contact(contacts)

            elif choice == "2":
                view_contacts(contacts)

            elif choice == "3":
                search_contacts(contacts)

            elif choice == "4":
                contacts = edit_contact(contacts)

            elif choice == "5":
                contacts = delete_contact(contacts)

            elif choice == "6":
                export_contacts(contacts)

            elif choice == "7":
                # Statistics
                print("\n===== STATISTICS =====")
                print(f"Total contacts: {len(contacts)}")

                if len(contacts) > 0:
                    # Count domains
                    domains = {}
                    for contact in contacts:
                        if "@" in contact['email']:
                            domain = contact['email'].split("@")[1]
                            if domain in domains:
                                domains[domain] += 1
                            else:
                                domains[domain] = 1

                    if domains:
                        print("\nContacts by email domain:")
                        for domain, count in domains.items():
                            print(f"  {domain}: {count}")

            elif choice == "8":
                print("\n📱 Contacts saved! Goodbye!")
                break

            else:
                print("\n❌ Invalid choice! Pick 1-8.")
