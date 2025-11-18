USE living_library_manage_system;
SET FOREIGN_KEY_CHECKS = 0;
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

select * from branches;
-- quick global fix of the garbled em dash
UPDATE branches
SET description = REPLACE(description, 'â€”', '—')
WHERE country_id = 2;


INSERT INTO branches (country_id, branch_name, description)
VALUES
(3, 'inner',  'Trí Tuệ — cho trí tuệ cảm xúc, nhận thức và sự cân bằng.'),
(3, 'health', 'Sức khỏe thể chất và tinh thần — cho cơ thể, tâm trí và sự khỏe mạnh toàn diện.'),
(3, 'social', 'Mối quan hệ xã hội và gia đình — cho sự đồng cảm, giao tiếp và kết nối.'),
(3, 'finance', 'Trao quyền tài chính và sự nghiệp — cho sự sung túc, ổn định và mục đích.');
update branches
set description = replace(description, 'â€”', '—')
where country_id= 3;

INSERT INTO branches (country_id, branch_name, description)
VALUES
(6, 'inner', 'Inner Self & Mindfulness — for emotional intelligence, awareness, and balance.'),
(6, 'health', 'Physical and Mental Health — for body, mind, and holistic wellbeing.'),
(6, 'social', 'Social and Family Relationship — for empathy, communication, and connection.'),
(6, 'finance', 'Finance and Career Empowerment — for abundance, stability, and purpose.');
update branches
set description = replace(description, 'â€”', '—')
where country_id= 6;

select * from branches;

describe branches;
-- =======================================================
-- 3. Insert 25 users (17 participants, 8 experts)
-- =======================================================
select * from users;
describe users;
INSERT INTO users (full_name, email, password_hash, role, country_id, branch_id, language)
VALUES
-- 🇩🇪 Germany
('Anja Nguyen', 'anja.nguyen@gmail.com', 'hash26', 'participant', 2, 1, 'German'),
('Linh Becker', 'linh.becker@gmail.com', 'hash27', 'participant', 2, 2, 'German'),
('Minh Müller', 'minh.mueller@gmail.com', 'hash28', 'participant', 2, 3, 'German'),
('Thao Schmidt', 'thao.schmidt@gmail.com', 'hash29', 'participant', 2, 4, 'German'),
('Hoa Bauer', 'hoa.bauer@gmail.com', 'hash30', 'participant', 2, 1, 'German'),
('Khanh Schneider', 'khanh.schneider@gmail.com', 'hash31', 'participant', 2, 2, 'German'),
('Trang Wagner', 'trang.wagner@gmail.com', 'hash32', 'participant', 2, 3, 'German'),
('Huy Braun', 'huy.braun@gmail.com', 'hash33', 'participant', 2, 4, 'German'),
('Linh Koch', 'linh.koch@gmail.com', 'hash34', 'participant', 2, 1, 'German'),
('Hanh Hofmann', 'hanh.hofmann@gmail.com', 'hash35', 'participant', 2, 2, 'German'),


-- 🇻🇳 Vietnam
('Ngọc Bích Trần', 'ngocbich.tran@gmail.com', 'hash36', 'participant', 3, 1, 'Vietnamese'),
('Thanh Tâm Lê', 'thanhtam.le@gmail.com', 'hash37', 'participant', 3, 2, 'Vietnamese'),
('Hoàng Duy Phạm', 'hoangduy.pham@gmail.com', 'hash38', 'participant', 3, 3, 'Vietnamese'),
('Kim Oanh Nguyễn', 'kimoanh.nguyen@gmail.com', 'hash39', 'participant', 3, 4, 'Vietnamese'),
('Bảo Trâm Đỗ', 'baotram.do@gmail.com', 'hash40', 'participant', 3, 1, 'Vietnamese'),
('Vân Anh Phan', 'vananh.phan@gmail.com', 'hash41', 'participant', 3, 2, 'Vietnamese'),
('Minh Khang Đặng', 'minhkhang.dang@gmail.com', 'hash42', 'participant', 3, 3, 'Vietnamese'),
('Ngọc Hân Lâm', 'ngochan.lam@gmail.com', 'hash43', 'participant', 3, 4, 'Vietnamese'),
('Nhật Hào Vũ', 'nhathao.vu@gmail.com', 'hash44', 'participant', 3, 1, 'Vietnamese'),
('Thuỷ Tiên Dương', 'thuytien.duong@gmail.com', 'hash45', 'participant', 3, 2, 'Vietnamese'),
('Tường Vy Hồ', 'tuongvy.ho@gmail.com', 'hash46', 'participant', 3, 3, 'Vietnamese'),
('Phương Nhi Trịnh', 'phuongnhi.trinh@gmail.com', 'hash47', 'participant', 3, 4, 'Vietnamese'),
('Quang Minh Lưu', 'quangminh.luu@gmail.com', 'hash48', 'participant', 3, 1, 'Vietnamese'),
('Hồng Hạnh Vương', 'honghanh.vuong@gmail.com', 'hash49', 'participant', 3, 2, 'Vietnamese'),
('Gia Huy Đỗ', 'giahuy.do@gmail.com', 'hash50', 'participant', 3, 3, 'Vietnamese'),


-- 🇯🇵 Japan
('Akira Nguyen', 'akira.nguyen@gmail.com', 'hash51', 'participant', 4, 1, 'Japanese'),
('Mai Tanaka', 'mai.tanaka@gmail.com', 'hash52', 'participant', 4, 2, 'Japanese'),
('Haru Pham', 'haru.pham@gmail.com', 'hash53', 'participant', 4, 3, 'Japanese'),
('Sakura Tran', 'sakura.tran@gmail.com', 'hash54', 'participant', 4, 4, 'Japanese'),
('Ren Do', 'ren.do@gmail.com', 'hash55', 'participant', 4, 1, 'Japanese'),
('Aiko Le', 'aiko.le@gmail.com', 'hash56', 'participant', 4, 2, 'Japanese'),
('Tomo Phan', 'tomo.phan@gmail.com', 'hash57', 'participant', 4, 3, 'Japanese'),
('Yuki Dang', 'yuki.dang@gmail.com', 'hash58', 'participant', 4, 4, 'Japanese'),
('Sora Nguyen', 'sora.nguyen@gmail.com', 'hash59', 'participant', 4, 1, 'Japanese'),
('Emi Tran', 'emi.tran@gmail.com', 'hash60', 'participant', 4, 2, 'Japanese'),

