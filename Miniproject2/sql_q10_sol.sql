select 
p.*
from euro_cup2016.player_mast p
join euro_cup2016.soccer_country c on p.team_id = c.country_id
where playing_club = 'Liverpool' and country_name = 'England'