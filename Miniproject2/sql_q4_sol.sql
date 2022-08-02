select 
play_stage,
sum(case when in_out = 'I' then 1 else 0 end) as subs
from euro_cup2016.player_in_out p
join euro_cup2016.match_mast m on p.match_no = m.match_no
group by play_stage;