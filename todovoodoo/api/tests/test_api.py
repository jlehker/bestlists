from test_plus import APITestCase


class TodoListTestCase(APITestCase):
    def setUp(self):
        self.user = self.make_user()
        self.client.force_login(user=self.user)

    def test_get(self):
        self.get("api:TodoList-list")
        self.response_200()


class ListItemTestCase(APITestCase):
    def setUp(self):
        self.user = self.make_user()
        self.client.force_login(user=self.user)

    def test_get(self):
        self.get("api:ListItem-list")
        self.response_200()