-- 🇦🇺 Australia
('Linh Anh Pham', 'linhanh.pham@gmail.com', 'hash61', 'participant', 1, 1, 'English'),
('Bao Chau Nguyen', 'baochau.nguyen@gmail.com', 'hash62', 'participant', 1, 2, 'English'),
('Huy Tran', 'huy.tran@gmail.com', 'hash63', 'participant', 1, 3, 'English'),
('My Duyen Le', 'myduyen.le@gmail.com', 'hash64', 'participant', 1, 4, 'English'),
('Van Anh Dang', 'vananh.dang@gmail.com', 'hash65', 'participant', 1, 1, 'English'),
('Ngoc Linh Vu', 'ngoclinh.vu@gmail.com', 'hash66', 'participant', 1, 2, 'English'),
('Thuy Duong Phan', 'thuyduong.phan@gmail.com', 'hash67', 'participant', 1, 3, 'English'),
('Minh Trang Do', 'minhtrang.do@gmail.com', 'hash68', 'participant', 1, 4, 'English'),
('Bao Nhi Nguyen', 'baonhi.nguyen@gmail.com', 'hash69', 'participant', 1, 1, 'English'),
('Hoang Linh Pham', 'hoanglinh.pham@gmail.com', 'hash70', 'participant', 1, 2, 'English'),
('Thao Nguyen', 'thao.nguyen@gmail.com', 'hash71', 'participant', 1, 3, 'English'),
('Hieu Tran', 'hieu.tran@gmail.com', 'hash72', 'participant', 1, 4, 'English'),
('Tuan Le', 'tuan.le@gmail.com', 'hash73', 'participant', 1, 1, 'English'),
('Phuong Vo', 'phuong.vo@gmail.com', 'hash74', 'participant', 1, 2, 'English'), 

-- 8 Experts / Admins

-- 🇦🇺 Australia (country_id = 1)
('Dr. Phuong Le', 'phuong.le@gmail.com', 'hash26', 'expert', 1, 1, 'English'),
('Dr. Minh Tran', 'minh.tran@gmail.com', 'hash27', 'expert', 1, 2, 'English'),
('Dr. Huong Nguyen', 'huong.nguyen@gmail.com', 'hash28', 'expert', 1, 3, 'English'),
('Dr. Bao Dang', 'bao.dang@gmail.com', 'hash29', 'expert', 1, 4, 'English'),
('Dr. Linh Vo', 'linh.vo@gmail.com', 'hash30', 'expert', 1, 1, 'English'),
('Dr. Tuan Pham', 'tuan.pham@gmail.com', 'hash31', 'expert', 1, 2, 'English'),
('Dr. Quynh Ha', 'quynh.ha@gmail.com', 'hash32', 'expert', 1, 3, 'English') ,

-- 🇩🇪 Germany (country_id = 2)
('Dr. Lan Anh Nguyen', 'lananh.nguyen@gmail.com', 'hash33', 'expert', 2, 1, 'German'),
('Dr. Thanh Hoang', 'thanh.hoang@gmail.com', 'hash34', 'expert', 2, 2, 'German'),
('Dr. Kim Mai Le', 'kimmai.le@gmail.com', 'hash35', 'expert', 2, 3, 'German'),
('Dr. Duc Vo', 'duc.vo@gmail.com', 'hash36', 'expert', 2, 4, 'German'),
('Dr. Hoa Tran', 'hoa.tran@gmail.com', 'hash37', 'expert', 2, 1, 'German'),
('Dr. Son Nguyen', 'son.nguyen@gmail.com', 'hash38', 'expert', 2, 2, 'German'),
('Dr. Trang Do', 'trang.do@gmail.com', 'hash39', 'expert', 2, 3, 'German'),

-- 🇻🇳 Vietnam (country_id = 3)
('Dr. Hanh Pham', 'hanh.pham@gmail.com', 'hash40', 'expert', 3, 1, 'Vietnamese'),
('Dr. Khang Le', 'khang.le@gmail.com', 'hash41', 'expert', 3, 2, 'Vietnamese'),
('Dr. Nhi Nguyen', 'nhi.nguyen@gmail.com', 'hash42', 'expert', 3, 3, 'Vietnamese'),
('Dr. Quoc Tran', 'quoc.tran@gmail.com', 'hash43', 'expert', 3, 4, 'Vietnamese'),
('Dr. Thao Phan', 'thao.phan@gmail.com', 'hash44', 'expert', 3, 1, 'Vietnamese'),
('Dr. Tam Dang', 'tam.dang@gmail.com', 'hash45', 'expert', 3, 2, 'Vietnamese'),
('Dr. Vy Hoang', 'vy.hoang@gmail.com', 'hash46', 'expert', 3, 3, 'Vietnamese') ,

-- 🇯🇵 Japan (country_id = 4)
('Dr. Hana Nguyen', 'hana.nguyen@gmail.com', 'hash47', 'expert', 4, 1, 'Japanese'),
('Dr. Kenji Tran', 'kenji.tran@gmail.com', 'hash48', 'expert', 4, 2, 'Japanese'),
('Dr. Sora Vo', 'sora.vo@gmail.com', 'hash51', 'expert', 4, 1, 'Japanese'),
('Dr. Emi Nguyen', 'emi.nguyen@gmail.com', 'hash52', 'expert', 4, 2, 'Japanese'),
('Dr. Haru Le', 'haru.le@gmail.com', 'hash53', 'expert', 4, 3, 'Japanese'),

-- 🇫🇷 France (country_id = 5)
('Dr. Camille Nguyen', 'camille.nguyen@gmail.com', 'hash54', 'expert', 5, 1, 'French'),
('Dr. Lucie Tran', 'lucie.tran@gmail.com', 'hash55', 'expert', 5, 2, 'French'),
('Dr. Pierre Le', 'pierre.le@gmail.com', 'hash56', 'expert', 5, 3, 'French'),
('Dr. Chantal Pham', 'chantal.pham@gmail.com', 'hash57', 'expert', 5, 4, 'French'),
('Dr. Julien Do', 'julien.do@gmail.com', 'hash58', 'expert', 5, 1, 'French'),
('Dr. Elise Hoang', 'elise.hoang@gmail.com', 'hash59', 'expert', 5, 2, 'French'),
('Dr. Louis Nguyen', 'louis.nguyen@gmail.com', 'hash60', 'expert', 5, 3, 'French'),


-- 🇺🇸 America (country_id = 6)
('Dr. Sarah Phan', 'sarah.phan@gmail.com', 'hash61', 'expert', 6, 1, 'English'),
('Dr. Michael Tran', 'michael.tran@gmail.com', 'hash62', 'expert', 6, 2, 'English'),
('Dr. Emily Le', 'emily.le@gmail.com', 'hash63', 'expert', 6, 3, 'English'),
('Dr. Kevin Pham', 'kevin.pham@gmail.com', 'hash64', 'expert', 6, 4, 'English'),
('Dr. Jessica Nguyen', 'jessica.nguyen@gmail.com', 'hash65', 'expert', 6, 1, 'English'),
('Dr. David Hoang', 'david.hoang@gmail.com', 'hash66', 'expert', 6, 2, 'English'),
('Dr. Amy Tran', 'amy.tran@gmail.com', 'hash67', 'expert', 6, 3, 'English'),

