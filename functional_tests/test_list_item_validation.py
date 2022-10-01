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

        # The home page refreshes and there is an error message saying 
        # that the list cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely she now decides to submit a second blank list item 

        # She recieves a simlar warning on the list page 

        # And she can correct it by filling some text in 

        self.fail("Write me! ")


if __name__ == "__main__":
    unittest.main(warnings="ignore")

