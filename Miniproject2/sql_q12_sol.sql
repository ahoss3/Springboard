select 
country_name,
posi_to_play,
count(g.goal_id) as goals
from euro_cup2016.player_mast p
join euro_cup2016.soccer_country c on p.team_id = c.country_id
join euro_cup2016.goal_details g on g.player_id = p.player_id
group by country_name, posi_to_play
having count(g.goal_id) > 0