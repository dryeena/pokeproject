import requests
import time


class APISource(): 
    def __init__(self):
        pass
    def getRequest(self, appURL):
        get_headers = {
            'user-agent': 'myapp v0.1 by /u/pokeappdev'
        }
        try:
            return requests.get(appURL, headers=get_headers, timeout=10)
        except:
            return None
    
    def getFromSubreddit(self, subreddit, before='', direction='before'):
        success=False
        appURL=f"https://www.reddit.com/{subreddit}/new.json?limit=50&{direction}={before}"
        while(not success):
            response = self.getRequest(appURL)
            if response and response.status_code==200:
                success=True
            else:
                print(f"{subreddit} Failed with {response.status_code}, trying again in 30")
                time.sleep(25)
        results=[]
        after=response.json()['data']['after']
        for d in response.json()['data']['children']:
            results.append(d)
        return results, after