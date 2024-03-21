-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(5, 2);
    DECLARE total_count INT;
    DECLARE avg_score DECIMAL(5, 2);
    
    SELECT SUM(score), COUNT(*) INTO total_score, total_count
    FROM scores
    WHERE user_id = user_id;

    IF total_count > 0 THEN
        SET avg_score = total_score / total_count;
        INSERT INTO average_scores (user_id, average_score)
        VALUES (user_id, avg_score)
        ON DUPLICATE KEY UPDATE average_score = avg_score;
    END IF;
END //

DELIMITER ;

