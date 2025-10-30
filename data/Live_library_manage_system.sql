
-- =======================================================
--  DATABASE: Living Library Management System (v2)
--  AUTHOR: Anna Phương 
--  DESCRIPTION: Multilingual multi-country coaching ecosystem
-- =======================================================

CREATE DATABASE IF NOT EXISTS living_library_manage_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE living_library_manage_system;

-- =======================================================
-- 1. COUNTRY LIBRARY TABLE
-- =======================================================
CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    language VARCHAR(50) NOT NULL,
    timezone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert predefined libraries (initial countries)
INSERT INTO countries (country_name, language, timezone)
VALUES 
('Australia', 'English', 'Australia/Sydney'),
('Germany', 'German', 'Europe/Berlin'),
('Vietnam', 'Vietnamese', 'Asia/Ho_Chi_Minh'),
('Japan', 'Japanese', 'Asia/Tokyo'),
('France', 'French', 'Europe/Paris'),
('America', 'English', 'America/New_York'),
('Hungary', 'Hungarian', 'Europe/Budapest');

-- =======================================================
-- 2. BRANCHES TABLE (each library has 4 main branches)
-- =======================================================
CREATE TABLE branches (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    branch_name ENUM('inner', 'health', 'social', 'finance') NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

-- Create default 4 branches for each country dynamically (optional to script separately later)

-- =======================================================
-- 3. USERS TABLE
-- =======================================================
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('participant', 'expert', 'admin') NOT NULL DEFAULT 'participant',
    country_id INT,
    branch_id INT,
    language VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE SET NULL,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE SET NULL
);

-- =======================================================
-- 4. EXPERTS TABLE
-- =======================================================
CREATE TABLE experts (
    expert_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    branch_id INT NOT NULL,
    specialization ENUM('inner', 'health', 'social', 'finance') NOT NULL,
    bio TEXT,
    rating_avg DECIMAL(3,2) DEFAULT 0.00,
    total_students INT DEFAULT 0,
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE
);

-- =======================================================
-- 5. COURSES TABLE
-- =======================================================
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    expert_id INT NOT NULL,
    branch_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    domain ENUM('inner', 'health', 'social', 'finance') NOT NULL,
    language VARCHAR(50) DEFAULT 'English',
    description TEXT,
    price DECIMAL(10,2) DEFAULT 0.00,
    avg_rating DECIMAL(3,2) DEFAULT 0.00,
    total_students INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (expert_id) REFERENCES experts(expert_id) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE
);

-- 22.10.25 begin
USE living_library_manage_system;

ALTER TABLE courses
ADD COLUMN connect_link VARCHAR(255) DEFAULT NULL AFTER description;
-- end

-- 23.10.2025 beginn
ALTER TABLE courses 
ADD COLUMN begin_date DATETIME DEFAULT NULL,
ADD COLUMN end_date DATETIME DEFAULT NULL;

ALTER TABLE courses
MODIFY COLUMN begin_date DATETIME DEFAULT NULL AFTER connect_link,
MODIFY COLUMN end_date DATETIME DEFAULT NULL AFTER connect_link;

ALTER TABLE courses
ALTER is_active SET DEFAULT 0;

ALTER TABLE courses
ALTER language SET DEFAULT NULL;

-- trigger for insert new
-- INSERT trigger
DROP TRIGGER IF EXISTS trg_course_auto_active;
DELIMITER $$
CREATE TRIGGER trg_course_auto_active
BEFORE INSERT ON courses
FOR EACH ROW
BEGIN
    IF NEW.begin_date IS NOT NULL AND NEW.begin_date <= NOW() THEN
        SET NEW.is_active = 1;
    ELSE
        SET NEW.is_active = 0;
    END IF;
END$$
DELIMITER ;

-- UPDATE trigger (handles later edits)
DROP TRIGGER IF EXISTS trg_course_update_active;
DELIMITER $$
CREATE TRIGGER trg_course_update_active
BEFORE UPDATE ON courses
FOR EACH ROW
BEGIN
    IF NEW.begin_date IS NOT NULL AND NEW.begin_date <= NOW() THEN
        SET NEW.is_active = 1;
    ELSE
        SET NEW.is_active = 0;
    END IF;
END$$
DELIMITER ;



-- end


-- =======================================================
-- 6. BOOKINGS TABLE
-- =======================================================
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    expert_id INT NOT NULL,
    user_id INT NOT NULL,
    scheduled_time DATETIME NOT NULL,
    status ENUM('booked', 'completed', 'cancelled') DEFAULT 'booked',
    booking_type ENUM('live', 'group') DEFAULT 'live',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (expert_id) REFERENCES experts(expert_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_booking_time (scheduled_time)
);

