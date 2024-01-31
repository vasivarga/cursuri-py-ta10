from random import randint

import requests

BASE_URL = "https://simple-books-api.glitch.me"
STATUS_ENDPOINT = "/status"
GET_ALL_BOOKS_ENDPOINT = "/books"
API_CLIENTS_ENDPOINT = "/api-clients"
ORDERS_ENDPOINT = "/orders"

def get_api_status():
    response = requests.get(BASE_URL + STATUS_ENDPOINT)
    return response

def get_list_of_books(book_type="", limit=""):

    url = BASE_URL + GET_ALL_BOOKS_ENDPOINT + f"?type={book_type}&limit={limit}"

    # if book_type != "" and limit == "":
    #     url += f"?type={book_type}"
    # elif book_type == "" and limit != "":
    #     url += f"?limit={limit}"
    # elif book_type != "" and limit != "":
    #     url += f"?limit={limit}&book_type={book_type}"

    response = requests.get(url)
    return response

def get_book_by_id(book_id):
    url = BASE_URL + GET_ALL_BOOKS_ENDPOINT + f"/{book_id}"
    return requests.get(url)

def get_token():
    token_found = False
    response = None

    while not token_found:
        random_number = randint(1, 999999999999999999)
        request_body = {
            "clientName": "Python",
            "clientEmail": f"pyta{random_number}@google.com"
        }
        response = requests.post(BASE_URL + API_CLIENTS_ENDPOINT, json=request_body)
        if "accessToken" in response.json().keys():
            token_found = True

    return response.json()['accessToken']

print(get_token())

# print(get_list_of_books().json())

# list_of_books: list = get_list_of_books().json()
#
# for book in list_of_books:
#     print(book['name'])
#     assert book['type'] == 'fiction' or book['type'] == 'non-fiction'

# a = 5
# a = a + 4
# a += 4


# print(get_list_of_books(limit="2", book_type="fiction").json())
