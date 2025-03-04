from celery import shared_task
import requests

@shared_task
def fetch_isins():
    """
    Simulated task: Fetches ISINs (International Securities Identification Numbers)
    every 24 hours and prints them.
    """
    print("Fetching ISINs...")  # Replace with actual API call if needed

    # Example: Fetch data from an API (replace with actual API URL)
    # response = requests.get("https://example.com/api/isins")
    # isins = response.json()
    # print(isins)

    return "ISINs fetched successfully!"
