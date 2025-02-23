# example_requests.py
"""Module providing a function printing python version."""

from os import requests

def fetch_random_quote():
    """
    Fetches a random quote from a public API.
    
    Returns:
        str: The fetched quote.
    """
    url = "https://api.quotable.io/random"
    # Making a GET request to fetch a random quote
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting the quote from the response JSON
        quote = response.json()["content"]
        return quote
    else:
        return f"Error: Unable to fetch quote. Status Code: {response.status_code}"

def main():
    """Function printing python version."""
    quote = fetch_random_quote()
    print("Random Quote:")
    print(quote)

if __name__ == "__main__":
    main()
