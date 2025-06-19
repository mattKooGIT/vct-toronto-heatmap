from valorant import Client
from config import RIOT_API_KEY

client = Client(RIOT_API_KEY)

leaderboard = client.get_leaderboard(region = 'na', queue = 'competitive')

#put players in a list
puuids = []
for rank_group in leaderboard.ranks: #go through each rank
    players = rank_group.players #list of players in that rank
    sample_players = players[:100] #take top 100 players
    for p in sample_players:
        puuids.append(p.puuids)