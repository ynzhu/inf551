SELECT title, c.name category
FROM film f, film_category f_c, category c
WHERE f.film_id = f_c.film_id AND f_c.category_id = c.category_id
ORDER BY title ASC;