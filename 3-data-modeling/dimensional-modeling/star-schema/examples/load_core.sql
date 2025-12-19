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

update core.dim_customer dc
set end_dt = current_timestamp, 
	is_current = false 
from public.customer c
where dc.customer_id = c.customer_id 
	and is_current = true
	and(
			dc.first_name  <> c.first_name 
		or	dc.last_name   <> c.last_name
		or  dc.city        <> c.city 
		or 	dc.country 	   <> c.country 
		or  dc.phone 	   <> c.phone 
	);
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
join core.dim_customer dc on dc.customer_id = c.customer_id
where 
	dc.is_current = false
	and dc.end_dt = (
		select max(end_dt)
		from core.dim_customer 
		where c.customer_id = dc.customer_id 
	)
