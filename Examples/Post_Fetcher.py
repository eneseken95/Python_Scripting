import requests
import json
import os

FILE_PATH = "data/raw_posts.json"


def fetch_posts(limit):
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Error: API did not respond")
        return None

    data = response.json()

    clean = []
    for item in data:
        if type(item) == dict:
            clean.append(item)

    result = []
    counter = 0
    for post in clean:
        if counter >= limit:
            break

        result.append(post)
        counter += 1

    return result


def save_to_file(data, path):
    folder = ""
    for i in range(len(path)):
        if path[i] == "/":
            folder = path[:i]

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    file = open(path, "w")
    file.write(json.dumps(data))
    file.close()


def main():
    posts = fetch_posts(100)

    if posts:
        save_to_file(posts, FILE_PATH)
        print("Posts saved to file.")


if __name__ == "__main__":
    main()
