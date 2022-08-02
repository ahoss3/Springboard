select
player_name
from euro_cup2016.player_in_out i
join euro_cup2016.player_mast p on i.player_id = p.player_id
where in_out = 'I' and play_schedule = 'NT' and play_half = 1
group by player_name