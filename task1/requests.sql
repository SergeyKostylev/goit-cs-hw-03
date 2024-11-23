-- Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 99;

-- Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = (SELECT id FROM statuses WHERE name = 'new');

-- Оновити статус конкретного завдання
UPDATE tasks SET status_id = (SELECT id FROM statuses WHERE name = 'in progress') WHERE id = 99;

-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users LEFT JOIN tasks ON (users.id = tasks.user_id) WHERE tasks.id is null

-- Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Task Name', 'Description', 1, 1);

-- Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM statuses WHERE name = 'completed');

-- Видалити конкретне завдання
DELETE FROM tasks WHERE id = 99;

-- Знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%user_name%';

-- Оновити ім'я користувача
UPDATE users SET fullname = 'New Name' WHERE id = 99;

-- Отримати кількість завдань для кожного статусу
SELECT status_id, COUNT(*) FROM tasks GROUP BY status_id;

-- Отримати завдання, що не мають опису
SELECT * FROM tasks WHERE description IS NULL or description = '';

-- Вибрати користувачів та їхні завдання у статусі 'in progress'
SELECT u.fullname, t.title FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = (SELECT id FROM statuses WHERE name = 'in progress');

-- Отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.id;