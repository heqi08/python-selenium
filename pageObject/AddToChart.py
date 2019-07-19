from selenium.webdriver.common.by import By

from framework.base_page import BasePage


class AddToChart(BasePage):
    search_bar = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_button = (By.XPATH, "//input[@type='submit']")
    search_target = (By.LINK_TEXT, "THERMOS 膳魔师 不锈钢保温杯 500ml 不锈钢色 FFM-500 SBK")
    add_to_chart = (By.XPATH, '//*[@id="add-to-cart-button"]')
    price = (By.XPATH, '//*[@id="hlb-subcart"]/div[1]/span/span[2]')

    def type_search_item(self):
        search_bar_element = self.driver.find_element(*AddToChart.search_bar)
        search_bar_element.send_keys("膳魔师保温杯")

    def click_search_button(self):
        search_button_element = self.driver.find_element(*AddToChart.search_button)
        search_button_element.click()

    def click_target_element(self):
        search_target_element = self.driver.find_element(*AddToChart.search_target)
        search_target_element.click()

    def click_add_to_chart(self):
        add_to_chart_element = self.driver.find_element(*AddToChart.add_to_chart)
        add_to_chart_element.click()

    def get_price_text(self):
        return self.driver.find_element(*AddToChart.price).text
