# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Mary", lastname="Test", nickname="marytest", title="QA",
                               company="Test company",
                               address="Some address example\n644000, Omsk, Russia",
                               work_phone_number="+738120000000", email="test@example.com", bday="10",
                               bmonth="March", byear="1990", notes="Test"))
