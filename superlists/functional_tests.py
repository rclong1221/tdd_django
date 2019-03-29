from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, unittest

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item
        todo_box = self.browser.find_element_by_id('tdb')
        self.assertEqual(
            todo_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types make Dan clean the dishes
        todo_box.send_keys('Make Dan clean the dishes')

        # When she hits enter, the page updates, and now the page list shows
        # "1: make Dan clean the dishes"
        todo_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Make Dan clean the dishes' for row in rows)
        )

        # Another text box invites here to enter another to-do item
        # She enters "make Dan clean the gutters"
        self.fail('Finish the test...')

        # Audrey wonders if the site saved her list.  She sees a unique URL for her.

        # She visits the URL and sees that her list is satisfied.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
