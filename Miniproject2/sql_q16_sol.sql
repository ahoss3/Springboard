select 
referee_name,
venue_name,
count(m.match_no) as matches
from euro_cup2016.match_mast m
join euro_cup2016.referee_mast r on r.referee_id = m.referee_id
join euro_cup2016.soccer_venue v on v.venue_id = m.venue_id
group by referee_name, venue_name