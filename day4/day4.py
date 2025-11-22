import requests
from bs4 import BeautifulSoup


def scrapeRedditPosts():

    url = 'https://old.reddit.com/r/news/top/'
    print(f"Fetching posts from {url}")

    try:
        # add User-Agent header so the website knows we are a script/browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)

        if (response.status_code != 200):
            print(f"Failed to retrieve page. {response.status_code}")
            return
        # parse html content
        soup = BeautifulSoup(response.text, 'html.parser')
        # extract data
        titles = soup.find_all('p', class_='title')
        print(f"Found {len(titles)} titles")
        for index, fullTitle in enumerate(titles, 1):
            title = fullTitle.find('a', class_='title')
            cleanText = title.get_text().strip() if title else "No title found"
            print(f"{index} {cleanText}")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    scrapeRedditPosts()


