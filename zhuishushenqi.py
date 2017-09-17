import requests
import config
import json

# search book by keyword, returns a result list
def search_book(keyword):
    response = requests.get(config.bookSearch, params={"query": keyword})
    search_results = json.loads(response.text)
    return search_results



if __name__ == "__main__":
    search_book("遮天")

