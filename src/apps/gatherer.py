from src.components.rabbit import RabbitConnection
from src.components.source import APISource
import json, time, os

subreddits=['r/pokemon/', 'r/pokemongo/', 'r/PokemonScarletViolet/', 'r/PokeMemes', 'r/PkmnTCG', 'r/PokemonTrades']
savepath=os.environ.get('SAVEPATH','savedata.json')

class Gatherer():
    def __init__(self, rabbit=None, api=None):
        self.rabbit=rabbit or RabbitConnection()
        self.api=api or APISource()
        if os.path.isfile(savepath):
            f = open(savepath, "r")
            self.before=json.loads(f.read())
        else:
            self.before={}

    def push(self, message):
        self.rabbit.send(message)
    def pull(self, rslash, after='', direction='before'):
        return self.api.getFromSubreddit(rslash, after, direction)
    
    def getFromSubreddit(self, subreddit, direction='before'):
        results, before = self.pull(subreddit, self.before.get(r, ''), direction)

        #if it's none we already have everything, skip and wait until it changes
        if(before != None):
            self.before[subreddit] = before
            print(f"[*] Latest pull from {subreddit}: { self.before[subreddit]}")
            for re in results:
                self.push(json.dumps(re))


if __name__ == '__main__':
    gatherer=Gatherer()
    if gatherer.before.get('after', False) == False:
        print("[*] Starting Backport")
        for iter in range(1, 20):
            print(f"[*] loop {iter} out of 20")
            for r in subreddits:
                gatherer.getFromSubreddit(r, 'after')
                time.sleep(20)
        gatherer.before={'after':True}
    print ("[*] ...Gatherer continuing from previous values")
    while(True):
        print ("[*] Gatherer checking for new objects")
        for r in subreddits:
            gatherer.getFromSubreddit(r)
            time.sleep(20)
        f = open(savepath, "w")
        f.write(json.dumps(gatherer.before))
        f.close()
        print (f"[*] Gatherer Sleeping at {time.time()}")
        time.sleep(200)


