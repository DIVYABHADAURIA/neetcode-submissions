-- Write your query below
with cte as ( select * from orders where customer_id not in (select customer_id from orders where product_name = 'C'))
select distinct a.customer_id,c.customer_name from cte a join cte b on a.customer_id = b.customer_id and a.product_name = 'A' and b.product_name = 'B' 
join customers c on a.customer_id = c.customer_id
order by c.customer_name







