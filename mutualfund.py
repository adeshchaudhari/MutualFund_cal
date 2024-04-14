import requests
from datetime import datetime, timedelta

def calculate_profit(scheme_code, start_date, end_date, capital=1000000.0):
    # Format dates
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')
    
    # Get NAV on start date
    nav_start = get_nav(scheme_code, start_date)
    
    # Get NAV on end date
    nav_end = get_nav(scheme_code, end_date)
    
    # Calculate units allotted on start date
    units_allotted = capital / nav_start
    
    # Calculate value of units on end date
    value_end = units_allotted * nav_end
    
    # Calculate net profit
    net_profit = value_end - capital
    
    return net_profit

def get_nav(scheme_code, date):
    date_str = date.strftime('%d-%m-%Y')
    api_url = f'https://api.mfapi.in/mf/{scheme_code}?date={date_str}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        nav_data = response.json()
        
        # If NAV data is not available for the exact date, find the next available date
        while 'data' not in nav_data:
            date += timedelta(days=1)
            date_str = date.strftime('%d-%m-%Y')
            api_url = f'https://api.mfapi.in/mf/{scheme_code}?date={date_str}'
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            nav_data = response.json()
        
        # Extract NAV value and convert to float
        nav = float(nav_data['data'][0]['nav'])
        return nav
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.JSONDecodeError as json_err:
        print(f'JSON decoding error occurred: {json_err}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')



# Test the calculate_profit function with sample inputs
scheme_code = '101206'  #sample scheme_code
start_date = '11-11-2023'
end_date = '21-02-2024'
capital = 1000000.0

profit = calculate_profit(scheme_code, start_date, end_date, capital)
print(f'Net profit: {profit}')