-- 🇭🇺 Hungary (country_id = 7)
('Dr. An Nguyen', 'an.nguyen@gmail.com', 'hash68', 'expert', 7, 1, 'Hungarian'),
('Dr. Linh Do', 'linh.do@gmail.com', 'hash69', 'expert', 7, 2, 'Hungarian'),
('Dr. Tam Tran', 'tam.tran@gmail.com', 'hash70', 'expert', 7, 3, 'Hungarian'),
('Dr. Huong Le', 'huong.le@gmail.com', 'hash71', 'expert', 7, 4, 'Hungarian'),
('Dr. Quang Pham', 'quang.pham@gmail.com', 'hash72', 'expert', 7, 1, 'Hungarian'),
('Dr. Hoa Nguyen', 'hoa.nguyen@gmail.com', 'hash73', 'expert', 7, 2, 'Hungarian'),
('Dr. Thuy Vo', 'thuy.vo@gmail.com', 'hash74', 'expert', 7, 3, 'Hungarian');


select *  from users where role='expert' order by branch_id;
-- =======================================================
-- 4. Insert 8 experts
-- =======================================================
INSERT INTO experts 
(user_id, branch_id, specialization, bio, rating_avg, total_students, verified)
VALUES
-- 🌿 INNER BRANCH (Mindfulness & Emotional Growth)
(62, 1, 'inner', 'Certified meditation and mindfulness teacher specializing in emotional awareness.', 4.9, 150, TRUE),
(72, 1, 'inner', 'Life coach helping clients develop presence and inner calm.', 4.8, 120, TRUE),
(74, 1, 'inner', 'Therapist blending Eastern mindfulness with Western psychology.', 4.9, 140, TRUE),
(77, 1, 'inner', 'Energy healer guiding self-reflection and clarity through meditation.', 4.7, 100, TRUE),
(81, 1, 'inner', 'Expert in mindful living and emotional intelligence practices.', 4.8, 135, TRUE),

-- 💪 HEALTH BRANCH (Physical & Mental Wellness)
(89, 2, 'health', 'Wellness coach focusing on stress management and mental clarity.', 4.6, 90, TRUE),
(85, 2, 'health', 'Nutritionist guiding clients toward balanced, holistic diets.', 4.8, 130, TRUE),
(52, 2, 'health', 'Yoga and breathing specialist supporting healthy mind-body alignment.', 4.7, 110, TRUE),
(73, 2, 'health', 'Certified psychotherapist promoting sustainable self-care routines.', 4.9, 160, TRUE),
(78, 2, 'health', 'Health mentor integrating mindfulness and physical movement.', 4.8, 145, TRUE); #,
select * from users where role= 'expert';

INSERT INTO experts 
(user_id, branch_id, specialization, bio, rating_avg, total_students, verified)
VALUES
-- 💬 SOCIAL BRANCH (Relationships & Communication)
(97, 3, 'social', 'Family and relationship counselor focusing on empathy and communication.', 4.7, 125, TRUE),
(53, 3, 'social', 'Coach for emotional intelligence in leadership and teamwork.', 4.8, 140, TRUE),
(57, 3, 'social', 'Mediator helping families restore harmony and understanding.', 4.6, 100, TRUE),
(90, 3, 'social', 'Social psychologist specializing in connection and trust dynamics.', 4.9, 155, TRUE),
(60, 3, 'social', 'Relationship coach supporting cross-cultural understanding and growth.', 4.7, 115, TRUE),

-- 💰 FINANCE BRANCH (Career & Financial Growth)
(87, 4, 'finance', 'Career strategist empowering individuals to find purpose and prosperity.', 4.8, 140, TRUE),
(61, 4, 'finance', 'Financial planner teaching mindful money management and abundance.', 4.9, 160, TRUE),
(80, 4, 'finance', 'Entrepreneurship mentor guiding conscious business creation.', 4.7, 130, TRUE),
(94, 4, 'finance', 'Corporate trainer promoting financial literacy and ethical leadership.', 4.8, 145, TRUE),
(68, 4, 'finance', 'Investment and life coach inspiring confidence in long-term planning.', 4.9, 175, TRUE); #,


select user_id as expert from users where role='expert';
INSERT INTO experts 
(user_id, branch_id, specialization, bio, rating_avg, total_students, verified)
VALUES
(62, 1, 'inner', 'Mindfulness and emotional balance expert.', 4.8, 120, TRUE),
(89, 2, 'health', 'Holistic health coach and psychologist.', 4.7, 85, TRUE),
(72, 1, 'inner', 'Meditation mentor focusing on spiritual growth.', 4.9, 140, TRUE),
(97, 3, 'social', 'Family relationship consultant.', 4.5, 90, TRUE),
(68, 4, 'finance', 'Personal finance and career development mentor.', 4.8, 110, TRUE),
(85, 2, 'health', 'Mental health expert for work-life balance.', 4.6, 75, TRUE),
(77, 1, 'inner', 'Hungarian mindfulness practitioner and therapist.', 4.9, 60, TRUE),

(74, 1, 'inner', 'Mindfulness and emotional balance expert.', 4.8, 120, TRUE),
(52, 2, 'health', 'Holistic health coach and psychologist.', 4.7, 85, TRUE),
(81, 1, 'inner', 'Meditation mentor focusing on spiritual growth.', 4.9, 140, TRUE),
(90, 3, 'social', 'Family relationship consultant.', 4.5, 90, TRUE),
(87, 4, 'finance', 'Personal finance and career development mentor.', 4.8, 110, TRUE),
(73, 2, 'health', 'Mental health expert for work-life balance.', 4.6, 75, TRUE),
(72, 1, 'inner', 'Hungarian mindfulness practitioner and therapist.', 4.9, 60, TRUE);
select * from experts order by specialization asc;


-- =======================================================
-- 5. Insert 8 courses
-- =======================================================
INSERT INTO courses (expert_id, branch_id, title, domain, language, description, price, avg_rating, total_students)
VALUES
(45, 1, 'Mindfulness Basics', 'inner', 'Vietnamese', 'Hiểu mình hiểu người, Nhân sinh như ý.', 25.00, 4.8, 120),
(40, 2, 'Healthy Mind, Healthy Life', 'health', 'German', 'Prinzipien der integrativen Gesundheit.', 30.00, 4.7, 85),
(41, 1, 'Meditation for Focus', 'inner', 'Japanese', 'ガイド付き瞑想と呼吸法の練習。', 20.00, 4.9, 140),
(12, 3, 'Harmony in Relationships', 'social', 'French', "Améliorer la communication et l'empathie.", 28.00, 4.5, 90),
(36, 4, 'Financial Clarity', 'finance', 'Vietnamese', 'Hiểu Đại Vận, Thắng Đại Trận', 22.00, 4.8, 110),
(37, 2, 'Work-Life Reset', 'health', 'English', 'Stress management and mental balance.', 35.00, 4.6, 75),
(26, 1, 'Silence and Awareness', 'inner', 'Hungarian', 'Mindful presence practices.', 18.00, 4.9, 60),
(21, 4, 'Global Strategy & Growth', 'finance', 'English', 'Advanced career leadership program.', 40.00, 5.0, 300);
describe courses;

