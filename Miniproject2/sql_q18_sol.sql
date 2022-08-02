select max(cards) from (
select 
match_no,
count(player_id) as cards
from euro_cup2016.player_booked
group by match_no
order by cards desc) a