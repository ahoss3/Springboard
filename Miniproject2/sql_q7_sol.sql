select 
distinct venue_name
from euro_cup2016.match_mast m
join euro_cup2016.soccer_venue s on m.venue_id = s.venue_id
where m.decided_by = 'P'