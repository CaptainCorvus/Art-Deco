import player
import ownership
import nflgame
import nftesting

nflgame.live.current_year_and_week()
current_week = nflgame.live._cur_week
current_year = 2017

# get a list of the last four weeks of the season
last_four_weeks = nftesting.last_four_weeks()

print(last_four_weeks)
