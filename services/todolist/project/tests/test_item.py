import json

from project.api.models import Item
from project.tests.base import BaseTestCase
from utils import add_item, add_list


class TestItemBlueprint(BaseTestCase):
    def test_get_single_item(self):
        test_list = add_list('Test List')
        test_item = add_item('Test item #1', test_list.id)

        response = self.client.get(f'/item/{test_item.id}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['data']['list'][0]['item']), 1)
        self.assertEqual(data['data']['list'][0]['name'], 'Test List')
        self.assertEqual(data['data']['list'][0]['item'][0], 'Test item #1')

    def test_get_all_list_items(self):
        test_list = add_list('Test List')
        add_item('Test item #1', test_list.id)
        add_item('Test item #2', test_list.id)

        response = self.client.get(f'/item/list/{test_list.id}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data']['list'][0]['name'], 'Test List')
        self.assertEqual(len(data['data']['list'][0]['item']), 2)
        self.assertEqual(data['data']['list'][0]['item'][0], 'Test item #1')
        self.assertEqual(data['data']['list'][0]['item'][1], 'Test item #2')

    def test_add_item(self):
        test_list = add_list('Test List')

        response = self.client.post(
            '/item/add',
            data=json.dumps({
                'item': 'Test item #1',
                'list_id': test_list.id
            }),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Item added.')

        test_item = Item.query.filter_by(id=1).first()
        self.assertEqual(test_item.item, 'Test item #1')
        self.assertEqual(test_item.list_id, test_list.id)

    def test_delete_item(self):
        pass

    def test_complete_item(self):
        pass

    def test_uncomplete_item(self):
        pass
