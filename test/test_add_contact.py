# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mary", lastname="Test", nickname="marytest", title="QA",
                      company="Test company",
                      address="Some address example\n644000, Omsk, Russia",
                      work_phone_number="+738120000000", email="test@example.com", bday="10",
                      bmonth="March", byear="1990", notes="Test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
