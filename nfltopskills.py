"""  @name trevor mccleery @date 1/1/2017
    this program implements the nflgame API in order to display stats of 
    the top WRs and RBs in the NFL, in order to make more informed fantasy 
    football transactions.  """


import nflgame
import datetime
import pytz

""" this first part must run in order to use the nflgame _cur_year, _cur_week variables
which store the current week and year of the nfl season.  """

nflgame.live.current_year_and_week()
current_year = nflgame.live._cur_year
current_week = nflgame.live._cur_week

"""this module will build a list with the most recent 4 weeks of the season,for example 
if the week is 16, it will return a list with [13, 14, 15, 16]. The elif statements are 
for the cases where returning 4 weeks would result in negative numbers, which would 
create errors.
    """
def last_four_weeks():
    if current_week >= 4:
        week_list = [current_week - 3, current_week - 2, current_week - 1, current_week]
    	return week_list
    elif current_week == 3:
        week_list = [current_week - 2, current_week - 1, current_week]
        return week_list
    elif current_week == 2:
        week_list = [current_week - 1, current_week]
        return week_list
    elif current_week == 1:
        week_list = current_week
        return week_list

""" get the receptions by the leading 5 recievers over the last 4 weeks """
def get_wr_touches():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RECEPTIONS: ")
    for p in players.receiving().sort("receiving_rec").limit(5):
        print p, p.receiving_rec


""" get the yards by the leading 5 recievers over the last 4 weeks """
def get_wr_yards():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RECEIVING YARDAGE: ")
    for p in players.receiving().sort("receiving_yds").limit(5):
        print p, p.receiving_yds

""" get the touchdowns by the leading 5 recievers over the last 4 weeks """
def get_wr_tds():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RECEIVING TOUCHDOWNS: ")
    for p in players.receiving().sort("receiving_tds").limit(5):
        print p, p.receiving_tds

""" get the rushes by the leading 5 running backs over the last 4 weeks """
def get_rb_touches():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RUSHING ATTEMPTS: ")
    for p in players.rushing().sort("rushing_att").limit(5):
        print p, p.rushing_att

""" get the yards by the leading 5 running backs over the last 4 weeks """
def get_rb_yards():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RUSHING YARDAGE: ")
    for p in players.rushing().sort("rushing_yds").limit(5):
        print p, p.rushing_yds

""" get the touchdowns of the leading 5 running backs over the last 4 weeks """
def get_rb_tds():
    last4games = nflgame.games(current_year, weeks)
    players = nflgame.combine_max_stats(last4games)
    print("RUSHING TOUCHDOWNS: ")
    for p in players.rushing().sort("rushing_tds").limit(5):
        print p, p.rushing_tds

#run the module to get the last 4 weeks stored as a list of numbers
weeks = last_four_weeks()

#run WR modules to get stats
print("TOP 5 WRs OVER LAST 4 WEEKS: ")
get_wr_touches()
get_wr_yards()
get_wr_tds()

#run RB modules to get stats
print("********************************************************* ")
print("TOP 5 RBs OVER LAST 4 WEEKS:  ")
get_rb_touches()
get_rb_yards()
get_rb_tds()

