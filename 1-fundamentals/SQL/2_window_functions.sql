-- Table: employee_performance - emp_id, department, team, salary, sales

select emp_id, department, team, salary, sales,
    avg(salary) over(partition by department) as avg_dept_salary,
    avg(salary) over(partition by team) as avg_team_salary,
    avg(sales) over(partition by department) as avg_dept_sales,
    rank() over(partition by department order by salary desc) as rn_dept_salary,
    rank() over(partition by team order by sales) as rn_team_sales
from employee_performance

/*
Задача 2: Разные ORDER BY для разных окон
Таблица: products - product_id, category, price, rating, created_date
Задача: Для каждого товара показать:
- Цену и рейтинг
- Рейтинг по цене (дорогие первые)
- Рейтинг по рейтингу (высокий рейтинг первые)
- Рейтинг по дате создания (новые первые)
- Самый дорогой товар в категории
-- products - product_id, category, price, rating, created_date
*/
select product_id, category, price, rating, created_date,
    row_number() over(partition by category order by price desc) as rn,
    row_number() over(partition by category order by rating desc) as rank_rating,
    row_number() over(partition by category order by created_date desc) as new_product,
    max(price) over(partition by category) as rn_product
from products

/*
Задача 3: Окна с агрегатами и ранжированием
Таблица: student_scores - student_id, subject, semester, score
Задача: Для каждой оценки студента показать:
- Текущий балл
- Средний балл студента по всем предметам
- Лучший балл студента по этому предмету
- Рейтинг студента в семестре по этому предмету
- Разницу с средним баллом группы по предмету
*/

select student_id, subject, semester, score,
    avg(score) over(partition by student_id) as avg_st_score,
    max(score) over(partition by student_id ) as best_score,
    row_number() over(partition by student_id order by semester, score) as rn,
    score - avg(score) over(partition by student_id) as diff_from_st_avg
from student_scores

/*
Задача 4: LAG/LEAD с разными смещениями
Таблица: monthly_finance - month, revenue, expenses, profit
Задача: Для каждого месяца показать:
- Выручку и прибыль
- Выручку за предыдущий месяц
- Выручку за тот же месяц год назад
- Прогноз выручки на следующий месяц
- Изменение прибыли compared to предыдущему месяцу
*/
select month, revenue, expenses, profit,
    lag(profit) over(partition by revenue order by month),

    lead(profit) over(partition by revenue order by month)
/*
Задача 5: Комбинированный анализ с фильтрацией
Таблица: customer_orders - order_id, customer_id, order_date, amount, category

Задача: Найти клиентов, у которых:

Средний чек выше среднего по всем клиентам

Есть заказы в премиум категориях (amount > 1000)

Показать их ранг по общей сумме заказов

Показать количество дней с момента последнего заказа
*/