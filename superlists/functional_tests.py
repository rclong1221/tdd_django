from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Audrey heard about this cool new website and goes to check it out
        self.browser.get('http://localhost:8000')

        # She notices the page header and title mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item
        self.fail("Finish the test...")

        # She types make Dan clean the dishes

        # When she hits enter, the page updates, and now the page list shows
        # "1: make Dan clean the dishes"

        # Another text box invites here to enter another to-do item
        # She enters "make Dan clean the gutters"

        # Audrey wonders if the site saved her list.  She sees a unique URL for her.

        # She visits the URL and sees that her list is satisfied.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
