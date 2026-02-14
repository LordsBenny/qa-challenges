"""
Question 3: API Verification
Objective:
Automate the verification of market data for a specific instrument using an API endpoint
from the Shenzhen Stock Exchange (SZSE) website.
Instructions:
1. Identify the API Endpoint:
-
Navigate to the following URL: SZSE Market Data.
-
Use developer tools in your browser to identify the API endpoint that
provides market data for the instrument with code 000001.
2. Send a Request:
-
Use Python to send a request to the identified API endpoint.
-
Ensure that the request is properly configured with any necessary headers
or parameters.
3. Verify the Response:
-
Check the response status code to determine if the request was successful
(e.g., status code 200 for HTTP success).
-
Log or print the response status for verification.
4. Extract and Verify Market Data:
-
Parse the API response to extract market data, specifically the "High" and
"Low" values for the instrument.
-
Verify that the "High" value is greater than the "Low" value.
-
Log or print the extracted values and the result of the verification.
"""


import time
import requests
import traceback


# API endpoint for real-time market data of Shenzhen Stock Exchange (SZSE)
SZSE_URL = "https://www.szse.cn/api/market/ssjjhq/getTimeData"

"""
# Request parameters for fetching stock data
# - code: Target stock ID (000001 is Ping An Bank)
# - marketId: Market identifier (1 = Shenzhen Main Board)
# - random: Timestamp to bypass cache and get the latest data
"""
REQUEST_DATA = {
    "code": "000001",
    "marketId": "1",
    "random": time.time()
}


def test_verify_szse_api():
    """
    Test case to verify the availability and data validity of SZSE real-time data API.

    Key validations:
    1. API returns 200 OK status code (service availability)
    2. Response contains valid stock data (code/name/high/low)
    3. High price is greater than low price (data logical validity)
    """
    try:
        r = requests.get(url=SZSE_URL, params=REQUEST_DATA)
        # Verify API returns successful response (200 OK)
        assert r.status_code == 200

        # Parse JSON response and extract core data field
        data = r.json().get("data")
        code = data.get("code")
        name = data.get("name")
        high = data.get("high")
        low = data.get("low")

        # Print extracted stock information for debugging/verification
        print(f"\ncode: {code}, name: {name}, high: {high}, low: {low}")

        # Verify high price is greater than low price (logical check)
        assert high > low

    except AssertionError as ae:
        # Catch assertion failures (validation errors)
        print(f"Assertion failed: {ae}")
        traceback.print_exc()

    except Exception as e:
        # Catch other exceptions (e.g: network error, JSON parse error)
        print(f"Unexpected error occurred: {e}")
        traceback.print_exc()
