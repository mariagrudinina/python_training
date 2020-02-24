# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="Mary", lastname="Test", nickname="marytest", title="QA",
                                company="Test company",
                                address="Some address example\n644000, Omsk, Russia",
                                work_phone_number="+738120000000", email="test@example.com", bday="10",
                                bmonth="March", byear="1990", notes="Test"))
    app.logout()
