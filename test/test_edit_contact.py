# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Mary Edited", lastname="Test Edited",
                                           address="Edited address example\n644999, Omsk, Russia",
                                           work_phone_number="+73812999999", email="test_edited@example.com"))
