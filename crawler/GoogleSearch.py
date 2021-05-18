#!/usr/bin/python3

import json
import os.path
from datetime import datetime
from googleapiclient.discovery import build

my_api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
my_cse_id = "xxxxxxxxxxxxxxxxxxxxxx"

max_page = 10
#query_keywords = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords1 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords2 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords3 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords4 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords5 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords6 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords7 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords8 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords9 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"
query_keywords10 = "xxxxxxx xxxx xxx xx x xxxxxxx x xxxxxx"


def google_search(service, query_keywords, cse_id):
    result = service.cse().list(q=query_keywords, cx=cse_id).execute()
    return google_next_page(service, query_keywords, my_cse_id, result, 1, max_page, result['items'])

def google_next_page(service, query_keywords, cse_id, res, page, max_page, url_items):
    try:
        next_res = service.cse().list(q=query_keywords, cx=cse_id, num=10, start=res['queries']['nextPage'][0]['startIndex'],).execute()

        url_items.extend(next_res['items'])
        page += 1
    except:
        return url_items

    if page == max_page:
        return url_items
    if len(res['queries']['nextPage'][0]) > 0:
        #return google_next_page(service, query_keywords, cse_id, next_res, page, max_page, url_items)
        return google_next_page(service, query_keywords, cse_id, next_res, page, max_page, url_items)
    else:
        return url_items

filename = "dominios.txt"
if os.path.isfile(filename):
    os.remove(filename)
f = open(filename, "w")

service = build("customsearch", "v1", developerKey=my_api_key)

url_items = None
#try:
url_items = google_search(service, query_keywords1, my_cse_id)
var = google_search(service, query_keywords2, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords3, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords4, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords5, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords6, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords7, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords8, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords9, my_cse_id)
url_items.extend(var)
var = google_search(service, query_keywords10, my_cse_id)
url_items.extend(var)

#except:
    #print("Erro!")

if len(url_items) > 0:
    for item in url_items:
        print(str(item['link']))
        f.write(str(item['link'])+"\n")
f.close()
