from task1.connection import Connection

queries = [
    """CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE)""",

    """CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE);""",

    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        CONSTRAINT fk_status FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
        CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);
    """,

    """INSERT INTO status (name)
        VALUES
        ('new'),
        ('in progress'),
        ('completed')
    ON CONFLICT (name) DO NOTHING;"""
]

if __name__ == '__main__':
    connection = Connection()
    cursor = connection.get_cursor()

    for query in queries:
        cursor.execute(query)

    connection.commit()
