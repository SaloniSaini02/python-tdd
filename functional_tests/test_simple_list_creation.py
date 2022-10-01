from calendar import c
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os
import unittest
from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_for_one_user(self):

        #Edith has heard about a cool to do app. She goes 
        #to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices that the page title and header mention to do lists

        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element("tag name", "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to do list item straight away
        inputbox = self.browser.find_element("id", "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy Peacock feathers" into a text box 
        inputbox.send_keys("Buy peacock feathers")

        #When she enters the page updates and now it lists 
        # "1. Buy peacock feathers" as an item in a to do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        # table = self.browser.find_element("id", "id_list_table")
        # rows = table.find_elements("tag name", "tr")
        
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # There is still a a text box inviting her to add another item. She enters 
        # "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element("id", "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # The page updates and now shows both her items
      
        # self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        

        # Satisfied she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element("id", "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user Francis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through the cookies etc

        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element('tag name', 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith
        inputbox = self.browser.find_element("id", "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again there is no trace of Ediths list
        page_text = self.browser.find_element("tag name", "body").text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied they both go back to sleep

if __name__ == "__main__":
    unittest.main(warnings="ignore")

