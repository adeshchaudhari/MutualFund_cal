from fastapi import FastAPI
from datetime import datetime
from mutualfund import calculate_profit

app = FastAPI()

@app.get("/profit")
async def calculate_profit_api(scheme_code: str, start_date: str, end_date: str, capital: float = 1000000.0):
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')
    
    # Calculate profit using calculate_profit function
    profit = calculate_profit(scheme_code, start_date, end_date, capital)
    
    return {"profit": profit}
