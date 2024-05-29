from selenium import webdriver
def save(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    with open('page.html', 'w', encoding="utf-8") as f:
        f.write(driver.page_source)
    driver.close()