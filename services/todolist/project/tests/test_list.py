import json
import unittest

from project.tests.base import BaseTestCase
from utils import add_list


class TestListBlueprint(BaseTestCase):
    def test_get_all_lists(self):
        add_list('This is a test list')
        add_list('This is also a test list')

        response = self.client.get('/list/')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['data']['list']), 2)
        self.assertIn(
            'This is a test list',
            data['data']['list'][0]
        )
        self.assertIn(
            'This is also a test list',
            data['data']['list'][1]
        )

    def test_get_single_list(self):
        add_list('This is a test list')
        response = self.client.get('/list/1')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['data']['title'], 'This is a test list')

    def test_add_list(self):
        response = self.client.post(
            '/list/add',
            data=json.dumps({
                'title': 'test-list'
            }),
            content_type='application/json'
        )

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'List added.')
        self.assertEqual(response.content_type, 'application/json')

    def test_remove_list(self):
        add_list('This is a test list')
        test_list = add_list('This is also a test list')
        response = self.client.get('/list/')
        data = json.loads(response.data.decode())
        self.assertEqual(len(data['data']['list']), 2)

        response = self.client.get(f'/list/remove/{test_list.id}')
        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'List removed.')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/list/')
        data = json.loads(response.data.decode())
        self.assertEqual(len(data['data']['list']), 1)


if __name__ == '__main__':
    unittest.main()
