import requests
import json
import nltk
from nltk.corpus import stopwords
from time import sleep

credentials = 'email', 'password'
session = requests.Session()
session.auth = credentials

def gather_tickets(ids=[XXXXXX,XXXXX], url='https://yourdoman.zendesk.com/api/v2/search.json?query='):
    output = []
    for id in ids:
        result = session.get(url + str(id)).json()
        if 'results' in result:
            for ticket in result['results']:
                output.append(ticket)
        else:
            print('no results...')
    return output

def search(s, n=1000, url='https://yourdomain.zendesk.com/api/v2/search.json?query='):
    # s is our query string - https://developer.zendesk.com/rest_api/docs/core/search
    # n is to limit the number of results
    if not isinstance(s,str):
        s = str(s)
    page = url + s
    output = []
    while bool(page):
        result = session.get(page)
        if result.status_code != 200:
            print('sleeping...{0}'.format(result.text))
            sleep(60)
        result = result.json()
        if 'results' in result:
            for ticket in result['results']:
                output.append(ticket)
        else:
            print('no results')
        if len(output) >= n:
            break
        print('got {0} tickets so far...'.format(len(output)))
        try: page = result['next_page']
        except: page = None
    return output

default_stopwords = set(nltk.corpus.stopwords.words('english'))

def tokenize(s):
    words = nltk.word_tokenize(s)
    # Remove single-character tokens (mostly punctuation)
    words = [word for word in words if len(word) > 1]
    # Remove numbers
    words = [word for word in words if not word.isnumeric()]
    # Lowercase all words (default_stopwords are lowercase too)
    words = [word.lower() for word in words]
    # Remove stopwords
    words = [word for word in words if word not in default_stopwords]
    return words

def distribution(words, n=25, words_to_ignore=['XXXXX']): #replace XXXX with common words that you want to exclude
    words = [word for word in words if word not in words_to_ignore]
    fdist = nltk.FreqDist(words)
    for word, frequency in fdist.most_common(n):
        print(u'{};{}'.format(word, frequency))
    fdist.plot(n,cumulative=False)

# https://developer.zendesk.com/rest_api/docs/core/search
# get 10,000 tickets
data = search(s='type:ticket',n=10000)
# put all of the ticket descriptions in a list
descriptions = [d['description'] for d in data]
# combine all ticket descriptions into 1 big string
text = ' '.join(descriptions)
# tokenize the string
words = tokenize(text)
# get thre work frequency of the top n words
distribution(words)
# grab ticket data on given ticket_ids
data = gather_tickets(ids=[XXXXX,XXXXX,XXXXX])
