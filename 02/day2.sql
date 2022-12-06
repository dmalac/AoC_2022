-- https://adventofcode.com/2022/day/2

.mode csv
.separator " "
CREATE TABLE DAY2 (abc TEXT, xyz TEXT);
.import input.csv DAY2;
ALTER TABLE DAY2 ADD COLUMN other INT;
ALTER TABLE DAY2 ADD COLUMN me INT;
ALTER TABLE DAY2 ADD COLUMN result INT;
UPDATE DAY2 SET other =
   (CASE abc WHEN 'A' THEN 1
   WHEN 'B' THEN 2
   WHEN 'C' THEN 3
   ELSE 0 END);
UPDATE DAY2 SET me =
   (CASE xyz WHEN 'X' THEN 1
   WHEN 'Y' THEN 2
   WHEN 'Z' THEN 3
   ELSE 0 END);
UPDATE DAY2 SET result =
   (CASE WHEN other = me THEN 3
   WHEN me - other = 1 OR other - me = 2 THEN 6
   WHEN other - me = 1 OR me - other = 2 THEN 0
   ELSE -1 END);
SELECT SUM(me) + SUM(result) FROM DAY2;

-- PART 2
ALTER TABLE DAY2 ADD COLUMN me2 INT;
ALTER TABLE DAY2 ADD COLUMN result2 INT;
UPDATE DAY2 SET result2 =
   (CASE xyz WHEN 'X' THEN 0
   WHEN 'Y' THEN 3
   WHEN 'Z' THEN 6
   ELSE -1 END);
UPDATE DAY2 SET me2 =
   (CASE result2 WHEN 3 THEN other
   WHEN 6 THEN (CASE WHEN other < 3 THEN other + 1 ELSE other - 2 END) 
   WHEN 0 THEN (CASE WHEN other > 1 THEN other - 1 ELSE other + 2 END) 
   ELSE 0 END);
SELECT SUM(me2) + SUM(result2) FROM DAY2;