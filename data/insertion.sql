USE living_library_manage_system;

-- =======================================================
-- 1. Insert 10 countries 
-- =======================================================


-- =======================================================
-- 2. Insert 25 users (17 participants, 8 experts)
-- =======================================================

-- Insert 4 main branches (you can adjust country_id if needed)
INSERT INTO branches (country_id, branch_name, description)
VALUES
(2, 'inner', 'Inner Self & Mindfulness — for emotional intelligence, awareness, and balance.'),
(2, 'health', 'Physical and Mental Health — for body, mind, and holistic wellbeing.'),
(2, 'social', 'Social and Family Relationship — for empathy, communication, and connection.'),
(2, 'finance', 'Finance and Career Empowerment — for abundance, stability, and purpose.');


-- =======================================================
-- 3. Insert 25 users (17 participants, 8 experts)
-- =======================================================
INSERT INTO users (full_name, email, password_hash, role, country_id, branch_id, language)
VALUES
('Anna Nguyen', 'anna.nguyen@gmail.com', 'hash1', 'participant', 2, 1, 'German'),
('Mai Le', 'mai.le@gmail.com', 'hash2', 'participant', 3, 1, 'Vietnamese'),
('David Tran', 'david.tran@gmail.com', 'hash3', 'participant', 3, 2, 'Vietnamese'),
('Lisa Becker', 'lisa.becker@gmail.com', 'hash4', 'participant', 2, 3, 'German'),
('Hiro Tanaka', 'hiro.tanaka@gmail.com', 'hash5', 'participant', 4, 1, 'Japanese'),
('Chloe Dubois', 'chloe.dubois@gmail.com', 'hash6', 'participant', 5, 2, 'French'),
('Thomas Nguyen', 'thomas.nguyen@gmail.com', 'hash7', 'participant', 3, 4, 'Vietnamese'),
('Sophie Müller', 'sophie.mueller@gmail.com', 'hash8', 'participant', 2, 1, 'German'),
('Olivia Carter', 'olivia.carter@gmail.com', 'hash9', 'participant', 6, 3, 'English'),
('Ben Davis', 'ben.davis@gmail.com', 'hash10', 'participant', 6, 2, 'English'),
('Marie Laurent', 'marie.laurent@gmail.com', 'hash11', 'participant', 5, 4, 'French'),
('Taro Kato', 'taro.kato@gmail.com', 'hash12', 'participant', 4, 1, 'Japanese'),
('Hung Pham', 'hung.pham@gmail.com', 'hash13', 'participant', 3, 3, 'Vietnamese'),
('Yuki Sato', 'yuki.sato@gmail.com', 'hash14', 'participant', 4, 4, 'Japanese'),
('Emily Brown', 'emily.brown@gmail.com', 'hash15', 'participant', 6, 1, 'English'),
('Attila Kovacs', 'attila.kovacs@gmail.com', 'hash16', 'participant', 7, 2, 'Hungarian'),
('Peter Horvath', 'peter.horvath@gmail.com', 'hash17', 'participant', 7, 3, 'Hungarian'),

-- 8 Experts / Admins
('Dr. Lara Phan', 'lara.phan@gmail.com', 'hash18', 'expert', 3, 1, 'Vietnamese'),
('Dr. Martin Weiss', 'martin.weiss@gmail.com', 'hash19', 'expert', 2, 2, 'German'),
('Dr. Alice Tan', 'alice.tan@gmail.com', 'hash20', 'expert', 4, 1, 'Japanese'),
('Dr. Jean Rousseau', 'jean.rousseau@gmail.com', 'hash21', 'expert', 5, 3, 'French'),
('Dr. Emma Nguyen', 'emma.nguyen@gmail.com', 'hash22', 'expert', 3, 4, 'Vietnamese'),
('Dr. Daniel Baker', 'daniel.baker@gmail.com', 'hash23', 'expert', 6, 2, 'English'),
('Dr. Zoltan Farkas', 'zoltan.farkas@gmail.com', 'hash24', 'expert', 7, 1, 'Hungarian'),
('Dr. Julia Smith', 'julia.smith@gmail.com', 'hash25', 'admin', 6, 4, 'English');

