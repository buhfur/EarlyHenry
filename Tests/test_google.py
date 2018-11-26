from googlesearch import search
#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)

try:
    from googlesearch import search

except ImportError:
    print("couldent import google search")

def test_google():
    query = "youtube"
    google_search = search(query, lang='en', num=10, start=0,
    stop=10)

    return google_search



if __name__ == '__main__':
    for new in test_google():
        print(new) #prints out the obtained urls
