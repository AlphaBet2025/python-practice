"""
PROJECT 6 (simplified): CONTACT BOOK (using a class)
========================================================
Teaches: what a class actually is -- a template for making objects
that each carry their own data. Compare this to project 5, which
stored tasks as plain strings in a list.
"""


class Contact:
    # This runs every time you create a new Contact(...)
    def __init__(self, name, phone):
        self.name = name    # "self" just means "this specific contact"
        self.phone = phone

    def show(self):
        print(self.name, "-", self.phone)


def main():
    contacts = []  # a list that will hold Contact objects

    while True:
        print("\n1) Show contacts  2) Add contact  3) Quit")
        choice = input("Choose: ")

        if choice == "1":
            for contact in contacts:
                contact.show()   # each contact knows how to print itself

        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            new_contact = Contact(name, phone)  # creates one Contact object
            contacts.append(new_contact)

        elif choice == "3":
            break

        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()
