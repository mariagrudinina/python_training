from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None, home_phone_number=None, mobile_phone_number=None, work_phone_number=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, group=None, address2=None, phone2=None, notes=None,
                 contact_id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.contact_id = contact_id

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s %s" % (self.contact_id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and self.firstname == other.firstname and self.lastname == other.lastname
