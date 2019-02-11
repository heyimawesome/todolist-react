from project import db
from project.api.models import List, Item


def add_list(title):
    new_list = List(title=title)
    db.session.add(new_list)
    db.session.commit()
    return new_list


def add_item(item, list_id):
    new_item = Item(item=item, list_id=list_id)
    db.session.add(new_item)
    db.session.commit()
    return new_item
