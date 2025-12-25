insert into core.fact_sales(customer_fk, product_fk, date_pk, unit_price, quantity, total_amount)
select
	dc.customer_pk , 
	dp.product_pk , 
	dd.date_pk , 
	oi.unit_price,
	oi.quantity, 
	oi.unit_price * oi.quantity as total_amount
from public."order" o 
join public.order_item oi on o.order_id = oi.order_id 
join core.dim_customer dc on dc.customer_id = o.customer_id 
		and dc.is_current = true
join core.dim_product dp on dp.product_id = oi.product_id 
		and dp.is_current = true
join core.dim_date dd on dd.full_date = o.order_date 
where not exists (
	select 1
	from core.fact_sales f
	where 
		f.customer_fk = dc.customer_pk
		and f.product_fk = dp.product_pk
		and f.date_pk = dd.date_pk
)
