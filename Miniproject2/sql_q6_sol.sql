select 
count(*)
from euro_cup2016.match_mast
where abs(cast(SUBSTRING_INDEX(SUBSTRING_INDEX(goal_score, '-', 1), '-', -1) as decimal) - cast(TRIM( SUBSTR(goal_score, LOCATE('-', goal_score)+1)) as decimal)) = 1
and decided_by = 'N'