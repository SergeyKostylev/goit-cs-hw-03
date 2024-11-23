from faker import Faker
import random
from task1.connection import Connection

def fill_users(amount: int = 100):
    fake = Faker()
    connection = Connection()
    cursor = connection.get_cursor()

    for _ in range(amount):
        sql = f"""
        INSERT INTO users
            (fullname, email) VALUES ('{fake.name()}', '{fake.email()}')
            ON CONFLICT (email) DO NOTHING;
        """
        cursor.execute(sql)

    connection.commit()
    print('Users were added')


def fill_tasks(amount: int = 100):
    fake = Faker()
    connection = Connection()
    cursor = connection.get_cursor()

    user_ids = []
    for user_id in connection.fetchall("SELECT id FROM users"):
        user_ids.append(user_id[0])

    status_ids = []
    for status_id in connection.fetchall("SELECT id FROM status"):
        status_ids.append(status_id[0])

    for _ in range(amount):
        sql = f"""
        INSERT INTO tasks
            (title, description, status_id, user_id) VALUES ('{fake.job()}', '{fake.text()}', {random.choice(status_ids)}, {random.choice(user_ids)});
        """
        cursor.execute(sql)

    connection.commit()
    print('Tasks were added')


if __name__ == "__main__":
    # table status was filled after creation
    fill_users(10)
    fill_tasks(10)