select * from users;
-- =======================================================
-- 4. Insert 8 experts
-- =======================================================
INSERT INTO experts 
(user_id, branch_id, specialization, bio, rating_avg, total_students, verified)
VALUES
(121, 1, 'inner', 'Mindfulness and emotional balance expert.', 4.8, 120, TRUE),
(122, 2, 'health', 'Holistic health coach and psychologist.', 4.7, 85, TRUE),
(123, 1, 'inner', 'Meditation mentor focusing on spiritual growth.', 4.9, 140, TRUE),
(124, 3, 'social', 'Family relationship consultant.', 4.5, 90, TRUE),
(125, 4, 'finance', 'Personal finance and career development mentor.', 4.8, 110, TRUE),
(126, 2, 'health', 'Mental health expert for work-life balance.', 4.6, 75, TRUE),
(127, 1, 'inner', 'Hungarian mindfulness practitioner and therapist.', 4.9, 60, TRUE),
(128, 4, 'finance', 'Admin & senior coach in life strategy.', 5.0, 300, TRUE);


-- =======================================================
-- 5. Insert 8 courses
-- =======================================================
INSERT INTO courses (expert_id, branch_id, title, domain, language, description, price, avg_rating, total_students)
VALUES
(49, 1, 'Mindfulness Basics', 'inner', 'Vietnamese', 'Daily mindfulness training for beginners.', 25.00, 4.8, 120),
(49, 2, 'Healthy Mind, Healthy Life', 'health', 'German', 'Integrative health principles.', 30.00, 4.7, 85),
(50, 1, 'Meditation for Focus', 'inner', 'Japanese', 'Guided meditation and breathing practice.', 20.00, 4.9, 140),
(50, 3, 'Harmony in Relationships', 'social', 'French', 'Enhance communication and empathy.', 28.00, 4.5, 90),
(50, 4, 'Financial Clarity 101', 'finance', 'Vietnamese', 'Practical finance for new professionals.', 22.00, 4.8, 110),
(51, 2, 'Work-Life Reset', 'health', 'English', 'Stress management and mental balance.', 35.00, 4.6, 75),
(51, 1, 'Silence and Awareness', 'inner', 'Hungarian', 'Mindful presence practices.', 18.00, 4.9, 60),
(52, 4, 'Global Strategy & Growth', 'finance', 'English', 'Advanced career leadership program.', 40.00, 5.0, 300);
describe courses;


