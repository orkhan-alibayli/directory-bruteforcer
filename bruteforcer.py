#Simple http bruteforcer

import requests
from requests.structures import CaseInsensitiveDict

class Bruteforcer:

    def __init__(self, url, wordlist, timeout) -> None:
        self.session = requests.Session()
        self.headers = CaseInsensitiveDict()
        self.headers = {'Connection': 'keep-alive', 'Keep-Alive': 'timeout=5, max=100'}
        self.url = url
        self.wordlist = wordlist
        self.timeout = timeout

    
    def run_bruteforcer(self):
        '''opens given wordlist file and send requests for each line in same TCP session'''

        try:
            with open(self.wordlist, 'r') as file:
                for directory in file:
                    directory = directory.replace('\n','')
                    directory = self.url + directory
                    response = self.session.get(directory, headers=self.headers,timeout=self.timeout)
                    if(response.status_code == 200):
                        print('directory found --->', directory)
        except FileNotFoundError:
            print('The file not found')