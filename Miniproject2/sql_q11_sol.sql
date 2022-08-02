select 
jersey_no,
player_name,
playing_club
from euro_cup2016.player_mast p
join euro_cup2016.soccer_country c on p.team_id = c.country_id
where country_name = 'England' and posi_to_play = 'GK'