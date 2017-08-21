import player
import ownership
import nflgame
import nftesting

nflgame.live.current_year_and_week()
current_week = nflgame.live._cur_week
current_year = 2017

# get a list of the last four weeks of the season
weeks = nftesting.last_four_weeks()

print(weeks)

var = nftesting.rec_stats()

for element in var:
    print element[0], element[1]

var1 = ownership.build_name_ownership()

print len(var1)

for i in var1: 
    print i.getOwned()
    print i.getName()
