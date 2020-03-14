from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name='Edited name', header='Edited header', footer='Edited footer'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name='Edited only name'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header='Edited only header'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
