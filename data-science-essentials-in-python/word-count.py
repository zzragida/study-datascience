import re
import urllib.request
from collections import Counter

def request_url(url):
    html = ''
    with urllib.request.urlopen(url) as doc:
        html = doc.read()
    return html

def main():
    # retrieve url
    url = 'https://naver.com'
    html = request_url(url)
    # print(html)
    print(type(html))
    # print(html.decode('utf-8'))

    # collect word count top10
    split_result = re.split(r"\W+", html.decode('utf-8'))
    # print(split_result)
    counter = Counter(split_result)
    print(counter.most_common(10))


if __name__ == "__main__":
    main()