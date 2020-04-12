import random

from model.group import Group


# def test_edit_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(name='Edited name', header='Edited header', footer='Edited footer'))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    group_rand = random.choice(old_groups)
    group = Group(name='Edited only name')
    group.id = group_rand.id
    group_rand.name = group.name  # меняю только имя случайной группы, так как сравниваем по id и имени
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header='Edited only header'))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
