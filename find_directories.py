import requests


wordlist = 'crash.txt'
url = 'http://localhost:8000/'
uri = None

with open(wordlist, 'r') as file:
    for directory in file:
        #print(repr(directory[-1]))
        directory = directory.replace('\n','')
        #print(repr(directory[-1]))
        uri = url + directory
        #print(uri)

        # note: requests by default follows redirections
        response = requests.get(uri, timeout=0.001, allow_redirects=False)
        if(response.status_code == 200):
            print('directory found --->', directory)
