SELECT DISTINCT CONCAT(first_name, " ", last_name) as name
FROM film_actor f_a, actor a
WHERE f_a.actor_id = a.actor_id
GROUP BY f_a.actor_id
HAVING count(f_a.film_id) > 1
ORDER BY name ASC;
