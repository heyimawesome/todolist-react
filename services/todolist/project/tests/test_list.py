import json

from project.tests.base import BaseTestCase


class TestListBlueprint(BaseTestCase):
    def test_get_all_lists(self):
        pass

    def test_get_single_list(self):
        pass

    def test_add_list(self):
        response = self.client.post(
            '/list/add',
            data=json.dumps({
                'name': 'test-list'
            }),
            content_type='application/json'
        )

        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'List added.')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_remove_list(self):
        pass
