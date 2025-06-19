from valorant import Client
from config import RIOT_API_KEY
import pandas as pd

client = Client(RIOT_API_KEY)

def extract_events(match_id):
    match = client.get_match_details(match_id)
    events = []

    for round in match.rounds:
        for kill in round.kill_events:
            events.append({
                "map": match.metadata.map,
                "match_id": match.match_id,
                "event-type": "kill",
                "x": kill.victim_death_location.x,
                "y": kill.victim_death_location.y,
                "round": round.round_num,
                "attacker": kill.killer_display_name,
                "victim": kill.victim_display_name,
                "agent": kill.victim_character,
                "team": kill.victim_team
            })
    return events
