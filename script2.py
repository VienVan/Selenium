from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

geckodriver = '/Users/VienVonVan/Downloads/chromedriver'
driver = webdriver.Chrome(geckodriver)
driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26next%3D%252F%26hl%3Den%26feature%3Dsign_in_button%26app%3Ddesktop&hl=en&passive=true#identifier')

# log in
email = driver.find_element_by_id('Email')
email.send_keys('vienvonvan@gmail.com')
driver.find_element_by_id('next').click()
# password = driver.find_element_by_id('Passwd')
# password.send_keys('phile1201')
# driver.find_element_by_id('link-forgot-passwd').click()

pwd = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Passwd"))
)
pwd.send_keys("phile1201")
driver.implicitly_wait(10)
nxt = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "signIn"))
)
nxt.click()
driver.implicitly_wait(10)
# search keyword
search = driver.find_element_by_id('masthead-search-term')
search.clear()
search.send_keys("fashion haul")
search.send_keys(Keys.RETURN)

filters = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-button"))
)
filters.click()
today = driver.find_element_by_xpath("//span[text()='Today']")
today.click()

# box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "box")))
# box.click()
#
# frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="+1"]')))
# driver.switch_to.frame(frame)
#
# driver.find_element_by_xpath('//div[@onclick]').click()
#
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jsname="msEQQc"]/following-sibling::div//div[@g_editable="true"]')))
# driver.execute_script("arguments[0].innerHTML='%s';" % comment, element)
