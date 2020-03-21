# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact
from test.test_add_group import random_string


def random_numbers(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))]) + "a.com"


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 10),
            company=random_string("company", 15),
            address=random_string("address", 30),
            work_phone_number=random_numbers("+", 10), email=random_email("email", 5), bday="10",
            bmonth="March", byear="1990", notes=random_string("firstname", 30))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
