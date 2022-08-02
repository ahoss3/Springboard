select 
s.match_no,
c.country_name
from euro_cup2016.penalty_shootout s
join euro_cup2016.soccer_team t on t.team_id = s.team_id
join euro_cup2016.soccer_country c on t.team_id = c.country_id
where s.match_no = (select match_no from euro_cup2016.penalty_shootout where kick_no = (select max(kick_no) from euro_cup2016.penalty_shootout))
group by s.match_no, c.country_name
