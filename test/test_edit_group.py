from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name='Edited name', header='Edited header', footer='Edited footer'))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name='Edited only name'))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header='Edited only header'))
