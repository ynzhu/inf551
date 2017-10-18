SELECT customer_id
FROM action_view
WHERE action_view.customer_id NOT IN (SELECT horror_view.customer_id FROM horror_view);