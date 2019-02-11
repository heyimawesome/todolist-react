from flask import Blueprint, jsonify, request

from project import db
from project.api.models import Item, List

item_bp = Blueprint('item', __name__)


@item_bp.route('/<item_id>', methods=['GET'])
def get_single_item(item_id):
    list_item = Item.query.filter_by(id=item_id).first()
    list_title = List.query.filter_by(id=list_item.list_id).first()
    response_object = {
        'status': 'success',
        'data': {
            'list': [
                {
                    'name': list_title.title,
                    'item': [list_item.item]
                }
            ]
        }
    }

    return jsonify(response_object), 200


@item_bp.route('/list/<list_id>', methods=['GET'])
def get_all_list_items(list_id):
    list_title = List.query.filter_by(id=list_id).first()

    response_object = {
        'status': 'success',
        'data': {
            'list': [
                {
                    'name': list_title.title,
                    'item': [items.item
                             for items in Item.query
                                              .filter_by(list_id=list_id).all()
                             ]
                }
            ]
        }
    }

    return jsonify(response_object), 200


@item_bp.route('/add', methods=['POST'])
def add_item():
    post_data = request.get_json()
    new_item = Item(item=post_data.get('item'),
                    list_id=(post_data.get('list_id'))
                    )
    db.session.add(new_item)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Item added.'
    }

    return jsonify(response_object), 201


@item_bp.route('/delete/<item_id>', methods=['GET'])
def delete_item(item_id):
    pass


@item_bp.route('/complete/<item_id>', methods=['GET'])
def complete_item(item_id):
    pass


@item_bp.route('/uncomplete/<item_id>', methods=['GET'])
def uncomplete_item(item_id):
    pass
