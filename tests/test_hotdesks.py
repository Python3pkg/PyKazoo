import pykazoo.hotdesks
import pykazoo.restrequest
from unittest import TestCase
from unittest.mock import create_autospec

mock_rest_request = create_autospec(pykazoo.restrequest.RestRequest)


class TestHotdesks(TestCase):
    def setUp(self):
        self.mock_rest_request = mock_rest_request

        self.hotdesks = pykazoo.hotdesks.Hotdesks(
            self.mock_rest_request)

        self.account_id = '123joj34af83jf438afj43af'
        self.user_id = '123123213rhh798ahfhewa'
        self.data = {'test': 'data'}
        self.params = {'test': 'params'}

    def test_get_hotdesks_request_call(self):
        self.hotdesks.get_hotdesks(self.account_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users/hotdesks',
                                                      self.params)

    def test_get_hotdesks_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.hotdesks.get_hotdesks(self.account_id, self.params)

        assert return_data is self.data

    def test_get_hotdesk_request_call(self):
        self.hotdesks.get_hotdesk(self.account_id, self.user_id, self.params)
        self.mock_rest_request.get.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users/' +
                                                      self.user_id +
                                                      '/hotdesks', self.params)

    def test_get_hotdesk_returns_dict(self):
        self.mock_rest_request.get.return_value = self.data
        return_data = self.hotdesks.get_hotdesk(self.account_id, self.user_id,
                                                self.params)

        assert return_data is self.data

    def test_create_hotdesk_request_call(self):
        self.hotdesks.create_hotdesk(self.account_id, self.user_id, self.data)
        self.mock_rest_request.put.assert_called_with('accounts/' +
                                                      self.account_id +
                                                      '/users/' +
                                                      self.user_id +
                                                      '/hotdesks', self.data)

    def test_create_hotdesk_returns_dict(self):
        self.mock_rest_request.put.return_value = self.data
        return_data = self.hotdesks.create_hotdesk(self.account_id,
                                                   self.user_id, self.data)

        assert return_data is self.data

    def test_update_hotdesk_request_call(self):
        self.hotdesks.update_hotdesk(self.account_id, self.user_id, self.data)
        self.mock_rest_request.post.assert_called_with('accounts/' +
                                                       self.account_id +
                                                       '/users/' +
                                                       self.user_id +
                                                       '/hotdesks',
                                                       self.data)

    def test_update_hotdesk_returns_dict(self):
        self.mock_rest_request.post.return_value = self.data
        return_data = self.hotdesks.update_hotdesk(self.account_id,
                                                   self.user_id, self.data)

        assert return_data is self.data

    def test_delete_hotdesk_request_call(self):
        self.hotdesks.delete_hotdesk(self.account_id, self.user_id)
        self.mock_rest_request.delete.assert_called_with('accounts/' +
                                                         self.account_id +
                                                         '/users/' +
                                                         self.user_id +
                                                         '/hotdesks')

    def test_delete_hotdesk_returns_dict(self):
        self.mock_rest_request.delete.return_value = self.data
        return_data = self.hotdesks.delete_hotdesk(self.account_id,
                                                   self.user_id)

        assert return_data is self.data
