from flask import Blueprint

from models import List

list_bp = Blueprint('list', __name__)


@list_bp.route('/ ', methods=['GET'])
def get_all_lists():
    pass


@list_bp.route('/<list_id>', methods=['POST'])
def get_single_list(list_id):
    pass


@list_bp.route('/add', methods=['POST'])
def add_list():
    pass


@list_bp.route('/remove/<list_id>', methods=['POST'])
def remove_list(list_id):
    pass
