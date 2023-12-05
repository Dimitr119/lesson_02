import os
from typing import List, Dict, Any
import requests
from dotenv import load_dotenv

load_dotenv()
AUTH_TOKEN = os.environ['AUTH_TOKEN']
API_URL = os.environ['API_URL']

def get_sales(date: str) -> List[Dict[str, Any]]:
    
    result = []
    
    for page in range(1,5):
        response = requests.get(
            url = API_URL,
            params = {'date': date, 'page': page},
            headers = {'Authorization': AUTH_TOKEN}
        )
        result += response.json()
    
    return result