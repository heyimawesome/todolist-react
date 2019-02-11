from flask import Blueprint, jsonify, request

from project import db
from project.api.models import List

list_bp = Blueprint('list', __name__)


@list_bp.route('/', methods=['GET'])
def get_all_lists():
    response_object = {
        'status': 'success',
        'data': {
            'list': [lists.title for lists in List.query.all()]
        }
    }
    return jsonify(response_object), 200


@list_bp.route('/<list_id>', methods=['GET'])
def get_single_list(list_id):
    list_title = List.query.filter_by(id=int(list_id)).first()
    response_object = {
        'status': 'success',
        'data': {
            'title': list_title.title
        }
    }
    return jsonify(response_object), 200


@list_bp.route('/add', methods=['POST'])
def add_list():
    post_data = request.get_json()
    new_list = List(title=post_data.get('title'))
    db.session.add(new_list)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'List added.'
    }
    return jsonify(response_object), 201


@list_bp.route('/remove/<list_id>', methods=['GET'])
def remove_list(list_id):
    del_list = List.query.filter_by(id=int(list_id)).first()
    db.session.delete(del_list)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'List removed.'
    }
    return jsonify(response_object), 200
