-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!

SELECT band_name, 
       CASE
           WHEN split IS NULL THEN 2022 - formed
           ELSE 2022 - formed + split
       END as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
