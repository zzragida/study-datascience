from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk import LancasterStemmer
import nltk

def main():
    url = "http://www.networksciencelab.com"
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc)

    links = [(link.string, link['href'])
        for link in soup.find_all('a')
        if link.has_attr('href')
    ]
    # print(links)

    ls = nltk.LancasterStemmer()

    # word tokenize
    words = nltk.word_tokenize(soup.text)

    # lowercase
    words = [w.lower() for w in words]

    # remove stopwords
    words = [ls.stem(w) 
        for w in words
        if w not in stopwords.words('english') and w.isalnum()
    ]

    # count frequency
    freqs = Counter(words)
    print(freqs.most_common(10))

if __name__ == "__main__":
    main()