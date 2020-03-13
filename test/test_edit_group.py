from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name='Edited name', header='Edited header', footer='Edited footer'))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name='Edited only name'))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header='Edited only header'))
    app.session.logout()
