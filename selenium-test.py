from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
driver.get("http://localhost:8000/g_1/")
okr = driver.find_element_by_id("1")
edit = okr.find_element_by_css_selector(".ajax-edit")
karty_view = okr.find_element_by_css_selector(".karty-view")
karty_edit = okr.find_element_by_css_selector(".karty-edit")
wyborcy_view = okr.find_element_by_css_selector(".wyborcy-view")
wyborcy_edit = okr.find_element_by_css_selector(".wyborcy-edit")
karty_view_val = karty_view.text
wyborcy_view_val = wyborcy_view.text
edit.click()
assert karty_view_val == karty_edit.get_attribute('value')
assert wyborcy_view_val == wyborcy_edit.get_attribute('value')
karty_val_new = str(int(karty_view_val) + 1)
karty_edit.clear()
karty_edit.send_keys(karty_val_new)
wyborcy_val_new = str(int(wyborcy_view_val) + 3)
wyborcy_edit.clear()
wyborcy_edit.send_keys(wyborcy_val_new)

btn_save = okr.find_element_by_css_selector(".ajax-save")
btn_save.click()
driver.implicitly_wait(3)
assert karty_val_new == karty_view.text
assert wyborcy_val_new == wyborcy_view.text

#driver.refresh()
driver.get("http://localhost:8000/g_1/")


driver.implicitly_wait(5)
okr = driver.find_element_by_id("1")

karty_view = okr.find_element_by_css_selector(".karty-view")
wyborcy_view = okr.find_element_by_css_selector(".wyborcy-view")
driver.close()
