import pandas as pd
from backend.database import get_db

def fetch_courses():
    query = """
        SELECT 
            c.course_id,
            c.title,
            b.branch_name AS Branch,
            u.full_name AS Expert,
            c.language,
            c.price,
            c.avg_rating,
            c.total_students,
            c.is_active,
            c.begin_date,
            c.end_date
        FROM courses c
        JOIN experts e ON c.expert_id = e.expert_id
        JOIN users u ON e.user_id = u.user_id
        JOIN branches b ON c.branch_id = b.branch_id
        ORDER BY c.domain, c.avg_rating DESC;
    """
    conn = get_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_experts():
    query = """
        SELECT 
            e.expert_id,
            u.full_name AS Expert,
            b.branch_name AS Branch,
            e.experience_years,
            e.expert_rating,
            COUNT(c.course_id) AS total_courses
        FROM experts e
        JOIN users u ON e.user_id = u.user_id
        JOIN branches b ON e.branch_id = b.branch_id
        LEFT JOIN courses c ON e.expert_id = c.expert_id
        GROUP BY e.expert_id, u.full_name, b.branch_name, e.experience_years, e.expert_rating
        ORDER BY e.expert_rating DESC, total_courses DESC;
    """
    conn = get_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df