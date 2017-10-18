SELECT c.name category, count(title) number
FROM film f, film_category f_c, category c
WHERE f.film_id = f_c.film_id AND f_c.category_id = c.category_id
GROUP BY c.name
HAVING count(title)>=60
ORDER BY count(title) DESC;