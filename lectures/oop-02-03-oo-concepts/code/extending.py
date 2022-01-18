#!/usr/bin/env python3
"""
Based on code from the OOP book.
"""


class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()   # class level  / shared

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __str__(self):
        return "({}, {}, {})".format(super().__str__(), self.name, self.email)

    def __repr__(self):
        return "({}, {}, {})".format(super().__repr__(), self.name, self.email)


t = ContactList([
    Contact("foo", "foo@bar.com"),
    Contact("foo2", "foo2@bar.com"),
])
t2 = ContactList()

print("t  : ", t.search("foo2"))
print("t2 : ", t.search("foo2"))
print(Contact.all_contacts)


class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
