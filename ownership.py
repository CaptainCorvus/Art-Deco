import bs4 as bs
import urllib


#The webpage with the source data from NFL.com

#nfl_url = 'http://fantasy.nfl.com/research/trends#researchTrendscache-*=researchTrends%2C%2Fresearch%2Ftrends%253Fposition%253D2%2526sort%253DpercentOwned%2526statCategory%253Dresearch%2526statSeason%253D2017%2526statType%253DweekResearchStats%2526statWeek%253D1%2Creplace'


class Player:
    'a class to hold player name and percent ownership'
    def __init__(self, name, owned):
        self.name = name
        self.owned = owned

    def getName(self):
        return self.name

    def getOwned(self):
        return self.owned

# must build the string to match the name format from nflgame api output.
# format is first initial last name. So Frank Gore would be 'F. Gore'
def buildName( henk ):
    length = len(henk)

offset = 1

# allplayers list will hold the raw html data to work with for each page
allplayers = []

# will hold objects of class Player which will house the attributes of
# name and ownership percentage. 
allPlayersOwnership = []

# this outer while loop will iterate through the pages at nfl.com by modifying 
# the url by some multiple of 25
while offset < 202:

    # long ass url will start at offset = 1 and increment by 25 each iteration
    nfl_url =  'http://fantasy.nfl.com/research/trends?offset=%d&position=O&sort=percentOwned&statCategory=research&statSeason=2017&statType=weekResearchStats&statWeek=1' % offset

    # open the web page
    nfl_source = urllib.urlopen(nfl_url)

    #make the beautiful soup object with html parser
    soup = bs.BeautifulSoup(nfl_source, 'html.parser')
    
    #print soup.title.string

    # the desired data is in the tbody tag. Since there is only one tbody 
    # per page, a find_all() will store it in a list. 
    body = soup.find_all('tbody')

    #print len(body)
    
    # 
    #players = []
    #print len(players)


    for child in body[0]:
        allplayers.append(child)
     #   players.append(child)

    
    ''''
    for duck in players:
        print duck.find_all('a')
        print '\n'
    '''
    # print len(allplayers)

    offset = offset + 25


# iterate over allplayers list and splice out the player name and 
# percent ownership from the html. player name is the only string
# in the first a tag. percent ownership is the only string in the 3rd
# td tag sibling
for duck in allplayers:
    #print duck.a.string
    playerName = duck.a.string.split()
    #print duck.contents[1]
    #print duck.td.next_sibling.next_sibling.string
    playerOwned = duck.td.next_sibling.next_sibling.string
    #print '\n'
    
    abrevName = playerName[0][0] + '. ' + playerName[1]

    p = Player(abrevName, float(playerOwned))
    allPlayersOwnership.append(p) 

    #print duck.contents[1].
print len(allPlayersOwnership)

# more for testing, but print the Player objects/attributes
for goose in allPlayersOwnership:
    num = goose.getOwned()
    print goose.getName(), num









