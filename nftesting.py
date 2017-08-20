# jazzy-branch test

import nflgame
import pytz
import datetime
import ownership
from prettytable import PrettyTable

nflgame.live.current_year_and_week()
current_week = nflgame.live._cur_week

print('Current Week: ', current_week)

#year = nflgame.live._cur_year
year = 2016
print('Current Year : ', year)


""" this module retreives the current week of the NFL season, and builds a list including
    that week, and the 3 preceeding weeks """
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


""" get the games and players for the last four weeks, with their max stats combined """
week = last_four_weeks()
games = nflgame.games(year, week)
players = nflgame.combine_max_stats(games)

""" these are the lists that hold receiver statistics """
receiver_list = []
rec_rec_list  = []
rec_yrd_list  = []
rec_tds_list  = []


""" these are the lists that hold running back statistics """
rusher_list   = []
rush_att_list = []
rush_yrd_list = []
rush_rec_list = []
rush_tds_list = []
rush_rec_tds_list = []

""" loop through to append appropriate receiver list using nflgame. zip, just in case """
def rec_stats():
    for p in players.receiving().sort("receiving_yds").limit(20):
        print p
        receiver_list.append(str(p))
        rec_rec_list.append(p.receiving_rec)
        rec_yrd_list.append(p.receiving_yds)
        rec_tds_list.append(p.receiving_tds)

    zippy = zip(receiver_list, rec_rec_list, rec_yrd_list, rec_tds_list)
    #print zippy

""" loop through to append appropriate rusher list using nflgame. zip, just in case """

def rusher_stats():
    for p in players.rushing().sort("rushing_yds").limit(20):
        rusher_list.append(str(p))
        rush_att_list.append(p.rushing_att)
        rush_yrd_list.append(p.rushing_yds)
        rush_tds_list.append(p.rushing_tds)
    zippy = zip(rusher_list, rush_att_list, rush_yrd_list, rush_tds_list)
    #print zippy

""" run the rusher/receiver stat modules """
rusher_stats()
rec_stats()


""" uses PrettyTable api to nicely make.....the tables pretty """
def build_rusher_table():
    x = PrettyTable()
    x.add_column('Running Back', rusher_list)
    x.add_column('Attempts', rush_att_list)
    x.add_column('Yards', rush_yrd_list)
    x.add_column('Touchdowns', rush_tds_list)
    print('TOP RUSHERS FOR WEEKS: ', week)
    print(x)

""" uses PrettyTable to make a table of receiver statistics look nice and pretty """
def build_receiver_table():
    x = PrettyTable()
    x.add_column('Receiver', receiver_list)
    x.add_column('Receptions', rec_rec_list)
    x.add_column('Yards', rec_yrd_list)
    x.add_column('Touchdowns', rec_tds_list)
    print('TOP RECEIVERS FOR WEEKS: ', week)
    print(x)
 
build_rusher_table()
print('**********************************')
print('**********beep*boop*beep**********')   
print('**********************************')
build_receiver_table()


