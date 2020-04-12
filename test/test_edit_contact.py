# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Mary Edited", lastname="Test Edited",
                      address="Edited address example\n644999, Omsk, Russia",
                      work_phone_number="+73812999999", email="test_edited@example.com")
    contact_rand = random.choice(old_contacts)
    contact.contact_id = contact_rand.contact_id
    # меняю только firstname и lastname, так как сравниваем по id и этим значениям
    contact_rand.firstname = contact.firstname
    contact_rand.lastname = contact.lastname
    app.contact.edit_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
