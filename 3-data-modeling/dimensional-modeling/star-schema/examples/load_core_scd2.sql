--- ======================
with batch as (
	select current_timestamp as batch_tm
),
change as (
	select 
		c.customer_id ,
		c.first_name ,
		c.last_name ,
		c.city ,
		c.country ,
		c.phone
	from public.customer c 
	join core.dim_customer dc on dc.customer_id = c.customer_id
		and dc.is_current = true
	where (
			dc.first_name  is distinct from c.first_name 
		or	dc.last_name   is distinct from c.last_name
		or  dc.city        is distinct from c.city 
		or 	dc.country 	   is distinct from c.country 
		or  dc.phone 	   is distinct from c.phone 
	)
)
update core.dim_customer dc
	set end_dt = b.batch_tm,
		is_current = false
from change c, batch b
where dc.customer_id = c.customer_id 
	and is_current = true;

insert into core.dim_customer (customer_id, first_name, last_name, city, country, phone, start_dt)
select 
	customer_id ,
	first_name ,
	last_name ,
	city ,
	country ,
	phone,
	b.batch_tm as start_dt 
from
(
	select
		customer_id ,
		first_name ,
		last_name ,
		city ,
		country ,
		phone
	from public.customer c
	where not exists(  
		select 1
		from core.dim_customer dc
		where dc.customer_id = c.customer_id
			and dc.is_current = true
	)
	union all

	select
		customer_id ,
		first_name ,
		last_name ,
		city ,
		country ,
		phone
	from change
	
) src
cross join batch b
