USE living_library_manage_system;

DROP PROCEDURE IF EXISTS proc_get_experts_and_active_courses_by_branch;
DELIMITER $$

CREATE PROCEDURE proc_get_experts_and_active_courses_by_branch(
    IN p_branch_name VARCHAR(50)
)
BEGIN
    /*
        Purpose:
        Given a branch_name ('inner', 'health', 'social', or 'finance'),
        this procedure returns:
            - Each expert in that branch (no duplicates)
            - A summary of their active course titles (if any)
    */

    SELECT 
        b.branch_name AS Branch,
        u.full_name AS Expert_Name,
        e.specialization AS Specialization,
        e.rating_avg AS Expert_Rating,
        GROUP_CONCAT(DISTINCT c.title ORDER BY c.title SEPARATOR ', ') AS Active_Courses
    FROM experts e
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON e.branch_id = b.branch_id
    LEFT JOIN courses c 
        ON e.expert_id = c.expert_id 
        AND c.is_active = TRUE
    WHERE 
        b.branch_name = p_branch_name
    GROUP BY 
        b.branch_name, u.full_name, e.specialization, e.rating_avg
    ORDER BY 
       # e.rating_avg DESC, 
        u.full_name ASC;
END$$

DELIMITER ;

select * from users u where u.role = 'expert';
CALL proc_get_experts_and_active_courses_by_branch('inner');
