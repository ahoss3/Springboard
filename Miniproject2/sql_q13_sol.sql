select 
player_name
from euro_cup2016.player_mast p
join euro_cup2016.goal_details g on g.player_id = p.player_id
where posi_to_play like '%D%'