-- INSERT INNER
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(49, 1, 'Mindfulness for Beginners', 'inner', 'English',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-21 00:00:00', '2025-12-21 00:00:00', 24.00, 4.8, 120),

(49, 1, 'Deep Breathing Awareness', 'inner', 'Vietnamese',
 'A calming practice to connect breath and body awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.7, 100),

(50, 1, 'Silent Power of the Present Moment', 'inner', 'Japanese',
 'Discover peace through present-moment meditation.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-15 00:00:00', '2025-11-30 00:00:00', 26.00, 4.9, 130),

(50, 1, 'Inner Transformation & Self-Discovery', 'inner', 'English',
 'Learn to shift inner energy and find emotional clarity.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-30 00:00:00', '2025-12-20 00:00:00', 28.00, 4.8, 140),

(51, 1, 'Meditative Movement Flow', 'inner', 'French',
 'A mix of movement and stillness for balance and awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-25 00:00:00', '2025-12-05 00:00:00', 25.00, 4.6, 95),

(51, 1, 'Gratitude Practice & Joyful Living', 'inner', 'English',
 'Develop gratitude habits that lift your emotional state.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 00:00:00', '2025-12-21 00:00:00', 23.00, 4.7, 105),

(52, 1, 'Energy of Stillness', 'inner', 'German',
 'Learn how inner silence improves focus and creativity.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-12-05 00:00:00', 29.00, 4.9, 115),

(52, 1, 'Compassion & Mindful Relationships', 'inner', 'Vietnamese',
 'Apply mindfulness in emotional connection and empathy.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-11-30 00:00:00', 27.00, 4.8, 98),

(49, 1, 'Clarity Through Meditation', 'inner', 'Hungarian',
 'Build clarity and reduce stress through mindful breathing.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-12-21 00:00:00', 20.00, 4.9, 120),

(50, 1, 'The Path to Inner Freedom', 'inner', 'English',
 'Release limiting thoughts and reconnect with your essence.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-25 00:00:00', '2025-12-21 00:00:00', 32.00, 4.95, 150);


INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(55, 1, 'Mindfulness for Beginners', 'inner', 'German',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 20:00:00', '2025-11-21 00:00:00', 24.00, 4.8, 120),
(60, 1, 'Mindfulness for Beginners', 'inner', 'Hungarian',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 20:00:00', '2025-11-21 0:00:00', 24.00, 4.8, 120);


-- INSERT 
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(49, 1, 'Mindfulness for Beginners', 'health', 'Vietnamese',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-21 00:00:00', '2025-12-21 00:00:00', 24.00, 4.8, 120),

(49, 1, 'Deep Breathing Awareness', 'inner', 'Vietnamese',
 'A calming practice to connect breath and body awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.7, 100);
 
-- INSERT HEALTH
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date, end_date, price, avg_rating, total_students)
VALUES
-- 1️⃣ Mind–Body Harmony (German)
(50, 2, 'Mind–Body Harmony', 'health', 'German',
 'Discover how nutrition, movement, and meditation work together to restore your body–mind balance.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-20 20:00:00', '2025-11-23 00:00:00', 29.00, 4.8, 95),

-- 2️⃣ Resilience and Stress Detox (English)
(54, 2, 'Resilience and Stress Detox', 'health', 'English',
 'A practical workshop on building mental resilience and releasing stress through body awareness and breathwork.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-20 20:00:00', '2025-11-23 00:00:00', 32.00, 4.7, 120),

-- 3️⃣ Holistic Nutrition for Energy (German)
(50, 2, 'Holistic Nutrition for Energy', 'health', 'German',
 'Learn to optimize daily vitality through integrative nutrition habits supported by mindfulness practice.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-23 10:00:00', '2025-11-23 00:00:00', 27.00, 4.9, 110),

-- 4️⃣ Emotional Wellbeing in Motion (English)
(54, 2, 'Emotional Wellbeing in Motion', 'health', 'English',
 'Explore movement and breathing sequences designed to free emotional tension and improve vitality.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-11-10 17:00:00', '2025-12-10 00:00:00', 30.00, 4.6, 105),

-- 5️⃣ Sleep, Breath, and Inner Calm (German)
(50, 2, 'Sleep, Breath, and Inner Calm', 'health', 'German',
 'Techniques for better sleep quality and stress release through mindful breathing and restorative rest.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-11-15 21:00:00', '2025-12-15 00:00:00', 26.00, 4.9, 98);

-- INSERT SOCIAL
INSERT INTO courses 
(expert_id, branch_id, title, domain, language, description, connect_link, 
 begin_date, end_date, price, avg_rating, total_students)
VALUES
(52, 3, "L'harmonie dans les relations", 'social', 'French',
"L'empathie et une compréhension plus profonde pour créer des relations harmonieuses en famille et au travail.",
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-27 18:00:00', '2025-11-27 00:00:00', 25.00, 4.8, 110),

(52, 3, 'Communication authentique', 'social', 'French',
 'Apprenez la communication non violente pour exprimer clairement vos besoins et écouter avec ouverture.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-11-05 19:00:00', '2025-12-05 00:00:00', 27.00, 4.9, 125),

(52, 3, 'Building Trust in Teams', 'social', 'English',
 'Practical framework to strengthen collaboration and build trust in professional and family teams.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-20 18:30:00', '2025-12-10 00:00:00', 26.00, 4.7, 100),

(52, 3, 'Du conflit à la connexion dans la communauté', 'social', 'French',
 "Transformer les conflits en opportunités de croissance mutuelle grâce à l'écoute active et à l'intelligence émotionnelle.",
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-28 17:30:00', '2025-12-12 00:00:00', 29.00, 4.9, 115),

(52, 3, "L'art de l'intelligence sociale", 'social', 'French',
 'Développez votre conscience sociale et votre empathie pour construire des relations épanouissantes entre les cultures.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-11-16 20:00:00', '2025-12-16 00:00:00', 30.00, 4.8, 140);

-- INSERT FINANCE
INSERT INTO courses 
(expert_id, branch_id, title, domain, language, description, connect_link, 
 begin_date, end_date, price, avg_rating, total_students)
VALUES
(53, 4, 'Tự Do Tài Chính', 'finance', 'Vietnamese',
 'Học các kỹ năng lập ngân sách, tiết kiệm và đầu tư cốt lõi để tạo ra sự tự do tài chính bền vững.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-03 18:00:00', '2025-12-03 00:00:00', 32.00, 4.8, 150),

(53, 4, 'Leadership and Money Mindset', 'finance', 'English',
 'Explore the psychology of abundance and develop leadership principles to grow your financial vision.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-06 19:30:00', '2025-12-06 00:00:00', 36.00, 4.9, 180),

(53, 4, 'Phụ nữ và Sự Giàu có', 'finance', 'Vietnamese',
 'Lớp học chuyên sâu giúp phụ nữ quản lý tiền bạc một cách khôn ngoan và lập kế hoạch bảo đảm an ninh lâu dài.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-09 20:00:00', '2025-12-09 00:00:00', 28.00, 4.7, 130),

(56, 4, 'Career Growth through Smart Finance', 'finance', 'English',
 'Understand how financial planning enhances career choices and business growth.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-12 18:30:00', '2025-12-12 00:00:00', 30.00, 4.8, 170),

(53, 4, 'Thịnh vượng toàn diện', 'finance', 'Vietnamese',
 'Một cách tiếp cận lấy trái tim làm trọng tâm để cân bằng sự giàu có, hạnh phúc và mục đích trong cuộc sống hiện đại.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-15 19:00:00', '2025-12-15 00:00:00', 34.00, 4.9, 160);


set sql_safe_updates =0;
delete from experts where expert_id=61;
set sql_safe_updates =1;
select * from experts;
select * from courses;
describe courses;
select * from users where user_id = 125 or user_id= 128; #role = 'expert';

-- =======================================================
-- 6. Insert 8 bookings
-- =======================================================
-- Random booking examples between participants and experts
INSERT INTO bookings (course_id, expert_id, user_id, scheduled_time, status)
VALUES
(17, 17, 104, NOW() + INTERVAL 1 DAY, 'booked'),
(18, 18, 105, NOW() + INTERVAL 2 DAY, 'completed'),
(19, 19, 106, NOW() + INTERVAL 1 HOUR, 'booked'),
(20, 20, 124, NOW() + INTERVAL 3 HOUR, 'booked'),
(21, 21, 127, NOW() + INTERVAL 1 DAY, 'booked'),
(22, 22, 122, NOW() + INTERVAL 4 HOUR, 'completed'),
(23, 23, 110, NOW() + INTERVAL 2 HOUR, 'booked'),
(24, 24, 111, NOW() + INTERVAL 1 HOUR, 'booked');

-- =======================================================
-- 7. Insert 4 analytics
-- =======================================================
INSERT INTO analytics (metric_type, reference_id, metric_value, country_id, branch_id)
VALUES
('student_count', 1, 120, 3, 1),
('expert_count', 1, 8, 3, 1),
('course_popularity', 5, 110, 3, 4),
('rating_avg', 1, 4.8, 3, 1);


-- ===============================================
-- 1️⃣ FAVORITES (users marking experts/courses they like)
-- ===============================================
INSERT INTO favorites (user_id, expert_id, course_id, created_at)
VALUES
(121, 17, 17, NOW()),  -- Anna likes Dr. Lara Phan's course
(122, 18, 18, NOW()),  -- Mai likes Dr. Emma Nguyen's finance course
(123, 18, 18, NOW()),  -- Lisa likes Dr. Martin Weiss (health)
(124, 18, 19, NOW()),  -- Hiro likes Dr. Alice Tan (inner)
(125, 19, 20, NOW()),  -- Sophie likes Dr. Daniel Baker (wellbeing)
(126, 17, 21, NOW()),  -- Olivia likes Dr. Zoltan Farkas (inner)
(127, 17, 22, NOW()),  -- Ben likes Dr. Julia Smith (admin coach)
(128, 17, 23, NOW()),  -- Hung also likes Dr. Lara Phan
(129, 19, 24, NOW());  -- Emily likes Dr. Martin Weiss


-- ===============================================
-- 3️⃣ GROUP_CLASSES (expert-hosted community sessions)
-- ===============================================
INSERT INTO group_classes (expert_id, course_id, branch_id, group_name, max_students, start_time, end_time, created_at)
VALUES
(17, 17, 1, 'Mindfulness Morning Club', 50, NOW() + INTERVAL 1 DAY, NOW() + INTERVAL 1 DAY + INTERVAL 1 HOUR, NOW()),
(18, 18, 2, 'Healthy Life Circle', 40, NOW() + INTERVAL 2 DAY, NOW() + INTERVAL 2 DAY + INTERVAL 90 MINUTE, NOW()),
(19, 19, 3, 'Finance for Growth Workshop', 60, NOW() + INTERVAL 3 DAY, NOW() + INTERVAL 3 DAY + INTERVAL 2 HOUR, NOW()),
(20, 20, 1, 'Hungarian Mindfulness Practice', 30, NOW() + INTERVAL 4 DAY, NOW() + INTERVAL 4 DAY + INTERVAL 1 HOUR, NOW()),
(21, 21, 4, 'Leaders Transformation Forum', 80, NOW() + INTERVAL 5 DAY, NOW() + INTERVAL 5 DAY + INTERVAL 2 HOUR, NOW());

-- ===============================================
-- 4️⃣ GROUP_MEMBERS (participants joining group classes)
-- ===============================================
INSERT INTO group_members (group_id, user_id, joined_at)
VALUES
(1, 104, NOW()),
(1, 105, NOW()),
(2, 107, NOW()),
(2, 108, NOW()),
(3, 109, NOW()),
(3, 111, NOW()),
(4, 116, NOW()),
(4, 117, NOW()),
(5, 118, NOW()),
(5, 120, NOW());


-- 22.10.25 begin
SET SQL_SAFE_UPDATES = 0;

UPDATE courses
SET connect_link = CASE course_id
    WHEN 17 THEN 'https://meet.google.com/mindfulness-basics'
    WHEN 18 THEN 'https://zoom.us/healthy-mind-life'
    WHEN 19 THEN 'https://meet.google.com/meditation-focus'
    WHEN 20 THEN 'https://zoom.us/harmony-relationships'
    WHEN 21 THEN 'https://meet.google.com/finance-clarity'
    WHEN 22 THEN 'https://zoom.us/work-life-reset'
    WHEN 23 THEN 'https://meet.google.com/silence-awareness'
    WHEN 24 THEN 'https://zoom.us/global-strategy-growth'
    ELSE 'https://zoom.us/healthy-mind-life'
END;

SET SQL_SAFE_UPDATES = 1;
-- end

-- update course - link zoom for inner branch - 27.10.2025
SET SQL_SAFE_UPDATES = 0;
UPDATE courses
SET connect_link = CASE
	WHEN domain = 'inner' AND language = 'Vietnamese' THEN 'https://us06web.zoom.us/j/883605381210?pwd=LRQyIkliTvXPmj16HltaJiKPkCK062.1'
	ELSE connect_link
END;
SET SQL_SAFE_UPDATES = 1;




select * from favorites; -- need informations --
select * from feedback; -- need informations --
select * from group_classes; 
select * from group_members; 
describe analytics;
select * from analytics;
select * from bookings; 
select * from branches order by branch_name;	
select * from countries;
select * from courses order by domain asc;
select * from invitations; -- need informations --
select * from users; #where role = 'expert' order by full_name asc;
select * from experts;

-- view for feedback 
-- view for favourites courses
-- view for favourites experts
-- view for the most participant in a country
-- store procedure

delete from countries
where country_id > 7;
SELECT * FROM countries WHERE country_id > 7;

