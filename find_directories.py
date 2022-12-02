import requests
from requests.structures import CaseInsensitiveDict
from http.client import HTTPConnection



s = requests.Session()


headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["Keep-Alive"] = "timeout=5, max=100"

desired_status_codes = [200, 301]

wordlist = 'wordlist.txt'
url = 'http://192.168.6.176:8000/'
directory = None
timeout = 100
follow_redirects = False



with open(wordlist, 'r') as file:
    for directory in file:
        directory = directory.replace('\n','')
        directory = url + directory
        response = s.get(directory, headers=headers,timeout=timeout)
        if(response.status_code == 200):
            print('directory found --->', directory)



