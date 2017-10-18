SELECT COUNT(DISTINCT r.customer_id) number
FROM rental r, customer, film f, inventory i, film_category f_c
WHERE f_c.category_id = 1 AND f_c.film_id = f.film_id 
AND customer.active = 1 AND f.film_id = i.film_id AND i.inventory_id = r.inventory_id;
