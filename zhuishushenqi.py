import requests
import config
import json

# search book by keyword, returns a result list
def search_book(keyword):
    response = requests.get(config.bookSearch, params={"query": keyword})
    search_results = json.loads(response.text)
    return search_results

def get_book_source_list(book_id):
    response = requests.get(config.bookInfo, params={"id": book_id})
    book_source_list = json.loads(response.text)
    return book_source_list

if __name__ == "__main__":
    # search_book("遮天")
    print(get_book_source_list("5106099abb1c67cf28000016"))
    print(requests.get("http://api.zhuishushenqi.com/book/:id?id=5106099abb1c67cf28000016").text)

