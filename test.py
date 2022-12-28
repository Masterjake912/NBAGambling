from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd

player_dict = players.get_players()

# Use ternary operator or write function
# Names are case-sensitive
lebron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
lebron_id = lebron['id']

# Find Team IDs
teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

# First we import the endpoint
# We will be using pandas dataframes to manipulate the data
# Call the API endpoint passing in lebron's ID & which season
gamelog_lebron = playergamelog.PlayerGameLog(player_id=lebron_id, season='2022')

# Converts gamelog object into a pandas dataframe
# Can also convert to JSON or dictionary
df_lebron_games_2022 = gamelog_lebron.get_data_frames()
print(df_lebron_games_2022)

# If you want all seasons, you must import the SeasonAll parameter
gamelog_lebron_all = playergamelog.PlayerGameLog(player_id=lebron_id, season=SeasonAll.all)

df_lebron_games_all = gamelog_lebron_all.get_data_frames()
print(df_lebron_games_all)

