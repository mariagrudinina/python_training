import re
from random import randrange

from model.contact import Contact


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", work_phone_number="+73812999999", home_phone_number="+12345678",
                                   email="test1@dev.com", email3="test3@dev.com", address="test address\n644000"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone_number == contact_from_edit_page.home_phone_number
    assert contact_from_view_page.mobile_phone_number == contact_from_edit_page.mobile_phone_number
    assert contact_from_view_page.work_phone_number == contact_from_edit_page.work_phone_number
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone_number, contact.mobile_phone_number,
                                        contact.work_phone_number, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
