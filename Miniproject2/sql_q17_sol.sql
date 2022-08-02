select 
country_name,
count(r.ass_ref_id)
from euro_cup2016.soccer_country c
join euro_cup2016.asst_referee_mast r on r.country_id = c.country_id
group by country_name