import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
load_dotenv(dotenv_path=dotenv_path)

def add_calendar_entry(title, date):
    headers = {
        "Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    data = {
        "parent": {
            "database_id": os.getenv('NOTION_DATABASE_ID')
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Datum": {
                "date": {
                    "start": date
                }
            }
        }
    }

    response = requests.post(
        f"{os.getenv('NOTION_API_BASE')}/pages",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        print("Entry added successfully.")
    else:
        print("Error adding entry:", response.status_code, response.text)