-- =======================================================
-- 7. FAVORITES TABLE
-- =======================================================
CREATE TABLE favorites (
    fav_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    expert_id INT NULL,
    course_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (expert_id) REFERENCES experts(expert_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- =======================================================
-- 8. FEEDBACK TABLE
-- =======================================================
CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    expert_id INT,
    course_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (expert_id) REFERENCES experts(expert_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- =======================================================
-- 9. ANALYTICS TABLE
-- =======================================================
CREATE TABLE analytics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    metric_type ENUM('student_count', 'expert_count', 'course_popularity', 'booking_rate', 'rating_avg') NOT NULL,
    reference_id INT NULL,
    metric_value DECIMAL(10,2) DEFAULT 0.00,
    country_id INT NULL,
    branch_id INT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE SET NULL,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE SET NULL,
    INDEX idx_metric_type (metric_type)
);

-- =======================================================
-- 10. CHATBOT LOGS TABLE (for experts & participants)
-- =======================================================
# CREATE TABLE chatbot_logs (
# chat_id INT AUTO_INCREMENT PRIMARY KEY,
#    user_id INT,
#    message TEXT NOT NULL,
#    response TEXT,
#    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
#);

-- =======================================================
-- 11. INVITATIONS TABLE (participants invite others)
-- =======================================================
CREATE TABLE invitations (
    invite_id INT AUTO_INCREMENT PRIMARY KEY,
    inviter_id INT NOT NULL,
    invitee_email VARCHAR(150) NOT NULL,
    course_id INT NOT NULL,
    branch_id INT,
    status ENUM('pending', 'accepted', 'declined') DEFAULT 'pending',
    invite_token VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inviter_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE SET NULL
);

-- =======================================================
-- 12. GROUP CLASSES TABLE
-- =======================================================
CREATE TABLE group_classes (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    expert_id INT NOT NULL,
    course_id INT NOT NULL,
    branch_id INT NOT NULL,
    group_name VARCHAR(150) NOT NULL,
    max_students INT DEFAULT 50,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (expert_id) REFERENCES experts(expert_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE
);

-- =======================================================
-- 13. GROUP MEMBERS TABLE
-- =======================================================
CREATE TABLE group_members (
    group_member_id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT NOT NULL,
    user_id INT NOT NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_id) REFERENCES group_classes(group_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- =======================================================
-- 14. DEFAULT ADMIN
-- =======================================================
INSERT INTO users (full_name, email, password_hash, role, country_id, language)
VALUES ('System Admin', 'admin@livinglibrary.com', 'admin123hash', 'admin', 2, 'English');


-- **********************************************************************************************************
-- CRUD --
-- **********************************************************************************************************
-- --------------------- CREATE ------------------------
-- **********************************************************************************************************


-- ✅COURSE CREATE ----------
-- ✅ Procedure for a new active course with begin_date and end_date
DROP PROCEDURE IF EXISTS new_active_course;
DELIMITER $$

CREATE PROCEDURE new_active_course(
    IN p_expert_id INT,
    IN p_branch_id INT,
    IN p_title VARCHAR(200),
    IN p_domain ENUM('inner','health','social','finance'),
    IN p_language VARCHAR(50),
    IN p_description TEXT,
    IN p_price DECIMAL(10,2),
    IN p_begin_date DATETIME,
    IN p_end_date DATETIME
)
BEGIN
    INSERT INTO courses (
        expert_id, 
        branch_id, 
        title, 
        domain, 
        language, 
        description, 
        price, 
        is_active, 
        begin_date, 
        end_date, 
        created_at, 
        updated_at
    )
    VALUES (
        p_expert_id,
        p_branch_id,
        p_title,
        p_domain,
        p_language,
        p_description,
        p_price,
        TRUE,
        p_begin_date,
        p_end_date,
        NOW(),
        NOW()
    );
END$$

DELIMITER ;

-- ✅ BOOKING CREATE ----------
-- ✅ Procedure for creating a new booking
DROP PROCEDURE IF EXISTS new_booking;
DELIMITER $$

CREATE PROCEDURE new_booking(
    IN p_course_id INT,
    IN p_expert_id INT,
    IN p_user_id INT,
    IN p_scheduled_time DATETIME,
    IN p_booking_type ENUM('live', 'group')
)
BEGIN
    /*
        This procedure inserts a new booking into the system.
        - Default status = 'booked'
        - Booking type defined by input (live / group)
        - created_at auto-filled
    */
    
    INSERT INTO bookings (
        course_id,
        expert_id,
        user_id,
        scheduled_time,
        status,
        booking_type,
        created_at
    )
    VALUES (
        p_course_id,
        p_expert_id,
        p_user_id,
        p_scheduled_time,
        'booked',
        p_booking_type,
        NOW()
    );
END$$

DELIMITER ;

-- ✅ BRANCH CREATE ----------
-- ✅ Procedure for creating a new branch
DROP PROCEDURE IF EXISTS new_branch;
DELIMITER $$

CREATE PROCEDURE new_branch(
    IN p_country_id INT,
    IN p_branch_name ENUM('inner','health','social','finance'),
    IN p_description TEXT
)
BEGIN
    /*
        This procedure inserts a new branch into the system.
        - Requires a valid country_id
        - branch_name must match ENUM values
        - created_at auto-filled
    */

    INSERT INTO branches (
        country_id,
        branch_name,
        description,
        created_at
    )
    VALUES (
        p_country_id,
        p_branch_name,
        p_description,
        NOW()
    );
END$$

DELIMITER ;

USE living_library_manage_system;

-- ✅ COUNTRIES CREATE ----------
-- ✅ Procedure for creating a new country
DROP PROCEDURE IF EXISTS new_country;
DELIMITER $$

CREATE PROCEDURE new_country(
    IN p_country_name VARCHAR(100),
    IN p_language VARCHAR(50),
    IN p_timezone VARCHAR(50)
)
BEGIN
    /*
        This procedure inserts a new country into the system.
        - Automatically sets created_at = NOW()
        - Accepts language and timezone for localization
    */

    INSERT INTO countries (
        country_name,
        language,
        timezone,
        created_at
    )
    VALUES (
        p_country_name,
        p_language,
        p_timezone,
        NOW()
    );
END$$

DELIMITER ;

-- ✅ EXPERTS CREATE ----------
-- ✅ Procedure for creating a new expert
DROP PROCEDURE IF EXISTS new_expert;
DELIMITER $$

CREATE PROCEDURE new_expert(
    IN p_user_id INT,
    IN p_branch_id INT,
    IN p_specialization ENUM('inner','health','social','finance'),
    IN p_bio TEXT,
    IN p_rating_avg DECIMAL(3,2),
    IN p_total_students INT,
    IN p_verified BOOLEAN
)
BEGIN
    INSERT INTO experts (
        user_id,
        branch_id,
        specialization,
        bio,
        rating_avg,
        total_students,
        verified,
        created_at
    )
    VALUES (
        p_user_id,
        p_branch_id,
        p_specialization,
        p_bio,
        IFNULL(p_rating_avg, 0.00),
        IFNULL(p_total_students, 0),
        IFNULL(p_verified, FALSE),
        NOW()
    );
END$$

DELIMITER ;

-- ✅ USERS CREATE ----------
-- ✅ Procedure for creating a new user
DROP PROCEDURE IF EXISTS new_user;
DELIMITER $$

CREATE PROCEDURE new_user(
    IN p_full_name VARCHAR(120),
    IN p_email VARCHAR(120),
    IN p_password_hash VARCHAR(255),
    IN p_role ENUM('participant','expert','admin'),
    IN p_country_id INT,
    IN p_branch_id INT,
    IN p_language VARCHAR(50)
)
BEGIN
    INSERT INTO users (
        full_name,
        email,
        password_hash,
        role,
        country_id,
        branch_id,
        language,
        created_at,
        updated_at
    )
    VALUES (
        p_full_name,
        p_email,
        p_password_hash,
        IFNULL(p_role, 'participant'),
        p_country_id,
        p_branch_id,
        IFNULL(p_language, 'English'),
        NOW(),
        NOW()
    );
END$$

DELIMITER ;




-- **********************************************************************************************************
-- --------------------- READ --------------------------

-- ======================================================
-- 15 Helper Functions
-- ======================================================
-- ✅ 22.10.2025
-- ✅ GET 
-- ✅ Get all active course per course_id:
DROP FUNCTION IF EXISTS func_is_course_active;
DELIMITER $$

CREATE FUNCTION func_is_course_active(course_id INT)
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE is_active_val BOOLEAN;

    SELECT is_active 
    INTO is_active_val
    FROM courses
    WHERE courses.course_id = course_id;

    RETURN (select group_concat(concat(title,':',language,':',connect_link))); #IFNULL(is_active_val, FALSE);
END $$

DELIMITER ;

-- USERS ----------------------------------------
-- ✅ function Get all users:
DROP FUNCTION IF EXISTS func_get_all_users;
DELIMITER $$
CREATE FUNCTION func_get_all_users()
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (SELECT GROUP_CONCAT(CONCAT(user_id, ':', full_name, ' (', role, ')') SEPARATOR ', ')
            FROM users);
END$$
DELIMITER ;

 -- ✅ procedure to get all users
DROP PROCEDURE IF EXISTS get_all_users;
DELIMITER $$

CREATE PROCEDURE get_all_users()
BEGIN
    SELECT 
        u.user_id,
        u.full_name,
        u.email,
        u.role,
        u.language,
        c.country_name,
        b.branch_name,
        u.created_at,
        u.updated_at
    FROM users u
    LEFT JOIN countries c ON u.country_id = c.country_id
    LEFT JOIN branches b ON u.branch_id = b.branch_id
    ORDER BY u.created_at DESC;
END$$

DELIMITER ;

 -- ✅ procedure to get one user by id
DROP PROCEDURE IF EXISTS get_user_by_id;
DELIMITER $$

CREATE PROCEDURE get_user_by_id(IN p_user_id INT)
BEGIN
    SELECT 
        u.*,
        c.country_name,
        b.branch_name
    FROM users u
    LEFT JOIN countries c ON u.country_id = c.country_id
    LEFT JOIN branches b ON u.branch_id = b.branch_id
    WHERE u.user_id = p_user_id;
END$$

DELIMITER ;


-- EXPERTS ----------------------------------------
-- ✅  Function to Get All Experts
DROP FUNCTION IF EXISTS func_get_all_experts;
DELIMITER $$
CREATE FUNCTION func_get_all_experts()
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (SELECT GROUP_CONCAT(CONCAT(e.expert_id, ':', u.full_name, ' - ', e.specialization) SEPARATOR ', ')
            FROM experts e
            JOIN users u ON e.user_id = u.user_id);
END$$
DELIMITER ;


-- ✅  Function to Get All Experts by Language
DROP FUNCTION IF EXISTS func_get_all_experts_by_language;
DELIMITER $$

CREATE FUNCTION func_get_all_experts_by_language(lang VARCHAR(50))
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (
        SELECT GROUP_CONCAT(
            CONCAT(
                'ID: ', e.expert_id,
                ' | Name: ', u.full_name,
                ' | Specialization: ', e.specialization,
                ' | Language: ', u.language,
                ' | Branch: ', b.branch_name
            ) SEPARATOR '\n'
        )
        FROM experts e
        JOIN users u ON e.user_id = u.user_id
        JOIN branches b ON e.branch_id = b.branch_id
        WHERE u.language = lang
        ORDER BY e.expert_id
    );
END$$

DELIMITER ;

-- ✅ TO GET ONE EXPERT BY ID
DROP PROCEDURE IF EXISTS get_expert_by_id;
DELIMITER $$

CREATE PROCEDURE get_expert_by_id(IN p_expert_id INT)
BEGIN
    SELECT 
        e.*,
        u.full_name,
        b.branch_name
    FROM experts e
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON e.branch_id = b.branch_id
    WHERE e.expert_id = p_expert_id;
END$$

DELIMITER ;


-- ✅  Function to Get Top Experts
DROP FUNCTION IF EXISTS func_get_top_experts;
DELIMITER $$
CREATE FUNCTION func_get_top_experts()
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (
        SELECT GROUP_CONCAT(CONCAT(u.full_name, ' (', e.rating_avg, ')') ORDER BY e.rating_avg DESC SEPARATOR ', ')
        FROM experts e
        JOIN users u ON e.user_id = u.user_id
        WHERE e.rating_avg >= 4.8
    );
END$$
DELIMITER ;



-- COURSES ----------------------------------------
-- ✅  Function to Get All active Courses
DROP FUNCTION IF EXISTS func_get_active_courses;
DELIMITER $$
CREATE FUNCTION func_get_active_courses()
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (SELECT GROUP_CONCAT(CONCAT(c.course_id, ':', c.title, ' [', c.domain, ']') SEPARATOR ', ')
            FROM courses c
            WHERE c.is_active = TRUE);
END$$
DELIMITER ;


-- ✅  Function to Get All Active Courses By Branch
DROP FUNCTION IF EXISTS func_active_courses_by_branch;
DELIMITER $$
CREATE FUNCTION func_active_courses_by_branch(p_branch_name VARCHAR(50))
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    DECLARE result_text VARCHAR(5000);

    SELECT 
        GROUP_CONCAT(
            CONCAT(
                'Branch: ', b.branch_name, 
                ' | Course: ', c.title, 
                ' | Description: ', c.description, 
                ' | Language: ', c.language
            ) 
            SEPARATOR '\n'
        )
    INTO result_text
    FROM courses c
    JOIN branches b ON c.branch_id = b.branch_id
    WHERE b.branch_name = p_branch_name
      AND c.is_active = TRUE;

    RETURN IFNULL(result_text, CONCAT('No active courses found for branch "', p_branch_name, '"'));
END$$
DELIMITER ;


-- ✅  Function to Get All Most Population Courses
DROP FUNCTION IF EXISTS func_most_popular_course;
DELIMITER $$
CREATE FUNCTION func_most_popular_course()
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    RETURN (
        SELECT title 
        FROM courses 
        ORDER BY total_students DESC 
        LIMIT 10
    );
END$$
DELIMITER ;

-- CREATE VIEW----------
USE Living_library_manage_system;

-- ---------- CREATE VIEW ----------
DROP VIEW IF EXISTS view_best_courses_by_month;

CREATE VIEW view_best_courses_by_month AS
SELECT 
    c.course_id,
    c.title AS course_title,
    c.domain,
    b.branch_name,
    u.full_name AS expert_name,
    COUNT(bo.booking_id) AS total_bookings,
    DATE_FORMAT(MIN(bo.scheduled_time), '%Y-%m') AS booking_month,
    MONTHNAME(MIN(bo.scheduled_time)) AS month_name,
    YEAR(MIN(bo.scheduled_time)) AS year_active
FROM bookings bo
JOIN courses c ON bo.course_id = c.course_id
JOIN experts e ON c.expert_id = e.expert_id
JOIN users u ON e.user_id = u.user_id
JOIN branches b ON c.branch_id = b.branch_id
WHERE bo.status IN ('booked', 'completed')
GROUP BY 
    c.course_id,
    c.title,
    c.domain,
    b.branch_name,
    u.full_name,
    YEAR(bo.scheduled_time),
    MONTH(bo.scheduled_time)
ORDER BY 
    YEAR(MIN(bo.scheduled_time)),
    MONTH(MIN(bo.scheduled_time)),
    total_bookings DESC;


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




-- BOOKINGS ----------------------------------------
-- ✅  Function to Get All active bookings
DROP FUNCTION IF EXISTS func_get_all_bookings;
DELIMITER $$
CREATE FUNCTION func_get_all_bookings()
RETURNS VARCHAR(5000)
DETERMINISTIC
BEGIN
    RETURN (SELECT GROUP_CONCAT(CONCAT('Booking#', b.booking_id, ':', u.full_name, ' -> ', c.title, ' [', b.status, ']') SEPARATOR ', ')
            FROM bookings b
            JOIN users u ON b.user_id = u.user_id
            JOIN courses c ON b.course_id = c.course_id);
END$$
DELIMITER ;

-- BRANCHES ----------------------------------------
-- ✅  Function to Get All Branch by countries
DROP FUNCTION IF EXISTS func_get_branches_by_country;
DELIMITER $$
CREATE FUNCTION func_get_branches_by_country(country_name VARCHAR(100))
RETURNS VARCHAR(2000)
DETERMINISTIC
BEGIN
    RETURN (
        SELECT GROUP_CONCAT(branch_name SEPARATOR ', ')
        FROM branches
        WHERE country_id = (
            SELECT country_id FROM countries WHERE country_name = country_name LIMIT 1
        )
    );
END$$
DELIMITER ;

-- ✅ procedure to get all branches
USE living_library_manage_system;

DROP PROCEDURE IF EXISTS get_all_branches;
DELIMITER $$

CREATE PROCEDURE get_all_branches()
BEGIN
    SELECT 
        b.branch_id,
        b.branch_name,
        b.description,
        b.created_at,
        c.country_name,
        c.language AS country_language,
        c.timezone
    FROM branches b
    JOIN countries c ON b.country_id = c.country_id
    ORDER BY c.country_name, b.branch_name;
END$$

DELIMITER ;


-- ✅ procedure to get one branche by id
DROP PROCEDURE IF EXISTS get_branch_by_id;
DELIMITER $$

CREATE PROCEDURE get_branch_by_id(IN p_branch_id INT)
BEGIN
    SELECT 
        b.*,
        c.country_name
    FROM branches b
    JOIN countries c ON b.country_id = c.country_id
    WHERE b.branch_id = p_branch_id;
END$$

DELIMITER ;



-- ======================================================
-- PROCEDURE - READ
-- ======================================================
-- USERS ------------------------------------------------
-- ✅  Procedure to Get All users by Language
DROP PROCEDURE IF EXISTS proc_get_all_users_by_language;
DELIMITER $$
CREATE PROCEDURE proc_get_all_users_by_language(IN lang VARCHAR(50))
BEGIN
    SELECT 
        u.user_id,
        u.full_name,
        u.email,
        u.role,
        u.language,
        c.country_name,
        b.branch_name
    FROM users u
    LEFT JOIN countries c ON u.country_id = c.country_id
    LEFT JOIN branches b ON u.branch_id = b.branch_id
    WHERE u.language = lang
    ORDER BY u.role, u.full_name;
END$$
DELIMITER ;

-- EXPERTS------------------------------------------------
-- ✅  Procedure To Get All Experts by Language
DROP PROCEDURE IF EXISTS proc_get_all_experts_by_language;
DELIMITER $$
CREATE PROCEDURE proc_get_all_experts_by_language(IN lang VARCHAR(50))
BEGIN
    SELECT 
        e.expert_id AS ExpertID,
        u.full_name AS ExpertName,
        e.specialization AS Specialization,
        u.language AS Language,
        b.branch_name AS Branch,
        c.country_name AS Country,
        e.rating_avg AS Rating,
        e.total_students AS TotalStudents,
        e.verified AS VerifiedStatus
    FROM experts e
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON e.branch_id = b.branch_id
    JOIN countries c ON u.country_id = c.country_id
    WHERE u.language = lang
    ORDER BY e.rating_avg DESC, u.full_name ASC;
END$$
DELIMITER ;

-- ✅  Procedure To Get All Experts
DROP PROCEDURE IF EXISTS get_all_experts;
DELIMITER $$

CREATE PROCEDURE get_all_experts()
BEGIN
    SELECT 
        e.expert_id,
        u.full_name AS expert_name,
        e.specialization,
        e.rating_avg,
        e.total_students,
        e.verified,
        b.branch_name,
        e.created_at
    FROM experts e
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON e.branch_id = b.branch_id
    ORDER BY e.created_at DESC;
END$$

DELIMITER ;

-- ✅  Procedure To Get one Experts by id
DROP PROCEDURE IF EXISTS get_expert_by_id;
DELIMITER $$

CREATE PROCEDURE get_expert_by_id(IN p_expert_id INT)
BEGIN
    SELECT 
        e.*,
        u.full_name,
        b.branch_name
    FROM experts e
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON e.branch_id = b.branch_id
    WHERE e.expert_id = p_expert_id;
END$$

DELIMITER ;


-- ✅ COURSES ------------------------------------------------
-- ✅  Procedure To Get All ACTIVE COURSES
DROP PROCEDURE IF EXISTS proc_get_active_courses;
DELIMITER $$
CREATE PROCEDURE proc_get_active_courses()
BEGIN
    SELECT 
        c.domain AS Branch,
        c.course_id,
        c.title,
        u.full_name AS Coacher,
        c.language,
        c.price,
        c.avg_rating,
        c.total_students,
        c.is_active
    FROM courses c
    JOIN experts e ON e.expert_id = c.expert_id
    JOIN users u ON u.user_id = e.user_id
    WHERE c.is_active = TRUE
     ORDER BY c.domain ASC;
END$$
DELIMITER ;

-- ✅  Procedure To Get All ACTIVE COURSES BY BRANCH WITH INPUT FIELD FOR BRANCH
DROP PROCEDURE IF EXISTS proc_get_active_courses_by_branch;
DELIMITER $$
CREATE PROCEDURE proc_get_active_courses_by_branch(IN p_branch_name VARCHAR(50))
BEGIN
    SELECT 
        b.branch_name AS Branch,
        c.course_id AS CourseID,
        c.title AS Title,
        c.description AS Description,
        c.language AS Language,
        u.full_name AS Coacher,
        c.price AS Price,
        c.avg_rating AS Rating,
        c.total_students AS TotalStudents,
        CASE WHEN c.is_active = TRUE THEN 'Active' ELSE 'Inactive' END AS ActiveStatus
    FROM courses c
        JOIN branches b ON c.branch_id = b.branch_id
        JOIN experts e ON e.expert_id = c.expert_id
        JOIN users u ON u.user_id = e.user_id
    WHERE b.branch_name = p_branch_name
      AND c.is_active = TRUE
    ORDER BY b.branch_name ASC, c.avg_rating DESC, c.title ASC;
END$$
DELIMITER ;


--  ✅ To get all course active now and will active in the future, sorted by month
DROP PROCEDURE IF EXISTS proc_get_courses;
DELIMITER $$

CREATE PROCEDURE proc_get_courses()
BEGIN
    /*
        This procedure returns all courses:
        - already active (is_active = 1)
        - or scheduled to be active in the future (begin_date >= NOW())
        Sorted by the month of begin_date (earliest first).
    */

    SELECT 
        c.course_id,
        c.title,
        c.domain,
        c.language,
        c.price,
        c.begin_date,
        c.end_date,
		CASE WHEN c.is_active = TRUE THEN 'Active' ELSE 'Inactive' END AS ActiveStatus,
        u.full_name AS expert_name,
        MONTHNAME(c.begin_date) AS month_name,
        YEAR(c.begin_date) AS year_active
    FROM courses c
    JOIN experts e ON c.expert_id = e.expert_id
    JOIN users u ON e.user_id = u.user_id
    WHERE 
        (c.is_active = 1 OR (c.begin_date IS NOT NULL AND c.begin_date >= NOW()))
    ORDER BY 
        YEAR(c.begin_date),
        MONTH(c.begin_date),
        c.begin_date;
END$$

DELIMITER ;


--  ✅ To get all courses
DROP PROCEDURE IF EXISTS get_all_courses;
DELIMITER $$

CREATE PROCEDURE get_all_courses()
BEGIN
    SELECT 
        c.course_id AS ID,
        c.title AS Title,
        c.domain AS Branch,
        c.language,
        c.description,
        #c.connect_link,
        #c.price,
        #c.avg_rating,
        #c.total_students,
        #c.is_active,
        c.begin_date AS Begin,
        c.end_date AS End
        #u.full_name AS expert_name,
    FROM courses c
    JOIN experts e ON c.expert_id = e.expert_id
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON c.branch_id = b.branch_id
    ORDER BY c.created_at DESC;
END$$

DELIMITER ;

--  ✅ To get one course by id
DROP PROCEDURE IF EXISTS get_course_by_id;
DELIMITER $$

CREATE PROCEDURE get_course_by_id(IN p_course_id INT)
BEGIN
    SELECT 
        c.course_id AS ID,
        c.title AS Title,
        c.domain AS Branch,
        c.language,
        c.description,
        #c.connect_link,
        #c.price,
        #c.avg_rating,
        #c.total_students,
        #c.is_active,
        c.begin_date AS Begin,
        c.end_date AS End,
        u.full_name AS expert_name,
        b.branch_name
    FROM courses c
    JOIN experts e ON c.expert_id = e.expert_id
    JOIN users u ON e.user_id = u.user_id
    JOIN branches b ON c.branch_id = b.branch_id
    WHERE c.course_id = p_course_id;
END$$

DELIMITER ;


-- ✅ BOOKINGS
-- ✅ get all bookings

DROP PROCEDURE IF EXISTS get_all_bookings;
DELIMITER $$

CREATE PROCEDURE get_all_bookings()
BEGIN
    SELECT 
        b.booking_id,
        b.scheduled_time,
        b.status,
        b.booking_type,
        b.created_at,
        u.full_name AS participant_name,
        e.expert_id,
        ue.full_name AS expert_name,
        c.title AS course_title
    FROM bookings b
    JOIN users u ON b.user_id = u.user_id
    JOIN experts e ON b.expert_id = e.expert_id
    JOIN users ue ON e.user_id = ue.user_id
    JOIN courses c ON b.course_id = c.course_id
    ORDER BY b.scheduled_time DESC;
END$$

DELIMITER ;

-- ✅get booking by id
DROP PROCEDURE IF EXISTS get_booking_by_id;
DELIMITER $$

CREATE PROCEDURE get_booking_by_id(IN p_booking_id INT)
BEGIN
    SELECT 
        b.*,
        u.full_name AS participant_name,
        ue.full_name AS expert_name,
        c.title AS course_title
    FROM bookings b
    JOIN users u ON b.user_id = u.user_id
    JOIN experts e ON b.expert_id = e.expert_id
    JOIN users ue ON e.user_id = ue.user_id
    JOIN courses c ON b.course_id = c.course_id
    WHERE b.booking_id = p_booking_id;
END$$

DELIMITER ;


--  ✅ BRANCHES

--  ✅ COUNTRIES 
-- to get all countries
DROP PROCEDURE IF EXISTS get_all_countries;
DELIMITER $$

CREATE PROCEDURE get_all_countries()
BEGIN
    SELECT 
        country_id,
        country_name,
        language,
        timezone,
        created_at
    FROM countries
    ORDER BY country_name;
END$$

DELIMITER ;

-- to get country by id
DROP PROCEDURE IF EXISTS get_country_by_id;
DELIMITER $$

CREATE PROCEDURE get_country_by_id(IN p_country_id INT)
BEGIN
    SELECT 
        c.country_id,
        c.country_name,
        c.language,
        c.timezone,
        c.created_at
    FROM countries c
    WHERE c.country_id = p_country_id;
END$$

DELIMITER ;


--  ✅ ANALYTICS


-- FAVOURITES -----------------------------------------------
-- GROUP MEMBERS --------------------------------------------
-- GROUP CLASS ----------------------------------------------
-- INVITATIONS ----------------------------------------------

-- **********************************************************************************************************
-- --------------------- UPDATE ------------------------
-- **********************************************************************************************************
--  ✅ USERS
DROP PROCEDURE IF EXISTS update_user;
DELIMITER $$

CREATE PROCEDURE update_user(
    IN p_user_id INT,
    IN p_full_name VARCHAR(120),
    IN p_email VARCHAR(120),
    IN p_password_hash VARCHAR(255),
    IN p_role ENUM('participant','expert','admin'),
    IN p_country_id INT,
    IN p_branch_id INT,
    IN p_language VARCHAR(50)
)
BEGIN
    UPDATE users
    SET
        full_name = IFNULL(p_full_name, full_name),
        email = IFNULL(p_email, email),
        password_hash = IFNULL(p_password_hash, password_hash),
        role = IFNULL(p_role, role),
        country_id = IFNULL(p_country_id, country_id),
        branch_id = IFNULL(p_branch_id, branch_id),
        language = IFNULL(p_language, language),
        updated_at = NOW()
    WHERE user_id = p_user_id;
END$$

DELIMITER ;


--  ✅ EXPERTS 
DROP PROCEDURE IF EXISTS update_expert;
DELIMITER $$

CREATE PROCEDURE update_expert(
    IN p_expert_id INT,
    IN p_bio TEXT,
    IN p_rating_avg DECIMAL(3,2),
    IN p_total_students INT,
    IN p_verified BOOLEAN
)
BEGIN
    UPDATE experts
    SET
        bio = IFNULL(p_bio, bio),
        rating_avg = IFNULL(p_rating_avg, rating_avg),
        total_students = IFNULL(p_total_students, total_students),
        verified = IFNULL(p_verified, verified)
    WHERE expert_id = p_expert_id;
END$$

DELIMITER ;

--  ✅ COURSES

DROP PROCEDURE IF EXISTS update_course;
DELIMITER $$

CREATE PROCEDURE update_course(
    IN p_course_id INT,
    IN p_title VARCHAR(200),
    IN p_description TEXT,
    IN p_connect_link VARCHAR(255),
    IN p_price DECIMAL(10,2),
    IN p_avg_rating DECIMAL(3,2),
    IN p_total_students INT,
    IN p_is_active BOOLEAN,
    IN p_begin_date DATETIME,
    IN p_end_date DATETIME
)
BEGIN
    UPDATE courses
    SET
        title = IFNULL(p_title, title),
        description = IFNULL(p_description, description),
        connect_link = IFNULL(p_connect_link, connect_link),
        price = IFNULL(p_price, price),
        avg_rating = IFNULL(p_avg_rating, avg_rating),
        total_students = IFNULL(p_total_students, total_students),
        is_active = IFNULL(p_is_active, is_active),
        begin_date = IFNULL(p_begin_date, begin_date),
        end_date = IFNULL(p_end_date, end_date),
        updated_at = NOW()
    WHERE course_id = p_course_id;
END$$

DELIMITER ;


--  ✅ BOOKINGS
DROP PROCEDURE IF EXISTS update_booking;
DELIMITER $$

CREATE PROCEDURE update_booking(
    IN p_booking_id INT,
    IN p_status ENUM('booked','completed','cancelled'),
    IN p_scheduled_time DATETIME,
    IN p_booking_type ENUM('live','group')
)
BEGIN
    UPDATE bookings
    SET
        status = IFNULL(p_status, status),
        scheduled_time = IFNULL(p_scheduled_time, scheduled_time),
        booking_type = IFNULL(p_booking_type, booking_type)
    WHERE booking_id = p_booking_id;
END$$

DELIMITER ;

--  ✅ BRANCHES
DROP PROCEDURE IF EXISTS update_branch;
DELIMITER $$

CREATE PROCEDURE update_branch(
    IN p_branch_id INT,
    IN p_description TEXT,
    IN p_country_id INT
)
BEGIN
    UPDATE branches
    SET
        description = IFNULL(p_description, description),
        country_id = IFNULL(p_country_id, country_id)
    WHERE branch_id = p_branch_id;
END$$

DELIMITER ;

--  ✅ COUNTRIES 
DROP PROCEDURE IF EXISTS update_country;
DELIMITER $$

CREATE PROCEDURE update_country(
    IN p_country_id INT,
    IN p_country_name VARCHAR(100),
    IN p_language VARCHAR(50),
    IN p_timezone VARCHAR(50)
)
BEGIN
    UPDATE countries
    SET
        country_name = IFNULL(p_country_name, country_name),
        language = IFNULL(p_language, language),
        timezone = IFNULL(p_timezone, timezone)
    WHERE country_id = p_country_id;
END$$

DELIMITER ;

--  ✅ ANALYTICS
-- **********************************************************************************************************
-- --------------------- DELETE ------------------------
-- **********************************************************************************************************
--  ✅ USERS
DROP PROCEDURE IF EXISTS delete_user;
DELIMITER $$

CREATE PROCEDURE delete_user(IN p_user_id INT)
BEGIN
    DELETE FROM users
    WHERE user_id = p_user_id;
END$$

DELIMITER ;

--  ✅ EXPERTS
DROP PROCEDURE IF EXISTS delete_expert;
DELIMITER $$

CREATE PROCEDURE delete_expert(IN p_expert_id INT)
BEGIN
    DELETE FROM experts
    WHERE expert_id = p_expert_id;
END$$

DELIMITER ;

--  ✅ COURSES
DROP PROCEDURE IF EXISTS delete_course;
DELIMITER $$

CREATE PROCEDURE delete_course(IN p_course_id INT)
BEGIN
    DELETE FROM courses
    WHERE course_id = p_course_id;
END$$

DELIMITER ;

--  ✅ BOOKINGS
DROP PROCEDURE IF EXISTS delete_booking;
DELIMITER $$

CREATE PROCEDURE delete_booking(IN p_booking_id INT)
BEGIN
    DELETE FROM bookings
    WHERE booking_id = p_booking_id;
END$$

DELIMITER ;

--  ✅ BRANCHES
DROP PROCEDURE IF EXISTS delete_branch;
DELIMITER $$

CREATE PROCEDURE delete_branch(IN p_branch_id INT)
BEGIN
    DELETE FROM branches
    WHERE branch_id = p_branch_id;
END$$

DELIMITER ;

--  ✅ COUNTRIES 
DROP PROCEDURE IF EXISTS delete_country;
DELIMITER $$

CREATE PROCEDURE delete_country(IN p_country_id INT)
BEGIN
    DELETE FROM countries
    WHERE country_id = p_country_id;
END$$

DELIMITER ;

--  ✅ ANALYTICS