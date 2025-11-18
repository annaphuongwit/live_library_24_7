USE living_library_manage_system;

DROP PROCEDURE IF EXISTS proc_get_courses_by_branch_and_expert;
DELIMITER $$

CREATE PROCEDURE proc_get_courses_by_branch_and_expert(
    IN p_branch_name VARCHAR(50),
    IN p_expert_name VARCHAR(120)
)
BEGIN
    /*
        Purpose:
        - Return all active courses for a given expert in a given branch.
        - Joins courses → experts → users → branches.
        - Only shows active courses.
    */

    SELECT 
        c.course_id AS Course_ID,
        c.title AS Title,
        c.description AS Description,
        c.language AS Language,
        c.price AS Price,
        c.avg_rating AS Rating,
        c.total_students AS Students,
        c.connect_link AS Link,
        b.branch_name AS Branch,
        u.full_name AS Expert_Name
    FROM courses c
    JOIN experts e ON c.expert_id = e.expert_id
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON c.branch_id = b.branch_id
    WHERE 
        b.branch_name = p_branch_name
        AND u.full_name = p_expert_name
        AND c.is_active = TRUE
    ORDER BY 
        c.avg_rating DESC, 
        c.title ASC;
END$$

DELIMITER ;

CALL proc_get_courses_by_branch_and_expert(
    'inner',
    'Sophia Tran Nguyen'
);

-- ---------- CREATE VIEW ----------
-- -- View courses, marked with whether or not they are currently available
DROP VIEW IF EXISTS view_current_courses_status;

CREATE VIEW view_current_courses_status AS
SELECT 
    c.course_id,
    c.title AS Title,
    c.domain AS Branch,
    b.branch_name,
    u.full_name AS Expert,
    c.language AS Language,
    c.price,
    c.total_students,
    c.begin_date AS Begin,
    c.end_date AS End,
    CASE 
        WHEN c.is_active = 1 
             OR (c.begin_date IS NOT NULL AND c.begin_date <= NOW() 
                 AND (c.end_date IS NULL OR c.end_date >= NOW())) 
        THEN 'Active Now'
        ELSE 'Inactive / Upcoming'
    END AS current_status
FROM courses c
JOIN experts e ON c.expert_id = e.expert_id
JOIN users u ON e.user_id = u.user_id
JOIN branches b ON c.branch_id = b.branch_id
ORDER BY 
    current_status DESC, 
    c.begin_date ASC;