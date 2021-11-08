"""
SQL90 获得积分最多的人(二)
with x AS ()

WITH t AS (
    SELECT  user_id,SUM(grade_num) AS grade_sum
    FROM grade_info
    GROUP BY user_id )
SELECT id,name,grade_sum
FROM t
JOIN user u ON u.id = t.user_id
WHERE grade_sum  = (SELECT MAX(grade_sum) FROM t)
"""