from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()


def test_faceBook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_rediffMail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.rediff.com/")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()

# run the script by using the below command or right click and click on run button.
# PS \\Practice\\examples> py.test .\test_WebPage_login.py
# pip install pytest-xdist
# Now, we can run tests by using the syntax pytest -n <num>
# pytest -n 3