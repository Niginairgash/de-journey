-- load data from public to core
insert into core.dim_customer (customer_id, first_name, last_name, city, country, phone, start_dt)
select 
	customer_id ,
	first_name ,
	last_name ,
	city ,
	country ,
	phone,
	current_timestamp as start_dt
from public.customer c 
where not exists(  
	select 1
	from core.dim_customer dc
	where dc.customer_id = c.customer_id
		and dc.is_current = true
)
