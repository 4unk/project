#Importing modules
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox_")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--windows-sixe=1920,1980")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()