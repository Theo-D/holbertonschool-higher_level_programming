#!/usr/bin/python3
import requests
import json
import csv

def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    dicts = r.json()
    if isinstance(r, requests.Response):
        print("Status Code: {}".format(r.status_code))
        for dict in dicts:
            print(dict['title'])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    dicts = r.json()
    if isinstance(r, requests.Response):
        with open('posts.csv', 'w', encoding="utf-8") as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(dicts)
