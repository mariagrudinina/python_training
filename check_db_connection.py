from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_groups_of_contact(Contact(contact_id='177'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
