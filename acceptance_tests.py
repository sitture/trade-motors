import unittest
from selenium import webdriver


class AdminLoginPageTest(unittest.TestCase):

    def setUp(self):
        self.admin_username = self.admin_password = 'admin'
        self.site_title = 'Global Trade Motors'
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/admin")

    def tearDown(self):
        self.browser.quit()

    def test_site_title(self):
        self.assertIn(
            self.site_title,
            self.browser.title
        )

    def test_site_header_name(self):
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEquals(
            self.site_title,
            header.text
        )


class AdminHomePageTest(unittest.TestCase):

    def setUp(self):
        self.site_title = 'Global Trade Motors'
        self.admin_username = self.admin_password = 'admin'
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000/admin")
        self.login()

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.find_element_by_id(
            'id_username').send_keys(self.admin_username)
        password = self.browser.find_element_by_id(
            'id_password')
        password.send_keys(self.admin_password)
        password.send_keys('\n')

    def test_site_branding_header(self):
        site_name = self.browser.find_element_by_id('site-name')
        self.assertEquals(
            self.site_title,
            site_name.text
        )


if __name__ == '__main__':
    unittest.main()
