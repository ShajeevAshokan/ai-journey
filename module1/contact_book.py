def add_contact(contacts,name,phone):
    contacts[name] = phone

def search_contact(contacts,name):
    return contacts.get(name)

def delete_contact(contacts,name):
    if name in contacts:
        del contacts[name]
        return True
    return False

def list_contact(contacts):
    if not contacts:
        print("No Contacts yet")
        return
    for name,phone in sorted(contacts.items()):
        print(f"{name}: {phone}")


def main():
    contacts = {}
    while True:
        print("\n1. Add  2. Search 3. List 4. Delete 5. Quit")
        choice = input("Choose : ").strip()
        if choice == "1":
            name = input("Name : ").strip()
            phone = input("Phone : ").strip()
            add_contact(contacts,name,phone)
            print("Saved")
        elif choice == "2":
            name = input("Name : ").strip()
            phone = search_contact(contacts,name)
            print(phone if phone else"Not Found.")
        elif choice == "3":
            list_contact(contacts)
        elif choice == "4":
            name = input("Name : ").strip()
            print("Deleted." if delete_contact(contacts,name) else print("Not Found."))
        elif choice == "5":
            print("Good Bye!")
            break
        else:
            print("Invalid Choice")
main()


