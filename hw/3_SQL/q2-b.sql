CREATE VIEW horror_view AS
SELECT DISTINCT cu.customer_id
FROM customer cu, film_category f_c, film f, inventory i, rental r
WHERE cu.customer_id = r.customer_id AND f.film_id = f_c.film_id AND f_c.category_id = 11 AND f.film_id = i.film_id AND i.inventory_id = r.inventory_id
ORDER BY cu.customer_id;