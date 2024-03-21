-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!

SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;

