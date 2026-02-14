import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


# Global Configuration Variables (User Only Needs to Modify Here)
TEST_PLATFORM = "android"  # Change to "ios" to switch to iOS testing

# Store element locators by platform. Key = operation name, Value = (locator type, locator value)
LOCATORS = {
    "android": {
        "agree_btn": ("id", "hk.gov.hko.MyObservatory:id/btn_agree"),
        "nine_day_tab": ("accessibility id", "9天預報"),
        "first_day_date": ("xpath",
                           "//android.widget.LinearLayout[@index='0']//android.widget.TextView[@resource-id='hk.gov.hko.MyObservatory:id/date']")
    },
    "ios": {
        "agree_btn": ("id", "btn_agree"),
        "nine_day_tab": ("accessibility id", "9-Day Forecast"),
        "first_day_date": ("xpath", "//XCUIElementTypeCell[@index=0]//XCUIElementTypeStaticText[@name='date']")
    }
}


@pytest.fixture(scope="module")
def appium_driver():
    # Initialize cross-platform Appium driver (compatible with Android/iOS)
    if TEST_PLATFORM.lower() == "android":
        caps = {
            "platformName": "Android",
            "deviceName": os.getenv("ANDROID_DEVICE_NAME", "Android Emulator"),
            "platformVersion": os.getenv("ANDROID_PLATFORM_VERSION", "13"),
            "appPackage": os.getenv("ANDROID_APP_PACKAGE", "hk.gov.hko.MyObservatory"),
            "appActivity": os.getenv("ANDROID_APP_ACTIVITY", ".AgreementActivity"),
            "automationName": "UiAutomator2",
            "noReset": True,
            "autoGrantPermissions": True,
            "newCommandTimeout": 30,
            "orientation": "PORTRAIT"
        }
        options = UiAutomator2Options().load_capabilities(caps)
    elif TEST_PLATFORM.lower() == "ios":
        caps = {
            "platformName": "iOS",
            "deviceName": os.getenv("IOS_DEVICE_NAME", "iPhone 15"),
            "platformVersion": os.getenv("IOS_PLATFORM_VERSION", "17.0"),
            "bundleId": os.getenv("IOS_BUNDLE_ID", "hk.gov.hko.MyObservatory"),
            "automationName": "XCUITest",
            "noReset": True,
            "newCommandTimeout": 30,
            "orientation": "PORTRAIT"
        }
        options = XCUITestOptions().load_capabilities(caps)
    else:
        raise ValueError(f"不支持的测试平台：{TEST_PLATFORM}，仅支持android/ios")

    # Initialize driver
    driver = webdriver.Remote(os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723/wd/hub"), options=options)

    yield driver

    # Close driver
    driver.quit()


@pytest.fixture(scope="module")
def platform_locators():
    """Provide element locators for the current test platform"""
    return LOCATORS[TEST_PLATFORM.lower()]
