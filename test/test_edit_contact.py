# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mary Edited", lastname="Test Edited",
                      address="Edited address example\n644999, Omsk, Russia",
                      work_phone_number="+73812999999", email="test_edited@example.com")
    index = randrange(len(old_contacts))
    contact.contact_id = old_contacts[index].contact_id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
