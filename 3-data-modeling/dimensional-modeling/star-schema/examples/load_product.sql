--Implemented Slowly Changing Dimension Type 2 for product dimension using PostgreSQL with batch-based processing and NULL-safe change detection
with batch as (
	select current_timestamp as batch_tm
),
change as (
	select 
		p.product_id ,
		p.product_name ,
		s.company_name ,
		s.contact_name ,
		p.unit_price ,
		p.package,
    p.is_discontinued
	from public.product p 
  join supplier s on s.supplier_id = p.supplier_id  
	join core.dim_product dp on dp.product_id = p.product_id
		and dp.is_current = true
	where (
			dp.product_name       is distinct from p.product_name
  or dp.suppliers_company_name    is distinct from s.company_name
  or dp.suppliers_contact_name    is distinct from s.contact_name
  or dp.unit_price                is distinct from p.unit_price
  or dp.package                   is distinct from p.package
  or dp.is_discontinued           is distinct from p.is_discontinued
	)
)
--update core.dim_product dp
--	set end_dt = b.batch_tm,
--		is_current = false
--from change c, batch b
--where dp.product_id = c.product_id 
--	and is_current = true;

insert into core.dim_product (product_id,	product_name, suppliers_company_name, suppliers_contact_name, unit_price, package, is_discontinued, start_dt)
select 
	product_id,	
	product_name, 
	company_name, 
	contact_name, 
	unit_price, package, 
	is_discontinued,
	b.batch_tm as start_dt 
from
(
	select
		product_id,	
		product_name, 
		company_name, 
		contact_name, 
		unit_price, package, 
		is_discontinued
	from public.product p 
  	join supplier s on s.supplier_id = p.supplier_id
	where not exists(  
		select 1
		from core.dim_product dp
		where dp.product_id = p.product_id
			and dp.is_current = true
	)
	union all

	select
		product_id,	product_name, company_name, contact_name, unit_price, package, is_discontinued
	from change
	
) src
cross join batch b
