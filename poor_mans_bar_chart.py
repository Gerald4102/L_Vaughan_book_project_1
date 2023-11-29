'''Displays a chart of the frequency of each letter in an online sample data set'''

from urllib import request
import json
from pprint import pprint, pformat
from string import ascii_lowercase

# e.g. https://jsonplaceholder.typicode.com/users
web_link = input("Enter an API: ")

response = request.urlopen(web_link)
json_response = response.read()

users = json.loads(json_response)
users_string = pformat(users).lower()

letter_count = {}
for c in ascii_lowercase:
    letter_count[c] = c * users_string.count(c)

pprint(letter_count)
