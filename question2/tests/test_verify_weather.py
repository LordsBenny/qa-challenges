import datetime
import pytz
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from question2.tests.setup import TEST_PLATFORM


# Hong Kong timezone
HK_TZ = pytz.timezone("Asia/Hong_Kong")

# Map locator types to AppiumBy enumeration (unified cross-platform locator logic)
LOCATOR_TYPE_MAP = {
    "id": AppiumBy.ID,
    "accessibility id": AppiumBy.ACCESSIBILITY_ID,
    "xpath": AppiumBy.XPATH,
    "name": AppiumBy.NAME,
    "class name": AppiumBy.CLASS_NAME
}


def get_locator(locator_config):
    """
    Parse locator configuration and return (AppiumBy type, locator value)

    :param locator_config: Tuple in format (locator_type, locator_value), e.g. ("id", "btn_agree")
    :return: Tuple containing AppiumBy type and locator value, e.g. (AppiumBy.ID, "btn_agree")
    """
    loc_type, loc_value = locator_config
    return LOCATOR_TYPE_MAP[loc_type.lower()], loc_value


def test_9day_weather_date(appium_driver, platform_locators):
    # Cross-platform validation of the first day's date in the 9-day weather forecast
    driver = appium_driver
    wait = WebDriverWait(driver, 15)

    # Step 1: Navigate to 9-day weather forecast page
    nine_day_tab_loc = get_locator(platform_locators["nine_day_tab"])
    nine_day_tab = wait.until(EC.element_to_be_clickable(nine_day_tab_loc))
    nine_day_tab.click()

    # Step 2: Locate the first day's weather forecast date element
    first_day_date_loc = get_locator(platform_locators["first_day_date"])
    first_day_date_elem = wait.until(EC.visibility_of_element_located(first_day_date_loc))

    # Extract displayed date text
    displayed_date_text = first_day_date_elem.text.strip()

    # Step 3: Parse and validate the date
    try:
        if TEST_PLATFORM.lower() == "android":
            displayed_date = datetime.datetime.strptime(displayed_date_text.split()[0], "%Y-%m-%d").date()
        else:  # iOS
            displayed_date = datetime.datetime.strptime(displayed_date_text, "%d %b %Y").date()
    except ValueError as e:
        raise ValueError(f"Date format parsing failed, please adapt to {TEST_PLATFORM} platform date format: {str(e)}")

    # Get current date in Hong Kong timezone
    current_hk_date = datetime.datetime.now(HK_TZ).date()

    # Assertion: The first day's date should be the current date or the next day (adapt to data update)
    assert displayed_date in [current_hk_date, current_hk_date + datetime.timedelta(days=1)], \
        f"Date validation failed! {TEST_PLATFORM.upper()} displayed date: {displayed_date}, Current Hong Kong date: {current_hk_date}"
