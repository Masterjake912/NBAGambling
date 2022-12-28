from nba_api.stats.static import players
from nba_api.stats.static import teams


player_dict = players.get_players()

# Use ternary operator or write function
# Names are case sensitive
lebron = [player for player in player_dict if player['full_name'] == 'Lebron James'][0]
lebron_id = lebron['id']

# Find Team IDs
teams = teams.get_teams()
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']
