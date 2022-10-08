from calendar import c
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os
import unittest
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):

        #  Edith goes to the home page and accidently tried to submit
        # an empty list item. She hits Enter on the empty input box
        
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        # The browser interceps the request and does not load the list page
        self.wait_for(lambda:self.browser.find_elements("css selector", '#id_text:invalid'))
        # She tries again with some text for the item and the error disappears
        self.get_item_input_box().send_keys("Buy milk")
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for(lambda:self.browser.find_elements("css selector", '#id_text:valid'))

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Perversely she now decides to submit a second blank list item 
        self.get_item_input_box().send_keys(Keys.ENTER)
        # Again, the browser will not comply 
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for(lambda:self.browser.find_elements("css selector", '#id_text:invalid'))
        
        # self.wait_for(lambda: self.assertEqual(self.browser.find_element("css selector", '.has-error').text,
        #  "You can't have an empty list item"
        # ))
        # And she can correct it by filling some text in 

        self.get_item_input_box().send_keys("Make tea")
        self.wait_for(lambda:self.browser.find_elements("css selector", '#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")


if __name__ == "__main__":
    unittest.main(warnings="ignore")

