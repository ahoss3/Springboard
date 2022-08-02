select referee_name from (
select 
referee_name,
count(b.player_id) as booking
from euro_cup2016.match_mast m
join euro_cup2016.referee_mast r on m.referee_id = r.referee_id
join euro_cup2016.player_booked b on b.match_no = m.match_no
group by referee_name
order by booking desc) a
where a.booking = (select max(booking) from (select 
referee_name,
count(b.player_id) as booking
from euro_cup2016.match_mast m
join euro_cup2016.referee_mast r on m.referee_id = r.referee_id
join euro_cup2016.player_booked b on b.match_no = m.match_no
group by referee_name
order by booking desc) b)
