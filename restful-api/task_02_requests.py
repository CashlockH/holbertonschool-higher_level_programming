"""Request to JSONPlaceHolder"""
import requests
import csv


def fetch_and_print_posts():
    """Get and prints the title of jsonplaceholder"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(r.status_code)
    for i in r.json():
        print(i['title'])


def fetch_and_save_posts():
    """Get the posts of jsonplaceholder and save it to a csv file"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    j = r.json()
    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in j:
            writer.writerow({
                'id': i['id'],
                'title': i['title'],
                'body': i['body']
                })
