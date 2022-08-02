select 
player_name,
jersey_no
from euro_cup2016.match_mast m
join euro_cup2016.match_details d on d.match_no = m.match_no
join euro_cup2016.soccer_country c on d.team_id = c.country_id
join euro_cup2016.player_mast p on d.player_gk = p.player_id
where country_name = 'Germany' and m.play_stage = 'G'
group by player_name, jersey_no
