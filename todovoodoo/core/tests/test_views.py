from test_plus import TestCase


class MasterListTests(TestCase):
    def setUp(self):
        self.user = self.make_user()

    def test_login_require(self):
        """ make sure you need to login to see master list """
        self.assertLoginRequired("core:master-list")

    def test_masterlist_get(self):
        """ test we can get the master list """
        url = self.reverse("core:master-list")

        with self.login(username=self.user):
            self.get(url)
            self.response_200()
