import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from framework.base_page import BasePage
from pageObject.AddToChart import AddToChart


class TestAmazon(unittest.TestCase):

    def setUp(self):
        browser = BasePage(self)
        self.driver = browser.open_browser()

    def test_amazon(self):
        amazon = AddToChart(self.driver)
        WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(amazon.search_bar))
        amazon.type_search_item()
        amazon.click_search_button()
        amazon.click_target_element()
        amazon.switch_to_new_tab()
        amazon.click_add_to_chart()
        self.assertEqual(amazon.get_price_text(), "￥ 161.35")

    def tearDown(self):
        self.driver.quit()

