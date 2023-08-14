# author_='Yuxuehong';
# date: 2023/8/14 15:28
# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# caps = dict()
# caps["appium:deviceName"] = "emulator-5554"
# caps["platformName"] = "Android"
# caps["appium:platformVersion"] = "7.1.2"
# caps["appium:appPackage"] = "com.zhao.myreader"
# caps["appium:appActivity"] = "com.zhao.myreader.ui.home.MainActivity"

caps = {
    "appium:deviceName": "emulator-5554",
    "platformName": "Android",
    "appium:platformVersion": "7.1.2",
    "appium:appPackage": "com.zhao.myreader",
    "appium:appActivity": "com.zhao.myreader.ui.home.MainActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.XPATH, value="//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"书城\"]/android.widget.TextView")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
el2.click()

driver.quit()