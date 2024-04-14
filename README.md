# MutualFund_cal

This Python script calculates the profit for a mutual fund investment based on the provided scheme code, start date, end date, and initial capital. It retrieves Net Asset Value (NAV) data from the Mutual Fund API to perform the calculations.

Working:-
Dependencies
Python 3.9.7
requests library
FastAPI
uvicorn


Usage:-
Install the required dependencies by running pip install requests fastapi uvicorn.
Modify the scheme_code, start_date, end_date, and capital variables in the mutualfund.py script according to your investment details.
Run the script using python mutualfund.py.
The script will calculate the net profit for your mutual fund investment and display the result.

uvicorn app:app --reload 
This command starts the FastAPI application, which serves the profit calculation endpoint. You can then send HTTP GET requests to calculate the profit for different mutual fund investments.

Functionality
The calculate_profit function calculates the net profit for the investment by fetching NAV data for the start and end dates, calculating the number of units allotted, and determining the final value of the investment.
The get_nav function retrieves the NAV data for a specific scheme code and date from the Mutual Fund API.
The script handles cases where NAV data is not available for the exact start or end date by finding the next available date with data.
Error Handling
HTTP errors and JSON decoding errors are handled gracefully using try-except blocks, ensuring robustness and preventing crashes due to network or data issues.


Below is an Example

scheme_code = '101206'
start_date = '11-11-2023'
end_date = '21-02-2024'
capital = 1000000.0

profit = calculate_profit(scheme_code, start_date, end_date, capital)
print(f'Net profit: {profit}')
Replace the scheme_code, start_date, end_date, and capital variables with your investment details to calculate the profit for your mutual fund investment.
