USE springboardopt;

-- -------------------------------------
SET @v1 = 1612521;
SET @v2 = 1145072;
SET @v3 = 1828467;
SET @v4 = 'MGT382';
SET @v5 = 'Amber Hill';
SET @v6 = 'MGT';
SET @v7 = 'EE';			  
SET @v8 = 'MAT';

-- 6. List the names of students who have taken all courses offered by department v8 (deptId).
explain
with crs as 
(
SELECT crsCode FROM Course WHERE deptId = @v8 AND crsCode IN (SELECT crsCode FROM Teaching)
),
crsCount as
(
SELECT COUNT(*) as count FROM Course WHERE deptId = @v8 AND crsCode IN (SELECT crsCode FROM Teaching)
)

select name from
(
SELECT studId, count(*) as count
	FROM Transcript t
	join crs on t.crsCode = crs.crsCode
    group by studId
) a
join crsCount on a.count = crsCount.count
join student s on a.studId = s.id

-- I did my best by creating indices where appropriate and removing the HAVING clause from the original query, instead opting for CTEs