select
count(distinct p.player_id)
from euro_cup2016.match_captain c
join euro_cup2016.player_mast p on p.player_id = player_captain
where posi_to_play = 'GK'