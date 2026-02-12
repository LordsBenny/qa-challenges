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


SZSE_URL = "https://www.szse.cn/api/market/ssjjhq/getTimeData"

REQUEST_DATA = {
    "code": "000001",  # stock id
    "marketId": "1",
    "random": time.time()   # force to pull the latest data
}


def test_verify_szse_api():
    try:
        r = requests.get(url=SZSE_URL, params=REQUEST_DATA)
        assert r.status_code == 200

        data = r.json().get("data")
        code = data.get("code")
        name = data.get("name")
        high = data.get("high")
        low = data.get("low")
        print(f"\ncode: {code}, name: {name}, high: {high}, low: {low}")
        assert high > low

    except Exception as e:
        print(e)
        traceback.print_exc()