select * from experts order by specialization asc;
-- INSERT INNER
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(39, 1, 'Mindfulness for Beginners', 'inner', 'English',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-21 00:00:00', '2025-12-21 00:00:00', 24.00, 4.8, 120),

(38, 1, 'Deep Breathing Awareness', 'inner', 'Vietnamese',
 'A calming practice to connect breath and body awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.7, 100),

(32, 1, 'Silent Power of the Present Moment', 'inner', 'Japanese',
 'Discover peace through present-moment meditation.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-15 00:00:00', '2025-11-30 00:00:00', 26.00, 4.9, 130),

(34, 1, 'Inner Transformation & Self-Discovery', 'inner', 'English',
 'Learn to shift inner energy and find emotional clarity.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-30 00:00:00', '2025-12-20 00:00:00', 28.00, 4.8, 140),

(26, 1, 'Meditative Movement Flow', 'inner', 'French',
 'A mix of movement and stillness for balance and awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-25 00:00:00', '2025-12-05 00:00:00', 25.00, 4.6, 95),

(22, 1, 'Gratitude Practice & Joyful Living', 'inner', 'English',
 'Develop gratitude habits that lift your emotional state.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 00:00:00', '2025-12-21 00:00:00', 23.00, 4.7, 105),

(23, 1, 'Energy of Stillness', 'inner', 'German',
 'Learn how inner silence improves focus and creativity.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-12-05 00:00:00', 29.00, 4.9, 115),

(24, 1, 'Compassion & Mindful Relationships', 'inner', 'Vietnamese',
 'Apply mindfulness in emotional connection and empathy.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-11-30 00:00:00', 27.00, 4.8, 98),

(25, 1, 'Clarity Through Meditation', 'inner', 'Hungarian',
 'Build clarity and reduce stress through mindful breathing.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-27 00:00:00', '2025-12-21 00:00:00', 20.00, 4.9, 120),

(45, 1, 'The Path to Inner Freedom', 'inner', 'English',
 'Release limiting thoughts and reconnect with your essence.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-25 00:00:00', '2025-12-21 00:00:00', 32.00, 4.95, 150);


select * from experts order by specialization asc;
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(41, 1, 'Mindfulness for Beginners', 'inner', 'German',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 20:00:00', '2025-11-21 00:00:00', 24.00, 4.8, 120),
(39, 1, 'Mindfulness for Beginners', 'inner', 'Hungarian',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-21 20:00:00', '2025-11-21 0:00:00', 24.00, 4.8, 120);

select * from experts order by specialization asc;
-- INSERT 
INSERT INTO courses
  (expert_id, branch_id, title, domain, language, description, connect_link,
   begin_date,           end_date,             price, avg_rating, total_students)
VALUES
(30, 1, 'Mindfulness for Beginners', 'health', 'Vietnamese',
 'Start your mindfulness journey with simple, practical exercises.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-11-21 00:00:00', '2025-12-21 00:00:00', 24.00, 4.8, 120),

(29, 1, 'Deep Breathing Awareness', 'inner', 'Vietnamese',
 'A calming practice to connect breath and body awareness.',
 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1',
 '2025-10-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.7, 100),
 
-- 1️⃣ Mind–Body Harmony (German)
(31, 2, 'Mind–Body Harmony', 'health', 'German',
 'Discover how nutrition, movement, and meditation work together to restore your body–mind balance.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-20 20:00:00', '2025-11-23 00:00:00', 29.00, 4.8, 95),

-- 2️⃣ Resilience and Stress Detox (English)
(33, 2, 'Resilience and Stress Detox', 'health', 'English',
 'A practical workshop on building mental resilience and releasing stress through body awareness and breathwork.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-20 20:00:00', '2025-11-23 00:00:00', 32.00, 4.7, 120),

-- 3️⃣ Holistic Nutrition for Energy (German)
(37, 2, 'Holistic Nutrition for Energy', 'health', 'German',
 'Learn to optimize daily vitality through integrative nutrition habits supported by mindfulness practice.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-10-23 10:00:00', '2025-11-23 00:00:00', 27.00, 4.9, 110),

-- 4️⃣ Emotional Wellbeing in Motion (English)
(40, 2, 'Emotional Wellbeing in Motion', 'health', 'English',
 'Explore movement and breathing sequences designed to free emotional tension and improve vitality.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-11-10 17:00:00', '2025-12-10 00:00:00', 30.00, 4.6, 105),

-- 5️⃣ Sleep, Breath, and Inner Calm (German)
(44, 2, 'Sleep, Breath, and Inner Calm', 'health', 'German',
 'Techniques for better sleep quality and stress release through mindful breathing and restorative rest.',
 'http://link.wit.edu.vn/ttlkn',
 '2025-11-15 21:00:00', '2025-12-15 00:00:00', 26.00, 4.9, 98);

select * from experts order by specialization asc;
-- INSERT SOCIAL
INSERT INTO courses 
(expert_id, branch_id, title, domain, language, description, connect_link, 
 begin_date, end_date, price, avg_rating, total_students)
VALUES
(12, 3, "L'harmonie dans les relations", 'social', 'French',
"L'empathie et une compréhension plus profonde pour créer des relations harmonieuses en famille et au travail.",
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-27 18:00:00', '2025-11-27 00:00:00', 25.00, 4.8, 110),

(35, 3, 'Communication authentique', 'social', 'French',
 'Apprenez la communication non violente pour exprimer clairement vos besoins et écouter avec ouverture.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-11-05 19:00:00', '2025-12-05 00:00:00', 27.00, 4.9, 125),

(16, 3, 'Building Trust in Teams', 'social', 'English',
 'Practical framework to strengthen collaboration and build trust in professional and family teams.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-20 18:30:00', '2025-12-10 00:00:00', 26.00, 4.7, 100),

(15, 3, 'Du conflit à la connexion dans la communauté', 'social', 'French',
 "Transformer les conflits en opportunités de croissance mutuelle grâce à l'écoute active et à l'intelligence émotionnelle.",
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-10-28 17:30:00', '2025-12-12 00:00:00', 29.00, 4.9, 115),

(42, 3, "L'art de l'intelligence sociale", 'social', 'French',
 'Développez votre conscience sociale et votre empathie pour construire des relations épanouissantes entre les cultures.',
 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1',
 '2025-11-16 20:00:00', '2025-12-16 00:00:00', 30.00, 4.8, 140),

-- 🌿 INNER BRANCH (1–13)
(25, 1, 'Mindfulness for Beginners', 'inner', 'English', 'Start your mindfulness journey with simple, practical exercises.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-21 00:00:00', '2025-12-21 00:00:00', 24.00, 4.8, 120),
(24, 1, 'Deep Breathing Awareness', 'inner', 'Vietnamese', 'A calming practice to connect breath and body awareness.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-10-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.7, 100),
(23, 1, 'Inner Peace Reset', 'inner', 'German', 'A guided self-reflection course to balance emotions and clarity.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-10 00:00:00', '2025-12-10 00:00:00', 25.00, 4.9, 140),
(22, 1, 'Gratitude Every Morning', 'inner', 'French', 'Simple daily rituals to start your day with gratitude and energy.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-05 00:00:00', '2025-12-05 00:00:00', 19.00, 4.8, 110),
(26, 1, 'Silent Mind, Clear Heart', 'inner', 'Japanese', 'Embrace silence as a source of wisdom and deep self-connection.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-18 00:00:00', '2025-12-18 00:00:00', 27.00, 4.9, 95),
(34, 1, 'Journey to Inner Clarity', 'inner', 'Hungarian', 'Learn to calm your thoughts and reconnect with your purpose.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-07 00:00:00', '2025-12-07 00:00:00', 23.00, 4.7, 130),
(32, 1, 'Meditation for Stress Relief', 'inner', 'English', 'Techniques to reduce stress and find inner harmony.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-09 00:00:00', '2025-12-09 00:00:00', 26.00, 4.8, 115),
(38, 1, 'Love and Mind Awareness', 'inner', 'Vietnamese', 'Reconnect with your inner source of love through guided awareness.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-15 00:00:00', '2025-12-15 00:00:00', 28.00, 4.9, 125),
(34, 1, 'Mindful Walking Practice', 'inner', 'German', 'Integrate mindfulness into your daily walks and routines.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-11 00:00:00', '2025-12-11 00:00:00', 21.00, 4.7, 98),
(38, 1, 'Focus & Flow', 'inner', 'English', 'A structured method to enhance focus through meditation and journaling.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-22 00:00:00', '2025-12-22 00:00:00', 32.00, 4.9, 200),
(41, 1, 'Inner Joy Awakening', 'inner', 'French', 'Reconnect to joy through mindful movement and laughter therapy.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-13 00:00:00', '2025-12-13 00:00:00', 29.00, 4.8, 105),
(41, 1, 'Awareness in Everyday Life', 'inner', 'English', 'Learn to turn ordinary moments into mindful experiences.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-26 00:00:00', '2025-12-26 00:00:00', 25.00, 4.9, 145),
(45, 1, 'Stillness and Insight', 'inner', 'Japanese', 'Find insight through guided stillness and mindful observation.', 'https://us06web.zoom.us/j/84409856171?pwd=n6ZNBGPGbJU6EU1NFGnNzuxvXb715h.1', '2025-11-30 00:00:00', '2026-01-05 00:00:00', 33.00, 5.0, 180),

-- 💪 HEALTH BRANCH (14–25)
(30, 2, 'Healthy Mind, Healthy Body', 'health', 'English', 'Holistic approaches to boost both mental and physical health.', 'http://link.wit.edu.vn/ttlkn', '2025-11-02 00:00:00', '2025-12-02 00:00:00', 28.00, 4.8, 160),
(29, 2, 'Work-Life Reset', 'health', 'German', 'Tools to restore balance between work and well-being.', 'http://link.wit.edu.vn/ttlkn', '2025-11-05 00:00:00', '2025-12-05 00:00:00', 30.00, 4.7, 150),
(31, 2, 'Nutrition & Mindfulness', 'health', 'French', 'Learn mindful eating and awareness-based nutrition habits.', 'http://link.wit.edu.vn/ttlkn', '2025-11-06 00:00:00', '2025-12-06 00:00:00', 26.00, 4.9, 140),
(33, 2, 'Healing Through Movement', 'health', 'Vietnamese', 'Gentle exercises to release emotional tension and increase vitality.', 'http://link.wit.edu.vn/ttlkn', '2025-11-08 00:00:00', '2025-12-08 00:00:00', 20.00, 4.8, 130),
(37, 2, 'Energy Renewal Practices', 'health', 'English', 'Daily physical practices to revitalize energy flow.', 'http://link.wit.edu.vn/ttlkn', '2025-11-09 00:00:00', '2025-12-09 00:00:00', 27.00, 4.7, 155),
(40, 2, 'Detox Your Life', 'health', 'Vietnamese', 'Cleansing habits to reset mind, body, and space.', 'http://link.wit.edu.vn/ttlkn', '2025-11-10 00:00:00', '2025-12-10 00:00:00', 22.00, 4.8, 120),
(44, 2, 'Emotional Fitness', 'health', 'German', 'Train emotional resilience for daily challenges.', 'http://link.wit.edu.vn/ttlkn', '2025-11-11 00:00:00', '2025-12-11 00:00:00', 29.00, 4.9, 210),
(28, 2, 'Yoga for Clarity', 'health', 'French', 'Breath, flow, and posture for balance and clarity.', 'http://link.wit.edu.vn/ttlkn', '2025-11-12 00:00:00', '2025-12-12 00:00:00', 24.00, 4.7, 100),
(27, 2, 'Rest & Recovery Workshop', 'health', 'English', 'Science-backed rest techniques for high-performance recovery.', 'http://link.wit.edu.vn/ttlkn', '2025-11-13 00:00:00', '2025-12-13 00:00:00', 32.00, 4.9, 175),
(44, 2, 'Healing Foods & Habits', 'health', 'Vietnamese', 'Learn about healing foods, herbs, and mindful cooking.', 'http://link.wit.edu.vn/ttlkn', '2025-11-14 00:00:00', '2025-12-14 00:00:00', 20.00, 4.8, 125),
(44, 2, 'Mindful Body Awareness', 'health', 'English', 'Reconnect with body wisdom through awareness and movement.', 'http://link.wit.edu.vn/ttlkn', '2025-11-15 00:00:00', '2025-12-15 00:00:00', 28.00, 4.9, 190),
(28,2, 'Holistic Health Habits', 'health', 'German', 'Practical ways to maintain health through mindful living.', 'http://link.wit.edu.vn/ttlkn', '2025-11-16 00:00:00', '2025-12-16 00:00:00', 27.00, 4.7, 110),

-- 💬 SOCIAL BRANCH (26–37)
(12, 3, 'Harmony in Relationships', 'social', 'French', 'Learn deep listening and empathy in family communication.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-01 00:00:00', '2025-12-01 00:00:00', 29.00, 4.8, 135),
(35, 3, 'Empathy and Connection', 'social', 'English', 'Develop empathy skills for meaningful human connections.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-03 00:00:00', '2025-12-03 00:00:00', 27.00, 4.9, 210),
(16, 3, 'Parent-Child Harmony', 'social', 'Vietnamese', 'Strengthen family bonds with mindful parenting.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-06 00:00:00', '2025-12-06 00:00:00', 25.00, 4.8, 150),
(15, 3, 'Emotional Intelligence 101', 'social', 'German', 'Understand and manage emotions in relationships effectively.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-09 00:00:00', '2025-12-09 00:00:00', 24.00, 4.7, 120),
(42, 3, 'Social Confidence Mastery', 'social', 'English', 'Boost self-esteem and confidence in communication.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-01 00:00:00', '2025-12-10 00:00:00', 30.00, 4.8, 180),
(14, 3, 'Cultural Connection Lab', 'social', 'French', 'Intercultural communication skills for global collaboration.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-01 00:00:00', '2025-12-11 00:00:00', 26.00, 4.9, 140),
(13, 3, 'Family Peace Circle', 'social', 'Vietnamese', 'Tools for peaceful conflict resolution at home.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-02 00:00:00', '2025-12-12 00:00:00', 28.00, 4.7, 170),
(12, 3, 'Relationship Healing Workshop', 'social', 'German', 'Rebuild trust and heal from emotional wounds.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-14 00:00:00', '2025-12-14 00:00:00', 32.00, 4.8, 160),
(35, 3, 'Communication Without Judgment', 'social', 'English', 'Nonviolent communication skills for real understanding.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-15 00:00:00', '2025-12-15 00:00:00', 33.00, 4.9, 220),
(16, 3, 'Teamwork & Trust', 'social', 'French', 'How to cultivate trust and cooperation in teams.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-16 00:00:00', '2025-12-16 00:00:00', 25.00, 4.7, 130),
(15, 3, 'Art of Listening', 'social', 'Vietnamese', 'Learn to listen deeply and build emotional safety in conversations.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-18 00:00:00', '2025-12-18 00:00:00', 19.00, 4.9, 145),
(42, 3, 'Friendship & Boundaries', 'social', 'English', 'Learn how to maintain healthy relationships with empathy and respect.', 'https://us06web.zoom.us/j/89995888930?pwd=CTkjr7qGpWzGXfUwrRwMsr5xYmqQgD.1', '2025-11-20 00:00:00', '2025-12-20 00:00:00', 28.00, 4.8, 160),

-- 💰 FINANCE BRANCH (38–50)
(21, 4, 'Financial Clarity 101', 'finance', 'Vietnamese', 'Understand your money mindset and build a stable foundation.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-01 00:00:00', '2025-12-01 00:00:00', 22.00, 4.8, 150),
(20, 4, 'Career Path Reboot', 'finance', 'English', 'Strategic tools to reimagine your career growth.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-05 00:00:00', '2025-12-05 00:00:00', 29.00, 4.9, 175),
(36, 4, 'Mindful Money Habits', 'finance', 'German', 'Learn the emotional side of money and smart budgeting.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-07 00:00:00', '2025-12-07 00:00:00', 27.00, 4.7, 190),
(19, 4, 'Investing for Beginners', 'finance', 'English', 'Simple guide to start investing with confidence.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-08 00:00:00', '2025-12-08 00:00:00', 33.00, 4.8, 210),
(18, 4, 'Wealth with Purpose', 'finance', 'French', 'Learn to align your finances with personal values and purpose.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-10 00:00:00', '2025-12-10 00:00:00', 35.00, 4.9, 250),
(17, 4, 'Entrepreneurial Mindset', 'finance', 'English', 'Transform your ideas into profitable ventures.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-12 00:00:00', '2025-12-12 00:00:00', 30.00, 4.7, 180),
(43, 4, 'Smart Savings Strategy', 'finance', 'Vietnamese', 'Practical saving systems for long-term financial success.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-14 00:00:00', '2025-12-14 00:00:00', 21.00, 4.9, 140),
(21, 4, 'Leadership & Influence', 'finance', 'German', 'How to lead with empathy and financial clarity.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-16 00:00:00', '2025-12-16 00:00:00', 36.00, 4.8, 200),
(20, 4, 'Digital Economy 2025', 'finance', 'English', 'Understand trends in digital finance and remote business.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-18 00:00:00', '2025-12-18 00:00:00', 38.00, 4.9, 230),
(36, 4, 'Global Trade Simplified', 'finance', 'French', 'Essentials for international trade and export businesses.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-20 00:00:00', '2025-12-20 00:00:00', 31.00, 4.8, 150),
(19, 4, 'Financial Healing & Abundance', 'finance', 'Vietnamese', 'Transform financial blocks into abundance mindset.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-21 00:00:00', '2025-12-21 00:00:00', 28.00, 4.9, 185),
(18, 4, 'Future Leaders Program', 'finance', 'English', 'Learn modern leadership and business ethics for success.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-23 00:00:00', '2025-12-23 00:00:00', 40.00, 5.0, 240),
(17, 4, 'Women & Wealth', 'finance', 'French', 'Empower women to manage and grow their wealth independently.', 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1', '2025-11-25 00:00:00', '2025-12-25 00:00:00', 29.00, 4.8, 170);

select * from experts order by specialization asc;


INSERT INTO courses 
(expert_id, branch_id, title, domain, language, description, connect_link, 
 begin_date, end_date, price, avg_rating, total_students)
VALUES
(21, 4, 'Tự Do Tài Chính', 'finance', 'Vietnamese',
 'Học các kỹ năng lập ngân sách, tiết kiệm và đầu tư cốt lõi để tạo ra sự tự do tài chính bền vững.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-03 18:00:00', '2025-12-03 00:00:00', 32.00, 4.8, 150),

(20, 4, 'Leadership and Money Mindset', 'finance', 'English',
 'Explore the psychology of abundance and develop leadership principles to grow your financial vision.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-06 19:30:00', '2025-12-06 00:00:00', 36.00, 4.9, 180),

(36, 4, 'Phụ nữ và Sự Giàu có', 'finance', 'Vietnamese',
 'Lớp học chuyên sâu giúp phụ nữ quản lý tiền bạc một cách khôn ngoan và lập kế hoạch bảo đảm an ninh lâu dài.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-09 20:00:00', '2025-12-09 00:00:00', 28.00, 4.7, 130),

(19, 4, 'Career Growth through Smart Finance', 'finance', 'English',
 'Understand how financial planning enhances career choices and business growth.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-12 18:30:00', '2025-12-12 00:00:00', 30.00, 4.8, 170),

(17, 4, 'Thịnh vượng toàn diện', 'finance', 'Vietnamese',
 'Một cách tiếp cận lấy trái tim làm trọng tâm để cân bằng sự giàu có, hạnh phúc và mục đích trong cuộc sống hiện đại.',
 'https://us06web.zoom.us/j/3939796789?pwd=QoDyjH0cm1MwbcVluv5JFNH5O0JRbb.1',
 '2025-11-15 19:00:00', '2025-12-15 00:00:00', 34.00, 4.9, 160);


-- =======================================================
-- 6. Insert 8 bookings
-- =======================================================
-- Random booking examples between participants and experts
describe bookings;
ALTER TABLE bookings 
MODIFY COLUMN user_id INT NULL;
select * from courses;
select * from experts;
INSERT INTO bookings (course_id, expert_id, scheduled_time, status)
VALUES
(15, 12, NOW() + INTERVAL 1 DAY, 'booked'),
(16, 13, NOW() + INTERVAL 2 DAY, 'completed'),
(17, 14, NOW() + INTERVAL 3 DAY, 'booked'),
(18, 15, NOW() + INTERVAL 4 DAY, 'booked'),
(19, 16, NOW() + INTERVAL 5 DAY, 'completed'),
(20, 17, NOW() + INTERVAL 6 DAY, 'booked'),
(21, 18, NOW() + INTERVAL 7 DAY, 'cancelled'),
(22, 19, NOW() + INTERVAL 8 DAY, 'booked'),
(23, 20, NOW() + INTERVAL 9 DAY, 'completed'),
(24, 21, NOW() + INTERVAL 10 DAY, 'booked'),

(25, 22, NOW() + INTERVAL 1 HOUR, 'booked'),
(26, 23, NOW() + INTERVAL 2 HOUR, 'completed'),
(27, 24, NOW() + INTERVAL 3 HOUR, 'booked'),
(28, 25, NOW() + INTERVAL 4 HOUR, 'booked'),
(29, 26, NOW() + INTERVAL 5 HOUR, 'cancelled'),
(30, 27, NOW() + INTERVAL 6 HOUR, 'booked'),
(31, 28, NOW() + INTERVAL 7 HOUR, 'completed'),
(32, 29, NOW() + INTERVAL 8 HOUR, 'booked'),
(33, 30, NOW() + INTERVAL 9 HOUR, 'completed'),
(34, 31, NOW() + INTERVAL 10 HOUR, 'booked'),

(35, 32, NOW() + INTERVAL 1 DAY, 'booked'),
(36, 33, NOW() + INTERVAL 2 DAY, 'booked'),
(37, 34, NOW() + INTERVAL 3 DAY, 'completed'),
(38, 35, NOW() + INTERVAL 4 DAY, 'booked'),
(39, 36, NOW() + INTERVAL 5 DAY, 'booked'),
(40, 37, NOW() + INTERVAL 6 DAY, 'cancelled'),
(41, 38, NOW() + INTERVAL 7 DAY, 'booked'),
(42, 39, NOW() + INTERVAL 8 DAY, 'completed'),
(43, 40, NOW() + INTERVAL 9 DAY, 'booked'),
(44, 41, NOW() + INTERVAL 10 DAY, 'booked'),

(45, 42, NOW() + INTERVAL 1 DAY, 'completed'),
(46, 43, NOW() + INTERVAL 2 DAY, 'booked'),
(47, 44, NOW() + INTERVAL 3 DAY, 'booked'),
(48, 45, NOW() + INTERVAL 4 DAY, 'booked'),
(49, 12, NOW() + INTERVAL 5 DAY, 'cancelled'),
(50, 13, NOW() + INTERVAL 6 DAY, 'booked'),
(51, 14, NOW() + INTERVAL 7 DAY, 'completed'),
(52, 15, NOW() + INTERVAL 8 DAY, 'booked'),
(53, 16, NOW() + INTERVAL 9 DAY, 'booked'),
(54, 17, NOW() + INTERVAL 10 DAY, 'completed'),

(55, 18, NOW() + INTERVAL 1 DAY, 'booked'),
(56, 19, NOW() + INTERVAL 2 DAY, 'booked'),
(57, 20, NOW() + INTERVAL 3 DAY, 'completed'),
(58, 21, NOW() + INTERVAL 4 DAY, 'booked'),
(59, 22, NOW() + INTERVAL 5 DAY, 'cancelled'),
(60, 23, NOW() + INTERVAL 6 DAY, 'booked'),
(61, 24, NOW() + INTERVAL 7 DAY, 'booked'),
(62, 25, NOW() + INTERVAL 8 DAY, 'completed'),
(63, 26, NOW() + INTERVAL 9 DAY, 'booked'),
(64, 27, NOW() + INTERVAL 10 DAY, 'booked'),

(65, 28, NOW() + INTERVAL 1 DAY, 'booked'),
(66, 29, NOW() + INTERVAL 2 DAY, 'completed'),
(67, 30, NOW() + INTERVAL 3 DAY, 'booked'),
(68, 31, NOW() + INTERVAL 4 DAY, 'booked'),
(69, 32, NOW() + INTERVAL 5 DAY, 'completed'),
(70, 33, NOW() + INTERVAL 6 DAY, 'booked'),
(71, 34, NOW() + INTERVAL 7 DAY, 'booked'),
(72, 35, NOW() + INTERVAL 8 DAY, 'booked'),
(73, 36, NOW() + INTERVAL 9 DAY, 'cancelled'),
(74, 37, NOW() + INTERVAL 10 DAY, 'booked'),

(75, 38, NOW() + INTERVAL 1 DAY, 'booked'),
(76, 39, NOW() + INTERVAL 2 DAY, 'completed'),
(77, 40, NOW() + INTERVAL 3 DAY, 'booked'),
(78, 41, NOW() + INTERVAL 4 DAY, 'booked'),
(79, 42, NOW() + INTERVAL 5 DAY, 'completed'),
(80, 43, NOW() + INTERVAL 6 DAY, 'booked'),
(81, 44, NOW() + INTERVAL 7 DAY, 'cancelled'),
(82, 45, NOW() + INTERVAL 8 DAY, 'booked'),
(83, 12, NOW() + INTERVAL 9 DAY, 'booked'),
(84, 13, NOW() + INTERVAL 10 DAY, 'completed');


select * from countries;
-- =======================================================
-- 7. Insert 4 analytics
-- =======================================================
INSERT INTO analytics (metric_type, reference_id, metric_value, country_id, branch_id)
VALUES
('student_count', 1, 120, 3, 1),
('expert_count', 1, 8, 3, 1),
('course_popularity', 5, 110, 3, 4),
('rating_avg', 1, 4.8, 3, 1);

select * from users where role='expert';
-- ===============================================
-- 1️⃣ FAVORITES (users marking experts/courses they like)
-- ===============================================
INSERT INTO favorites (user_id, expert_id, course_id, created_at)
VALUES
(51, 15, 12, NOW()),   -- User 51 likes Dr. Lara Phan’s course
(52, 16, 18, NOW()),   -- User 52 likes Dr. Martin Weiss’ course
(53, 17, 22, NOW()),   -- User 53 likes Dr. Alice Tan’s course
(54, 18, 25, NOW()),   -- User 54 likes Dr. Jean Rousseau’s course
(55, 19, 28, NOW()),   -- User 55 likes Dr. Emma Nguyen’s course
(56, 20, 30, NOW()),   -- User 56 likes Dr. Daniel Baker’s course
(57, 21, 31, NOW()),   -- User 57 likes Dr. Zoltan Farkas’s course
(58, 22, 33, NOW()),   -- User 58 likes Dr. Julia Smith’s course
(59, 23, 35, NOW()),   -- User 59 likes Dr. Hana Nguyen’s course
(60, 24, 38, NOW()),   -- User 60 likes Dr. Minh Tran’s course
(61, 25, 41, NOW()),   -- User 61 likes Dr. Quynh Ha’s course
(62, 26, 43, NOW()),   -- User 62 likes Dr. Tam Dang’s course
(63, 27, 45, NOW()),   -- User 63 likes Dr. Yumi Phan’s course
(64, 28, 47, NOW()),   -- User 64 likes Dr. Pierre Le’s course
(65, 29, 49, NOW()),   -- User 65 likes Dr. Sarah Phan’s course
(66, 30, 52, NOW()),   -- User 66 likes Dr. Kevin Pham’s course
(67, 31, 55, NOW()),   -- User 67 likes Dr. Amy Tran’s course
(68, 32, 59, NOW()),   -- User 68 likes Dr. Linh Do’s course
(69, 33, 63, NOW()),   -- User 69 likes Dr. Huong Le’s course
(70, 34, 65, NOW());   -- User 70 likes Dr. Quang Pham’s course


-- ===============================================
-- 3️⃣ GROUP_CLASSES (expert-hosted community sessions)
-- ===============================================
INSERT INTO group_classes (expert_id, course_id, branch_id, group_name, max_students, start_time, end_time, created_at)
VALUES
(12, 15, 1, '🌿 Mindfulness Morning Circle', 50, NOW() + INTERVAL 1 DAY, NOW() + INTERVAL 1 DAY + INTERVAL 1 HOUR, NOW()),
(13, 18, 1, '🌸 Inner Peace Practice Group', 45, NOW() + INTERVAL 2 DAY, NOW() + INTERVAL 2 DAY + INTERVAL 90 MINUTE, NOW()),
(14, 22, 2, '💪 Healthy Life Circle', 60, NOW() + INTERVAL 3 DAY, NOW() + INTERVAL 3 DAY + INTERVAL 2 HOUR, NOW()),
(15, 24, 3, '💬 Family Harmony Workshop', 40, NOW() + INTERVAL 4 DAY, NOW() + INTERVAL 4 DAY + INTERVAL 2 HOUR, NOW()),
(16, 26, 4, '💰 Financial Freedom Club', 70, NOW() + INTERVAL 5 DAY, NOW() + INTERVAL 1 DAY + INTERVAL 2 HOUR, NOW()),
(17, 31, 2, '🧘 Mind-Body Reset Session', 55, NOW() + INTERVAL 6 DAY, NOW() + INTERVAL 2 DAY + INTERVAL 90 MINUTE, NOW()),
(18, 33, 2, '🌿 Healing & Energy Renewal', 50, NOW() + INTERVAL 7 DAY, NOW() + INTERVAL 3 DAY + INTERVAL 90 MINUTE, NOW()),
(19, 36, 3, '💬 Conscious Communication Lab', 65, NOW() + INTERVAL 8 DAY, NOW() + INTERVAL 4 DAY + INTERVAL 2 HOUR, NOW()),
(20, 38, 3, '💞 Trust & Connection Space', 40, NOW() + INTERVAL 9 DAY, NOW() + INTERVAL 1 DAY + INTERVAL 2 HOUR, NOW()),
(21, 41, 1, '🌅 Awakening Awareness', 80, NOW() + INTERVAL 10 DAY, NOW() + INTERVAL 2 DAY + INTERVAL 2 HOUR, NOW()),
(22, 45, 1, '🪷 Meditation & Stillness Group', 50, NOW() + INTERVAL 11 DAY, NOW() + INTERVAL 3 DAY + INTERVAL 90 MINUTE, NOW()),
(23, 50, 1, '🌼 Mindful Living Community', 60, NOW() + INTERVAL 12 DAY, NOW() + INTERVAL 4 DAY + INTERVAL 2 HOUR, NOW()),
(24, 55, 2, '💚 Work-Life Balance Circle', 45, NOW() + INTERVAL 13 DAY, NOW() + INTERVAL 1 DAY + INTERVAL 90 MINUTE, NOW()),
(25, 66, 3, '🗣️ Empathy & Relationship Growth', 70, NOW() + INTERVAL 14 DAY, NOW() + INTERVAL 2 DAY + INTERVAL 2 HOUR, NOW()),
(26, 78, 4, '💎 Wealth & Purpose Masterclass', 90, NOW() + INTERVAL 15 DAY, NOW() + INTERVAL 3 DAY + INTERVAL 2 HOUR, NOW());


-- ===============================================
-- 4️⃣ GROUP_MEMBERS (participants joining group classes)
-- ===============================================
INSERT INTO group_members (group_id, user_id, joined_at)
VALUES
(1, 51, NOW()),   -- User 51 joins Mindfulness Morning Circle
(1, 52, NOW()),   -- User 52 joins Mindfulness Morning Circle
(2, 53, NOW()),   -- User 53 joins Inner Peace Practice Group
(2, 54, NOW()),   -- User 54 joins Inner Peace Practice Group
(3, 55, NOW()),   -- User 55 joins Healthy Life Circle
(4, 56, NOW()),   -- User 56 joins Family Harmony Workshop
(5, 57, NOW()),   -- User 57 joins Financial Freedom Club
(6, 58, NOW()),   -- User 58 joins Mind-Body Reset Session
(7, 59, NOW()),   -- User 59 joins Healing & Energy Renewal
(8, 60, NOW());   -- User 60 joins Conscious Communication Lab


SET FOREIGN_KEY_CHECKS = 1;

-- 22.10.25 begin
#SET SQL_SAFE_UPDATES = 0;
#UPDATE courses
#SET connect_link = CASE course_id
#    WHEN 17 THEN 'https://meet.google.com/mindfulness-basics'
#    ELSE 'https://zoom.us/healthy-mind-life'
#END;
#SET SQL_SAFE_UPDATES = 1;
-- end


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
