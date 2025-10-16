**Мини-тест: Уровень владения рекурсивными CTE**

**Вопрос 1: Базовая структура**

  Какие две обязательные части есть в рекурсивном CTE?
    
    A) _________________________
    B) _________________________

**Вопрос 2: Поиск ошибки**

  Что не так в этом запросе? Исправить одну строку.
    
    WITH RECURSIVE numbers AS (
        SELECT 1 as n
        UNION
        SELECT n + 1 FROM numbers WHERE n < 5
    )
    SELECT * FROM numbers;

**Вопрос 3: Логика соединения**

    WITH RECURSIVE hierarchy AS (
        SELECT id, name, manager_id FROM employees WHERE id = 1
        UNION ALL
        SELECT e.id, e.name, e.manager_id
        FROM employees e
        JOIN hierarchy h ON e.manager_id = h.id  -- ← Эта строка
    )

**Вопрос 4: Практическая задача**
    
  Напишите рекурсивный CTE который генерирует числа от 10 до 1 (в обратном порядке).
