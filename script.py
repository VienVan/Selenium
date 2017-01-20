from selenium import webdriver
from selenium.webdriver.common.keys import Keys

geckodriver = "/Users/VienVonVan/Downloads/chromedriver"
driver = webdriver.Chrome(geckodriver)
driver.get("http://www.youtube.com")

# search keyword
search = driver.find_element_by_id('masthead-search-term')
search.clear()
search.send_keys("fashion haul")
search.send_keys(Keys.RETURN)

# filter criteria videos posted today

# filters = driver.find_element_by_xpath("//span[contains(@class, 'yt-uix-button-content')]")
filters = driver.find_element_by_xpath("//button[contains(@class, 'filter-button')]")
print("**************", filters)
driver.implicitly_wait(30)
today = driver.find_element_by_xpath("//span[text()='Today']")
today.click()
driver.implicitly_wait(30)
links = driver.find_elements_by_xpath("//h3[contains(@class, 'yt-lockup-title ')]")
for link in links:
    link.click()
#
# videos = driver.find_element_by_xpath("//ol[contains(@class, 'section-list')]")
# for child in videos.find_elements_by_xpath(".//*"):
#     child.click()
#     driver.implicitly_wait(30)
# driver.find_element_by_xpath("//input[@id='next']").click()

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# filters = driver.find_element_by_xpath("//button[contains(@class, 'filter-button')]")


# notworking code
# elem = driver.find_element_by_xpath("//span[text()='Sign in']")
# elem.click()
# email = driver.find_element_by_id('Email')
# email.clear()
# email.send_keys('vienvonvan@gmail.com')
# email.send_keys(Keys.RETURN)
