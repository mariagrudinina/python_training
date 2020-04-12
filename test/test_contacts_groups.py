import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups_of_not_this_contact = orm.get_groups_of_not_contact(contact)
    if len(groups_of_not_this_contact) == 0:  # если в системе нет групп, к которым не принадлежит контакт, создаем
        app.group.create(Group(name="Test"))
        groups_of_not_this_contact = orm.get_groups_of_not_contact(contact)
    new_group = random.choice(groups_of_not_this_contact)
    app.contact.add_group(contact.contact_id, new_group.id)
    groups_of_contact = orm.get_groups_of_contact(contact)
    groups_of_not_this_contact = orm.get_groups_of_not_contact(contact)
    assert new_group in groups_of_contact
    assert new_group not in groups_of_not_this_contact


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups_of_contact = orm.get_groups_of_contact(contact)
    if len(groups_of_contact) == 0:  # если у контакта нет группы, добавим её
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Test"))
        all_groups = db.get_group_list()
        new_group = random.choice(all_groups)
        app.contact.add_group(contact.contact_id, new_group.id)
        groups_of_contact = orm.get_groups_of_contact(contact)
    group_to_remove_from = random.choice(groups_of_contact)
    app.contact.remove_group(contact.contact_id, group_to_remove_from.id)
    groups_of_contact = orm.get_groups_of_contact(contact)
    groups_of_not_this_contact = orm.get_groups_of_not_contact(contact)
    assert group_to_remove_from not in groups_of_contact
    assert group_to_remove_from in groups_of_not_this_contact
