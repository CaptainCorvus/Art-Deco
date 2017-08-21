

class Player:
    'a class to hold player name and percent ownership'
    def __init__(self, name, owned):
        self.name = name
        self.owned = owned

    def getName(self):
        return self.name

    def getOwned(self):
        return self.owned



class Receiver:
    def __init__(self, name, receptions, yards, tds, owned):
        self.name = name
        self.receptions = receptions
        self.yards = yards
        self.tds = tds
        self.owned = owned

class Rushers: 
    def __init__(self, name, ru_yards, receptions, re_yards, tds, owned):
        self.name = name
        self.ru_yards = ru_yards 
        self.receptions = receptions
        self.re_yards = re_yards
        self.tds = tds
        self.owned = owned

class Passers:
    def __init__(self, name, completions, yards, tds, ints, sacks, owned):
        self.name = name
        self.completions = completions
        self.yards = yards
        self.tds = tds
        self.ints = ints
        self.sacks = sacks
        self.owned = owned


#this probably won't work, since it's trying to parse a BS object it doesn't
#have acces to
""" Description: This function takes an array containing all of the players 
        webscraped data. And parses it down to jus their first and last name, 
        using split to store the name into two arrays. 

def build_player_name(allPlayersArray):
    for player in allPlayersArray:
        
        # player name is the only string in the first </a> tag in the html
        # split it into two char arrays and store in playerName
        playerName = player.a.string.split()        

        # ownership is in the third </td> tag of 
        playerOwned = player.td.next_sibling.next_sibling.string
        
        # get the first initial and the full last name. Matching nflgame form
        abrevName = playerName[0][0] + '.' + playerName[1]
        
        p = Player(abrevName, float(playerOwned))
        
        # array to hold player objects, with name and ownership data
        playerObjectArray = []
        playerObjectArray.append(p)
        
        return
"""