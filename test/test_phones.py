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


def test_all_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test", work_phone_number="+73812999999", home_phone_number="+12345678",
                                   email="test1@dev.com", email3="test3@dev.com", address="test address\r\n644000"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list_with_phones_emails_address()
    assert len(contact_from_home_page) == len(contact_from_db)
    contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    for i in range(len(contact_from_db)):
        assert contact_from_home_page[i].contact_id == contact_from_db[i].contact_id
        assert contact_from_home_page[i].all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_db[i])


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
