# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mary Edited", lastname="Test Edited",
                      address="Edited address example\n644999, Omsk, Russia",
                      work_phone_number="+73812999999", email="test_edited@example.com")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
