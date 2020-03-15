from selenium.webdriver.support.ui import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if len(wd.find_elements_by_link_text(
                "home page")) > 0:  # если есть ссылка, предлагающая перейти на Home page, то кликаем ее
            wd.find_element_by_link_text("home page").click()
        else:
            self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("work", contact.work_phone_number)
        self.change_field_value("email", contact.email)
        if contact.bday and contact.bmonth and contact.byear:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
            wd.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
            wd.find_element_by_xpath("//option[@value='" + contact.bmonth + "']").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("(//a[img[@title='Edit']])[1]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()  # добавила, иначе в new_contacts сохранялся удаленный контакт
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            i = 1
            for element in wd.find_elements_by_name("entry"):
                last_name = wd.find_element_by_xpath('((//tr[@name="entry"])/td[2])[' + str(i) + ']').text
                first_name = wd.find_element_by_xpath('((//tr[@name="entry"])/td[3])[' + str(i) + ']').text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, contact_id=contact_id))
                i += 1
        return list(self.contact_cache)
